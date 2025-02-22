from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import ReportItemForm, SearchItemForm
from app.models import LostItem

@app.route('/')
def index():
    form = SearchItemForm()
    return render_template('index.html', form=form)

@app.route('/report_item', methods=['GET', 'POST'])
def report_item():
    form = ReportItemForm()
    if form.validate_on_submit():
        item = LostItem(
            item_name=form.item_name.data,
            description=form.description.data,
            location=form.location.data,
            date_lost=form.date_lost.data,
            contact_info=form.contact_info.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Item reported successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('report_item.html', form=form)

@app.route('/search_items', methods=['GET', 'POST'])
def search_items():
    form = SearchItemForm()
    if form.validate_on_submit():
        search_query = form.search_query.data
        results = LostItem.query.filter(
            (LostItem.item_name.contains(search_query)) | 
            (LostItem.location.contains(search_query))
        ).all()
        return render_template('search_items.html', results=results, form=form)
    return redirect(url_for('index'))

@app.route('/item/<int:item_id>')
def item_details(item_id):
    item = LostItem.query.get_or_404(item_id)
    return render_template('item_details.html', item=item)