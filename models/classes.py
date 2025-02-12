class Company:
    def __init__(self, name, email, contact, location): # constructor
        self.name = name
        self.email = email
        self.contact = contact
        self.location = location

dorah_foods = Company('Dorah foods', 'dorahfoods@gmail.com', +256709435591, 'Wakiso') # creating an instance
print(dorah_foods.name)
print(f'You can contact {dorah_foods.name} via email: {dorah_foods.email} or call: {dorah_foods.contact}')


class Author:
    def __init__(self, name, age, nationality, experience_years, email):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.experience_years = experience_years
        self.email = email
        
    def details(self):
        print(f"{self.name} is {self.age} years old and is {self.nationality}.")
    
    def experience(self):
        print(f"{self.name} is an author with an experience of about {self.experience_years} years.")
    
author1 = Author("Dorah Naks", 20, "Ugandan", 2, "dorahnakslove@gmail.com")
author1.details()
author1.experience()

class Book:
    def __init__(self, title, publication_year, edition, genre, ratings):
        self.title = title
        self.publication_year = publication_year
        self.edition = edition
        self.genre = genre
        self.ratings = ratings
        
    def book_info(self):
        print(f"{self.title} {self.edition} edition is of genre {self.genre} with ratings ({self.ratings})  ")
    
    def get_publication_year(self):
        print(f"The publication year of {self.title} is {self.publication_year}")
    
book1 = Book("Myras Journey", 2025, "1st", "Horror", 4.7)
book1.book_info()
book1.get_publication_year()