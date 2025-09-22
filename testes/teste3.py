from db_works import peopleManagement
from db_works import agenciesManager

agency = agenciesManager.retrieve_agency_info("nome1")

engine = agenciesManager.recreate_engine_for_agency(agency)

# creatwe a new person and add to the database
people = peopleManagement.create_people("James", 30, "james@example.com", "istoe")
peopleManagement.add_person_to_db(people, engine)


