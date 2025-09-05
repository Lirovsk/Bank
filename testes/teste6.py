from db_works import (agenciesManager, 
                      agencyStorageCreation, 
                      peopleManagement,
                      operations)
from sqlalchemy.orm import Session
import os

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
