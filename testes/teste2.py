from db_works import agenciesManager

# Retrieve and display all agencies
agencies = agenciesManager.retrieve_agencies_info()
for agency in agencies:
    print(agency.name)
 
# Prompt user to choose an agency   
name = input("chose an agency: ")

# Retrieve the selected agency's information
agency = agenciesManager.retrieve_agency_info(name)

# Recreate the database engine for the selected agency
engine = agenciesManager.recreate_engine_for_agency(agency)

# Create necessary tables in the agency's database
agenciesManager.create_table(engine)