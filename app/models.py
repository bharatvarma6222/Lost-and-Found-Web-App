from app import db

class LostItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_lost = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"LostItem('{self.item_name}', '{self.location}', '{self.date_lost}')"