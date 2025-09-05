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
    agency = agencyStorageCreation(eval(f"name{i+1}"), eval(f"version{i+1}"),senha="1234")
    url = agency.create_agency_url()
    agency.storage_agency_info()
    print(url)

