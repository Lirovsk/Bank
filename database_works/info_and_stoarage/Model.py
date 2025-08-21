from sqlalchemy import create_engine
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            DeclarativeBase,
                            sessionmaker)

engine = create_engine("sqlite:///bank.db")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

"""This file contains the model of the table that stores the engines information"""

class engineInformation(Base):
    __tablename__ = "engine_information"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[str] = mapped_column(nullable=False)
