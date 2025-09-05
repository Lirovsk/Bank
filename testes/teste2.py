from db_works import agenciesManager

agencies = agenciesManager.retrieve_agencies_info()
for agency in agencies:
    print(agency.name)
    
name = input("chose an agency: ")
agency = agenciesManager.retrieve_agency_info(name)

engine = agenciesManager.recreate_engine_for_agency(agency)

agenciesManager.create_table(engine)