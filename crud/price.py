from sqlalchemy.orm import Session

from models.price import Price 
from schema.price import Price as schema_price

def get_price(db: Session):
    price = db.query(Price).all()
    return price[0] if price else None