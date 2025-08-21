from sqlalchemy.orm import (Mapped,
                            DeclarativeBase,
                            relationship,
                            mapped_column
                            )
from sqlalchemy import ForeignKey, create_engine



class Base(DeclarativeBase):
    pass


class Cliente(Base):
    __tablename__ = "Clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    nome: Mapped[str] 
    idade: Mapped[int] 
    email: Mapped[str] 
    contas: Mapped[list["Conta"]] = relationship(back_populates="cliente")


class Conta(Base):
    __tablename__ = "Contas"

    id: Mapped[int] = mapped_column(primary_key=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    numero: Mapped[str] = mapped_column()
    saldo: Mapped[float] = mapped_column()
    cliente_id: Mapped[int] = mapped_column(ForeignKey("Clientes.id"))
    cliente: Mapped[Cliente] = relationship(back_populates="contas")
