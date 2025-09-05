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
