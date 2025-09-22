from pymongo import MongoClient
import datetime
from urllib.parse import quote_plus

username = quote_plus("Lirovsk")
password = quote_plus("f0guet@oS2")

uri = f"mongodb+srv://{username}:{password}@cluster0.6jrv4gw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client["bank_operations"]
operations_collection = db["operations"]

class saveOperations:
    
    
    @staticmethod
    def save_operation(operation_type: str, account_number: int, amount: float, status: str, account_number_to: int = None):
        """
        Saves an operation record to the MongoDB collection.
        Args:
            operation_type (str): The type of operation (e.g., 'withdraw', 'deposit', 'transfer').
            account_number (int): The account number associated with the operation.
            amount (float): The amount involved in the operation.
            status (str): The status of the operation (e.g., 'success', 'failed').
        """
        if operation_type != "transfer":
            operation_record = {
                "operation_type": operation_type,
                "account_number": account_number,
                "amount": amount,
                "status": status,
                "timestamp": datetime.datetime.now(datetime.UTC)
            }
            operations_collection.insert_one(operation_record)
        else:
            operation_record = {
                "operation_type": operation_type,
                "account_number_from": account_number,
                "account_number_to": account_number_to,
                "amount": amount,
                "status": status,
                "timestamp": datetime.datetime.now(datetime.UTC)
            }
            operations_collection.insert_one(operation_record)
    
    @staticmethod    
    def get_operations(account_number: int):
        """
        Retrieve all operations related to a specific account number.
        This function queries the operations collection for documents where the given
        account number appears either as the main account number, as the sender
        (account_number_from), or as the receiver (account_number_to). It combines
        the results from both queries and returns a list of all matching operations.
        Args:
            account_number (int): The account number to search for in operations.
        Returns:
            list: A list of operation documents related to the specified account number.
        """
        number = str(account_number)
        
        list_operations = operations_collection.find({"account_number": number})
        second_list_operations = operations_collection.find({"$or": [{"account_number_from": number}, {"account_number_to": number}]})
        all_operations = list(list_operations) + list(second_list_operations)
        
        return all_operations
    
    @staticmethod
    def get_daily_operations(account_number: int, date: datetime.date):
        """
        Retrieves all operations for a given account that occurred on a specific date.
        Args:
            account_number (int): The account number to retrieve operations for.
            date (datetime.date): The date to filter operations by.
        Returns:
            list: A list of operation dictionaries that occurred on the specified date.
        """
        
        list_operations = saveOperations.get_operations(account_number)
        daily_operations = [op for op in list_operations if op['timestamp'].date() == date]
        
        return daily_operations