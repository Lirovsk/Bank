# the following path is the database file for the agency
# remember to ensure that the new path set by exists on the filesystem
PATH = "info_of_agency.db"

from .Models import engine, Base, BasePeopleAccounts, Pessoa, Conta
from sqlalchemy import Inspector
from .agency_access import agenciesManager
from .agency_creation import agencyCreation
from .agency_creation import agencyStorageCreation
from .people import peopleManagement
    

__version__ = "0.3.0"