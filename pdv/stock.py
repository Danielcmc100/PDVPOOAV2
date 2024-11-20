"""Copyright (c) 2024."""

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    registry,
    sessionmaker,
)

engine = create_engine("sqlite:///stock.db")
Session = sessionmaker(bind=engine)
session = Session()
reg = registry()


@reg.mapped_as_dataclass
class Product:
    """Product model."""

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    quantity: Mapped[int]


reg.metadata.create_all(engine)


def create_product(name: str, quantity: int) -> None:
    """Create stock."""
    product = Product(name=name, quantity=quantity)
    session.add(product)
    session.commit()


def get_product(stock_id: int) -> Product | None:
    """Get stock by id.

    Returns:
        Stock | None: Stock if found, None otherwise.

    """
    return session.query(Product).filter_by(id=stock_id).first()


def get_all_products() -> list[Product]:
    """Get all stocks.

    Returns:
        list[Stock]: All stocks.

    """
    return session.query(Product).all()


def update_product(
    stock_id: int,
    name: str | None = None,
    quantity: int | None = None,
) -> None:
    """Update stock by id."""
    stock = session.query(Product).filter_by(id=stock_id).first()
    if stock:
        if name:
            stock.name = name
        if quantity:
            stock.quantity = quantity
        session.commit()


def delete_product(stock_id: int) -> None:
    """Delete stock by id."""
    stock = session.query(Product).filter_by(id=stock_id).first()
    if stock:
        session.delete(stock)
        session.commit()
