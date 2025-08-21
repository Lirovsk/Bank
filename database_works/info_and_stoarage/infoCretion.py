from ...Models.Conta_e_pessoa import Conta, Cliente
from sqlalchemy import create_engine
from database_works.info_and_stoarage.Model import engineInformation, Session
from ...Models.Conta_e_pessoa import Base as db_base

"""
This file contains configurations methods to manage information of engines (tables and collections information)
and methods to create, update, delete and retrieve engine information.
"""

class EngineConfig:
    
    @staticmethod
    def engine_creation(engine_name: str,):
        """returns the database url, an engine still needs to be created"""

        return f"sqlite:///{engine_name}.db"

    @staticmethod
    def storage_info(engine_name: str, version_local: str):
        """stores information about the engine in the database"""
        session = Session()
        try:
            session.add(engineInformation(name=engine_name, version=version_local))
            session.commit()
            session.close()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error creating engine: {e}")
            session.close()
            return False

    @staticmethod
    def retrieve_data(name: str):
        """retrieves engine information from the database"""
        session = Session()
        try:
            engine_info = session.query(engineInformation).filter_by(name=name).first()
            session.close()
            return engine_info
        except Exception as e:
            session.rollback()
            print(f"Error retrieving engine: {e}")
            session.close()
            return None

def create_db():
    """
    Creates a new database and stores its information.
    """
    nome = input("Enter the name of the database: ")
    version = input("Enter the version of the database: ")
    do_it = EngineConfig.storage_info(nome, version)

    if do_it:
        str = EngineConfig.engine_creation(nome)
        engine = create_engine(str)
        db_base.metadata.create_all(engine)

        return engine
    
    else:
        return False


def existing_engine():

    session = Session()
    try:
        engine_info = session.query(engineInformation).all()
        session.close()
    except Exception as e:
        session.rollback()
        print(f"Error retrieving engine: {e}")
        session.close()
        return None

    for engine in engine_info:
        print(f"Name: {engine.name}, Version: {engine.version}")

    needed_engine = input("Enter the name of the engine you want to use: ")
    engine = EngineConfig.retrieve_data(needed_engine)

    return create_engine(f"sqlite:///{engine.name}.db") if engine else None


class ContaConfig():
    
    @staticmethod
    def create_account():
        """Creates a new account in the database"""

        pass
    
    @staticmethod
    def delete_account():
        pass
    
    @staticmethod
    def retrieve_acount():
        pass
    
    @staticmethod
    def update_account():
        pass


class ClienteConfig():

    @staticmethod
    def create_client(engine):
        """Creates a new client in the database"""

        nome = input("Enter the name of the client: ")
        idade = int(input("Enter the age of the client: "))
        email = input("Enter the email of the client: ")
        senha = input("Enter the password of the client: ")

        new_client = Cliente(nome=nome, idade=idade, email=email, senha=senha)
        session = Session()
        try:
            session.add(new_client)
            session.commit()
            print(f"Client {nome} created successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error creating client: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_client(engine):
        """Deletes a client from the database"""
        name = input("Enter the name of the client to delete: ")
        session = Session()
        try:
            client = session.query(Cliente).filter_by(nome=name).first()
            if client:
                session.delete(client)
                session.commit()
                print(f"Client {name} deleted successfully.")
            else:
                print(f"No client found with name: {name}")
        except Exception as e:
            session.rollback()
            print(f"Error deleting client: {e}")
        finally:
            session.close()
        pass

    @staticmethod
    def retrieve_client(engine, name:str):
        session = Session()
        try:
            client = session.query(Cliente).filter_by(nome=name).first()
            return client
        except Exception as e:
            session.rollback()
            print(f"Error retrieving client: {e}")
        finally:
            session.close()

    @staticmethod
    def update_client(engine, name:str, **kwargs):
        session = Session()
        try:
            client = session.query(Cliente).filter_by(nome=name).first()
            if client:
                for key, value in kwargs.items():
                    setattr(client, key, value)
                session.commit()
                print(f"Client {name} updated successfully.")
            else:
                print(f"No client found with name: {name}")
        except Exception as e:
            session.rollback()
            print(f"Error updating client: {e}")
        finally:
            session.close()
