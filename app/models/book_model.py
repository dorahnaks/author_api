class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    title = db.Column(db.String(50))
    price = db.Column(db.String(50))
    description = db.Column(db.String(100))
    isbn = db.Column(db.String(50))
    image = db.Column(db.String(50))
    no_of_pages = db.Column(db.String(50))
    price_unit = db.Column(db.String(50))
    publication_year = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    specialisation = db.Column(db.String(50))
    
    
    def __init__(self, id, title, price, description, isbn, image, no_of_pages, price_unit, publication_year, genre, specialisation):
        pass