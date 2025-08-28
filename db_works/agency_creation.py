from .Model import Base, engine, agencyInfo
from sqlalchemy.orm import Session

class agencyCreation:
    def __init__(self, name: str, version: str, senha: str):
        self.name = name
        self.version = version
        self.senha = senha

    def create_agency_url(self):
        if self.version == "sqlite":
            return f"sqlite:///agencies/{self.name}.db"

    def storage_agency_info(self):
        with Session(engine) as session:
            new_agency = agencyInfo(name=self.name, version=self.version, senha=self.senha)
            session.add(new_agency)
            session.commit()

