from .Models import agencyInfo, engine, Base 
from sqlalchemy import Engine, Inspector, create_engine
from sqlalchemy.orm import Session
from .Models import BasePeopleAccounts

class agenciesManager:
    
    @staticmethod
    def retrieve_agencies_info():
        """Retrieve information about all agencies."""
        
        with Session(engine) as session:
            agencies = session.query(agencyInfo).all()
            return agencies

    @staticmethod
    def retrieve_agency_info(agency_name: str):
        """Retrieve information about a specific agency."""
        
        with Session(engine) as session:
            agency = session.query(agencyInfo).filter(agencyInfo.name == agency_name).first()
            return agency

    @staticmethod
    def delete_agency_info(agency_name: str):
        """Delete an agency."""
        
        with Session(engine) as session:
            agency = session.query(agencyInfo).filter(agencyInfo.name == agency_name).first()
            if agency:
                session.delete(agency)
                session.commit()
                
    @staticmethod
    def recreate_engine_for_agency(agency: agencyInfo):
        """creates a engine for an existing agency"""
        
        name = agency.name
        url = f"sqlite:///agencies/{name}.db"
        return create_engine(url)
    
    @staticmethod
    def create_table(engine: Engine):
        """creates the tables for an existing agency"""
        
        inspector = Inspector(engine)
        if not (inspector.has_table("pessoas") and inspector.has_table("contas")):
            from .agency_creation import agencyCreation
            BasePeopleAccounts.metadata.create_all(engine)
        
    