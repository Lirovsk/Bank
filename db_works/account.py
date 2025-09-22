from sqlalchemy.orm import Session
from sqlalchemy import Engine
from .Models import Conta, Pessoa

class accountManagement:

    @staticmethod
    def create_account(numero: int, saldo: float, senha: str):
        """Creates a new account instance."""
        new_account = Conta(numero=numero, saldo=saldo, senha=senha)
        return new_account

    @staticmethod
    def add_account_to_db(account: Conta, people: Pessoa, engine: Engine):
        """Adds an account instance to the database."""
        
        with Session(engine) as session:
            pessoa = session.query(Pessoa).filter(Pessoa.id == people.id).first()
            if pessoa:
                pessoa.conta.append(account)
                session.commit()

    @staticmethod
    def delete_account(account_id: int, engine: Engine):
        """Deletes an account instance from the database."""
        with Session(engine) as session:
            account = session.query(Conta).filter(Conta.id == account_id).first()
            if account:
                session.delete(account)
                session.commit()

    @staticmethod
    def filter_accounts_by_owner(id_owner: int, engine: Engine):
        """Filters accounts by the owner's ID."""
        with Session(engine) as session:
            accounts = session.query(Conta).filter(Conta.pessoa_id == id_owner).all()
            return accounts
        
    @staticmethod
    def get_all_accounts(person_id: int, engine: Engine):
        """
        Retrieves all accounts associated with a given person ID.
        Args:
            person_id (int): The unique identifier of the person whose accounts are to be retrieved.
            engine (Engine): The SQLAlchemy engine used to connect to the database.
        Returns:
            list: A list of Conta objects associated with the person ID.
        Raises:
            Exception: Prints an error message if an exception occurs during the database query.
        """
        
        with Session(engine) as session:
            try:
                accounts = session.query(Conta).filter(Conta.pessoa_id == person_id).all()
                return accounts
            except Exception as e:
                print(f"Error occurred: {e}")
        return []
