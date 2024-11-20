"""Copyright (c) 2024."""

from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Product:
    """Product model."""

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    quantity: Mapped[int]
