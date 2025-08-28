from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            DeclarativeBase)
from sqlalchemy import create_engine

engine = create_engine("sqlite:///info_of_agency.db")

class Base(DeclarativeBase):
    pass

class agencyInfo(Base):
    __tablename__ = "agency_info"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[str]
    senha: Mapped[str] = mapped_column(nullable=False)
