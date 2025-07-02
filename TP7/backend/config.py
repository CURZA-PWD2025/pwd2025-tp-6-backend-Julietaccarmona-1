#####import os
####class Config:
####    SQLALCHEMY_DATABASE_URI = os.getenv(
    ####    "DATABASE_URL",
        #####"sqlite:///tienda.db"      
    ###)
 #####   SQLALCHEMY_TRACK_MODIFICATIONS = False


import os

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
