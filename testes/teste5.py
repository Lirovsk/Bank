from db_works import agenciesManager
from db_works import accountManagement


agency = agenciesManager.retrieve_agency_info("nome1")
engine = agenciesManager.recreate_engine_for_agency(agency)

# Retrieve accounts owned by the person with ID 1
accounts = accountManagement.filter_accounts_by_owner(1, engine)

for account in accounts:
    print(account.numero)

    
    