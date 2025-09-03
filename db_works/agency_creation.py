from .Models.Model import Base, engine, agencyInfo
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from .Models.people_accounts import Pessoa, Conta
from .Models.people_accounts import Base as Base_pessoas

class agencyStorageCreation:
    def __init__(self, name: str, version: str, senha: str):
        self.name = name
        self.version = version
        self.senha = senha

    def create_agency_url(self):
        if self.version == "sqlite":
            return f"sqlite:///agencies/{self.name}.db"

    def storage_agency_info(self):
        try:
            with Session(engine) as session:
                new_agency = agencyInfo(name=self.name, version=self.version, senha=self.senha)
                session.add(new_agency)
                session.commit()
            return True
        except:
            return False



class agencyCreation:
    
    @staticmethod
    def create_all(engine):
        Base_pessoas.metadata.create_all(engine)


