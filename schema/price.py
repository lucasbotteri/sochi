from pydantic import BaseModel

class PriceBase(BaseModel):
    simpleSide: float
    doubleSide: float
    shipping: float
    ringedSmall: float
    ringedMedium: float
    ringedLarge: float
    

class PriceCreate(PriceBase):
    pass

class Price(PriceBase):
    id: int

    class Config:
        orm_mode = True
