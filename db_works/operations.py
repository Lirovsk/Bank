from sqlalchemy import Engine
from sqlalchemy.orm import Session

from db_works.Models.people_accounts import Conta

class operations:
    
    @staticmethod
    def withdraw(account_number: str, amount: float, password: str, engine: Engine):
        """
        Withdraws a specified amount from a user's account after verifying credentials.
        Args:
            account_number (str): The unique identifier of the account to withdraw from.
            amount (float): The amount of money to withdraw.
            password (str): The password for account authentication.
            engine (Engine): The SQLAlchemy engine instance for database connection.
        Returns:
            None
        Raises:
            Exception: If the account does not exist, the password is incorrect, or the withdrawal fails.
        Note:
            After a successful withdrawal, the operation should be saved using a NoSQL database (implementation pending).
        """
        
        with Session(engine) as session:
            account = session.query(Conta).filter_by(Conta.id ==account_number).first()

        if (account_number != None) and (account.senha == password):
            done = dbOperations.db_withdraw(account, amount, engine)
        
        if done:
            #save the operation using the nosql
            pass
        

    @staticmethod
    def deposit(account_number: str, amount: float, password: str, engine: Engine):
        """
        Deposits a specified amount into an account after verifying the account number and password.
        Args:
            account_number (str): The unique identifier of the account to deposit into.
            amount (float): The amount of money to deposit.
            password (str): The password for account authentication.
            engine (Engine): The SQLAlchemy engine used for database connection.
        Returns:
            None
        Raises:
            Exception: If the account is not found or the password is incorrect.
        Note:
            After a successful deposit, the operation should be saved using a NoSQL database (implementation pending).
        """
        
        with Session(engine) as session:
            account = session.query(Conta).filter_by(Conta.id == account_number).first()

        if (account_number != None) and (account.senha == password):
            done = dbOperations.db_deposit(account, amount, engine)

        if done:
            #save the operation using the nosql
            pass

    @staticmethod
    def transfer(account_number_from: str, account_number_to: str, amount: float, password: str, engine: Engine):
        """
        Transfers a specified amount from one account to another after verifying credentials.
        Args:
            account_number_from (str): The account number to transfer funds from.
            account_number_to (str): The account number to transfer funds to.
            amount (float): The amount of money to transfer.
            password (str): The password for the source account for authentication.
            engine (Engine): The SQLAlchemy engine instance for database connection.
        Returns:
            None
        Side Effects:
            - Performs a transfer operation in the database if credentials are valid.
            - Intended to log the operation in a NoSQL database (not yet implemented).
        Raises:
            None explicitly, but may raise exceptions from underlying database operations.
        """
        
        with Session(engine) as session:
            account_from = session.query(Conta).filter_by(Conta.id == account_number_from).first()
            account_to = session.query(Conta).filter_by(Conta.id == account_number_to).first()

        if (account_from != None) and (account_to != None) and (account_from.senha == password):
            done = dbOperations.db_transfer(account_from, account_to, amount, engine)

        if done:
            #save the operation using the nosql
            pass

    @staticmethod
    def get_balance(account_number: str, engine: Engine):
        """
        Retrieves the balance for a given account number.
        Args:
            account_number (str): The unique identifier of the account whose balance is to be retrieved.
            engine (Engine): The SQLAlchemy engine instance used to connect to the database.
        Returns:
            float or None: The balance of the account if found, otherwise None.
        """
        
        with Session(engine) as session:
            account = session.query(Conta).filter_by(Conta.id == account_number).first()
            if account != None:
                return dbOperations.db_get_balance(account, engine)
        return None


class dbOperations:

    @staticmethod
    def db_withdraw(account: Conta, amount: float, engine: Engine):
        """
        Withdraws a specified amount from the given account and updates the balance in the database.
        Args:
            account (Conta): The account object from which the amount will be withdrawn.
            amount (float): The amount of money to withdraw.
            engine (Engine): The SQLAlchemy engine used to connect to the database.
        Raises:
            Exception: If an error occurs during the withdrawal process, the transaction is rolled back and the error is printed.
        Note:
            This function assumes that the account exists in the database and that the balance is sufficient for the withdrawal.
        """
        
        with Session(engine) as session:
            try:
                _account = session.query(Conta).filter(Conta.id == account.id).first()
                _account.saldo -= amount
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred: {e}")
        pass

    @staticmethod
    def db_deposit(account: Conta, amount: float, engine: Engine):
        """
        Deposits a specified amount into the given account and updates the balance in the database.
        Args:
            account (Conta): The account object to deposit into.
            amount (float): The amount of money to deposit.
            engine (Engine): The SQLAlchemy engine used to connect to the database.
        Raises:
            Exception: If an error occurs during the database transaction, the exception is caught, the transaction is rolled back, and the error is printed.
        Note:
            This function assumes that the account exists in the database and that the balance is sufficient for the withdrawal.
        """
        
        with Session(engine) as session:
            
            try:
                _account = session.query(Conta).filter(Conta.id == account.id).first()
                _account.saldo += amount
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred: {e}")
        pass

    @staticmethod
    def db_transfer(account_from: Conta, account_to: Conta, amount: float, engine: Engine):
        """
        Transfers a specified amount from one account to another within a database transaction.
        Args:
            account_from (Conta): The source account from which the amount will be deducted.
            account_to (Conta): The destination account to which the amount will be added.
            amount (float): The amount of money to transfer.
            engine (Engine): The SQLAlchemy engine used to connect to the database.
        Raises:
            Exception: Rolls back the transaction and prints an error message if any exception occurs during the transfer.
        Note:
            This function assumes that both accounts exist in the database and that the source account has sufficient funds.
        """
        
        with Session(engine) as session:
            try:
                _account_from = session.query(Conta).filter(Conta.id == account_from.id).first()
                _account_to = session.query(Conta).filter(Conta.id == account_to.id).first()
                _account_from.saldo -= amount
                _account_to.saldo += amount
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred: {e}")
        pass

    @staticmethod
    def db_get_balance(account: Conta, engine: Engine):
        """
        Retrieve the balance (saldo) of a given account from the database.
        Args:
            account (Conta): The account object whose balance is to be retrieved.
            engine (Engine): The SQLAlchemy engine used to connect to the database.
        Returns:
            float or None: The balance of the account if found, otherwise None.
        Raises:
            Exception: Prints an error message if an exception occurs during the database query.
        """
        
        with Session(engine) as session:
            try:
                _account = session.query(Conta).filter(Conta.id == account.id).first()
                return _account.saldo
            except Exception as e:
                print(f"Error occurred: {e}")
        return None
