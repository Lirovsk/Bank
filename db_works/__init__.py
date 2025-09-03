from .Models.Model import engine, Base
from sqlalchemy import Inspector
from .agency_access import agenciesManager
from .agency_creation import agencyCreation
from .agency_creation import agencyStorageCreation

inspector = Inspector(engine)

if not (inspector.has_table("agency_info")):
    Base.metadata.create_all(engine)
    

__version__ = "0.1.0"