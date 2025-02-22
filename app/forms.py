from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReportItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    date_lost = StringField('Date Lost', validators=[DataRequired()])
    contact_info = StringField('Contact Info', validators=[DataRequired()])
    submit = SubmitField('Report Item')

class SearchItemForm(FlaskForm):
    search_query = StringField('Search by Item Name or Location', validators=[DataRequired()])
    submit = SubmitField('Search')