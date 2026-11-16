from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)

    product_name: Mapped[str] = mapped_column(String(150), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    status: Mapped[str] = mapped_column(String(30), default="pending", nullable=False)
