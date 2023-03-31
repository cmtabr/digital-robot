from sqlalchemy import Column, Integer
from models.base import Base

# Define a model class for 'axis' table
class Axis(Base):
    __tablename__ = 'axis'
    id = Column(Integer, primary_key=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    z = Column(Integer, nullable=False)
    r = Column(Integer, nullable=False)
