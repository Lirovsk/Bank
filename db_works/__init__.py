from .Model import engine, Base
from sqlalchemy import Inspector

inspector = Inspector(engine)

if not (inspector.has_table("agency_info")):
    Base.metadata.create_all(engine)
    

    