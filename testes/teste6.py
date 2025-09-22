from db_works import (agenciesManager, 
                      agencyStorageCreation, 
                      peopleManagement,
                      operations,
                      accountManagement)
from sqlalchemy.orm import Session
import os

#this a overall test os the system

agencies = agenciesManager.retrieve_agencies_info()
for agency in agencies:
    print(agency.name)

selected_agency = input("what agency do you want to use: ")
try:
    agency_info = agenciesManager.retrieve_agency_info(selected_agency)
    if agency_info:
        print(f"Agency found: {agency_info.name}")
    else:
        print("Agency not found.")
except Exception as e:
    print(f"Error retrieving agency information: {e}")

engine = agenciesManager.recreate_engine_for_agency(agency_info)
agenciesManager.create_table(engine)

name = input("Enter your name: ")
os.system('cls')
password = input("Enter your password: ")

person = peopleManagement.get_people_by_name(name, engine, password)
if person:
    print(f"Welcome {person.nome}!")
else:
    print("Invalid credentials.")

print("Which operation do you want to do?")
input_operation = input("1 - Withdraw\n2 - Deposit\n")

match input_operation:
    case '1':
        accounts = accountManagement.get_all_accounts(person.id, engine)
        for account in accounts:
            print(f"Account Number: {account.numero}, Balance: {account.saldo}")
        account_number = input("Enter your account number: ")
        password_ = input("Enter your password: ")
        amount = float(input("Enter the amount to withdraw: "))
        operations.withdraw(account_number, amount, password_, engine)
    case '2':
        accounts = accountManagement.get_all_accounts(person.id, engine)
        for account in accounts:
            print(f"Account Number: {account.numero}, Balance: {account.saldo}")
        account_number = input("Enter your account number: ")
        password_ = input("Enter your password: ")
        amount = float(input("Enter the amount to deposit: "))
        operations.deposit(account_number, amount, password_, engine)
    case _:
        print("Invalid operation selected.")
        