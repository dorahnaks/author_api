from app.extensions import db
from datetime import datetime


class Author(db.Model):
    __tablename__ = "author's"
    id = db.Column(db.Integer, primary_key=True, nullablle=False)
    first_name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))
    last_name = db.Column(db.String(20))
    contact = db.Column(db.Integer(20))
    email = db.Column(db.String(20), nullablle=False, unique=True)
    password = db.Column(db.String(20), nullablle=False)
    image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime,  default = datetime.now())
    updated_at = db.Column(db.DateTime,  onupdate = datetime.now())
    
    
    def __init__(self, id, first_name, last_name, contact, email, password, image, created_at, updated_at):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.email = email
        self.password = password
        self.image = image
        self.created_at = created_at
        self.updated_at = updated_at
        
    
    
