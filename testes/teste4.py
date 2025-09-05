from db_works import accountManagement
from db_works import peopleManagement
from db_works import agenciesManager

agency = agenciesManager.retrieve_agency_info("nome1")

engine = agenciesManager.recreate_engine_for_agency(agency)

pessoa = peopleManagement.get_people_by_name("James", engine)

account = accountManagement.create_account(2332, 1000.0, "securepassword")
accountManagement.add_account_to_db(account, pessoa, engine)