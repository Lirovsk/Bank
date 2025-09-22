from db_works import agencyStorageCreation

name1 = "nome1"
version1 = "sqlite"

name2 = "nome2"
version2 = "sqlite"

name3 = "nome3"
version3 = "sqlite"

name4 = "nome4"
version4 = "sqlite"

for i in range(4):
    # This line uses eval to access the variables dynamically and save agencies' information in the database
    agency = agencyStorageCreation(eval(f"name{i+1}"), eval(f"version{i+1}"),senha="1234")
    # this line creates the agency URL 
    url = agency.create_agency_url()
    # this line stores the agency information in the main database
    agency.storage_agency_info()
    print(url)

