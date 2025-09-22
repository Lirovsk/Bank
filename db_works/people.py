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
        """
        Adds a Pessoa object to the database using the provided SQLAlchemy engine.
        Args:
            person (Pessoa): The person object to be added to the database.
            engine (Engine): The SQLAlchemy engine instance connected to the target database.
        Raises:
            SQLAlchemyError: If there is an error during the database transaction.
        Example:
            add_person_to_db(person_instance, engine)
        """
        
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

    @staticmethod
    def get_people_by_name(name: str, engine: Engine, password: str):
        """Retrieves a person instance from the database by name."""
        with Session(engine) as session:
            person = session.query(Pessoa).filter(Pessoa.nome == name).first()
        
        if person and person.senha == password:
            return person
        return None
    