from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            DeclarativeBase,
                            relationship)
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Pessoa(Base):
    __tablename__ = "pessoas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    idade: Mapped[int] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)
    conta: Mapped[list["Conta"]] = relationship(back_populates="pessoa")

class Conta(Base):
    __tablename__ = "contas"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(nullable=False)
    saldo: Mapped[float] = mapped_column(nullable=False)
    pessoa_id: Mapped[int] = mapped_column(ForeignKey("pessoas.id"))
    senha: Mapped[str] = mapped_column(nullable=False)
    pessoa: Mapped["Pessoa"] = relationship(back_populates="conta")
