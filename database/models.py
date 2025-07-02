from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "Inventario"

    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    component: Mapped[str] = mapped_column(nullable=False)
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    serialNo: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
    obs: Mapped[str] = mapped_column(nullable=True)
    create_date: Mapped[str] = mapped_column(nullable=False)
    update_date: Mapped[str] = mapped_column(nullable=False)
