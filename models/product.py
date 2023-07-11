from config.database import Base
from sqlalchemy import Column, Integer, String

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    about = Column(String)
    year = Column(Integer)
    units = Column(Integer)
    category = Column(String)