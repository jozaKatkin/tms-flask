class Config:
    DEBUG = True

    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_NAME = 'Products'
    DB_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'

