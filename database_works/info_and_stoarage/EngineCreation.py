from ...Models.Conta_e_pessoa import Conta, Cliente
from sqlalchemy import create_engine
from database_works.info_and_stoarage.Model import engineInformation


class EngineConfig:
    
    @staticmethod
    def engine_creation():
        pass

    @staticmethod
    def storage_info():
        pass

    @staticmethod
    def retrieve_data():
        pass


class ContaConfig():
    
    @staticmethod
    def create_account():
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
    def create_client():
        pass

    @staticmethod
    def delete_client():
        pass

    @staticmethod
    def retrieve_client():
        pass

    @staticmethod
    def update_client():
        pass
