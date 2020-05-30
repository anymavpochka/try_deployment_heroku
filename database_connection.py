from sqlalchemy.engine import create_engine

# для создания таблиц Вам неободимо прописать путь к своей базе данніх oracle
DATABASE_URI = 'postgres://utemlymneonnou:12dd2bfa4d3cd28a04420436bdb9949257f3224994532766aad6120329c29bba@ec2-54-75-231-215.eu-west-1.compute.amazonaws.com:5432/dc2um1rbuc1avj'

engine = create_engine(DATABASE_URI)

