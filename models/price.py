from sqlalchemy import  Column, Integer, Float

from database import Base


class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True, index=True)
    simpleSide = Column(Float, )
    doubleSide = Column(Float)
    shipping = Column(Float)
    ringedSmall = Column(Float)
    ringedMedium = Column(Float)
    ringedLarge = Column(Float)
