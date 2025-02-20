class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))
    last_name = db.Column(db.String(20))
    contact = db.Column(db.Integer(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(20))
    image = db.Column(db.String(20))
    
    
    def __init__(self, id, first_name, last_name, contact, email, password, image):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.email = email
        self.password = password
        self.image = image
        
    def __repr__(self):
        return '<Product %d>' % self.id
db.create_all()
