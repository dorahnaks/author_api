class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/authors_db" # connection string
    JWT_SECRET_KEY = "authors" # secret key for jwt
