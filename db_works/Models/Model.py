from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            DeclarativeBase)
from sqlalchemy import create_engine, Inspector
from .. import PATH

engine = create_engine(f"sqlite:///{PATH}")

class Base(DeclarativeBase):
    pass

class agencyInfo(Base):
    __tablename__ = "agency_info"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[str]
    senha: Mapped[str] = mapped_column(nullable=False)

inspector = Inspector(engine)
if not (inspector.has_table("agency_info")):
    Base.metadata.create_all(engine)