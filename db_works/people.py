from .Models import BasePeopleAccounts, Pessoa
from sqlalchemy.orm import Session
from sqlalchemy import Engine

class peopleManagement:

    @staticmethod
    def create_people(name: str, age: int, email: str, senha: str):
        """Creates a new person instance."""

        new_person = Pessoa(nome=name, idade=age, email=email, senha=senha)
        return new_person

    @staticmethod
    def add_person_to_db(person: Pessoa, engine: Engine):
        """Adds a person instance to the database."""
        with Session(engine) as session:
            session.add(person)
            session.commit()
            
    @staticmethod
    def delete_people(name: str, engine: Engine):
        """Deletes a person instance from the database."""
        with Session(engine) as session:
            person = session.query(Pessoa).filter(Pessoa.nome == name).first()
            if person:
                session.delete(person)
                session.commit()
    
