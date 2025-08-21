from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            DeclarativeBase)

class Base(DeclarativeBase):
    pass


class engineInformation(Base):
    __tablename__ = "engine_information"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[str] = mapped_column(nullable=False)
