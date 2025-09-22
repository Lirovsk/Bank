from db_works import(agenciesManager,
                     agencyStorageCreation,
                     peopleManagement,
                     operations,
                     accountManagement)
import os
from time import sleep

MENU1 = """
1- create agency
2- access agency
0- exit
"""

MENU2 = """
1- create personal account
2- access personal account
0- back to main menu
"""

MENU3 = """
1- create bank account
2- access bank account
0- back to previous menu
"""

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


while True:
    clear()
    print("Welcome to the Bank System")
    print(MENU1)
    option = input("Select an option: ")
    match option:
        case '1':
            clear()
            agency_name = input("Enter the agency name: ")
            agency_version = input("Enter the database version (e.g., sqlite, postgresql): ")
            agency_password = input("Set a password for the agency: ")
            agency = agencyStorageCreation(agency_name, agency_version, senha=agency_password)
            agency.storage_agency_info()
            clear()
            print(f"Agency '{agency_name}' created successfully!")
            print("going back to main menu...")
            sleep(2)
            
        case '2':
            clear()
            agencies = agenciesManager.retrieve_agencies_info()
            for agency in agencies:
                print(agency.name)
            
            choosen_agency = input("Choose an agency: ")
            agency = agenciesManager.retrieve_agency_info(choosen_agency)
            if not agency:
                print("Agency not found. Returning to main menu...")
                sleep(2)
                continue
            
            engine = agenciesManager.recreate_engine_for_agency(agency)
            agenciesManager.create_table(engine)
            print(f"Accessing agency: {agency.name}")
            sleep(1)
            clear()
            
            while True:
                print(MENU2)
                option2 = input("Select an option: ")
                match option2:
                    case '1':
                        clear()
                        name = input("Enter your name: ")
                        age = int(input("Enter your age: "))
                        email = input("Enter your email: ")
                        password = input("Set a password for your account: ")
                        person = peopleManagement.create_people(name, age, email, password)
                        peopleManagement.add_person_to_db(person, engine)
                        clear()
                        print(f"Personal account for '{name}' created successfully!")
                        print("Returning to previous menu...")
                        sleep(2)
                        clear()
                        
                    case '2':
                        clear()
                        name = input("Enter your name: ")
                        password = input("Enter your password: ")
                        person = peopleManagement.get_people_by_name(name, engine, password)
                        if not person:
                            print("Invalid credentials. Returning to previous menu...")
                            sleep(2)
                            clear()
                            continue
                        
                        clear()
                        print(f"Welcome {person.nome}!")
                        print(MENU3)
                        option3 = input("Select an option: ")
                        match option3:
                            case '1':
                                # Create bank account
                                account_number = input("Enter account number: ")
                                initial_balance = float(input("Enter initial balance: "))
                                password = input("Set a password for the bank account: ")
                                account = accountManagement.create_account(account_number, initial_balance, password)
                                accountManagement.add_account_to_db(account, person, engine)
                                clear()
                                print("Account created successfully!")
                                
                            case '2':
                                # Access bank account
                                accounts = accountManagement.get_all_accounts(person.id, engine)
                                
                                for account in accounts:
                                    print(f"Account Number: {account.numero}, Balance: {account.saldo}")
                                    
                                account_number = input("Enter account number: ")
                                clear()
                                
                                while True:
                                    clear()
                                    print("Which operation do you want to do?")
                                    input_operation = input("1 - Withdraw\n2 - Deposit\n3 - Get history of transactions\n0 - Back to previous menu\n")
                                    
                                    match input_operation:
                                        case '1':
                                            amount = float(input("Enter the amount to withdraw: "))
                                            password_ = input("Enter your password: ")
                                            operations.withdraw(account_number, amount, password_, engine)
                                            oia = input("Press Enter to continue...")
                                        
                                        case '2':
                                            amount = float(input("Enter the amount to deposit: "))
                                            password_ = input("Enter your password: ")
                                            operations.deposit(account_number, amount, password_, engine)
                                            oia = input("Press Enter to continue...")
                                        
                                        case '3':
                                            # Get and display transaction history
                                            operations.get_history(account_number)
                                            oia = input("Press Enter to continue...")
                                        
                                        case '0':
                                            clear()
                                            break
                                        
                                        case _:
                                            print("Invalid operation selected. Please try again.")
                                            clear()
                        sleep(1)
                        clear()
                        
                    case '0':
                        clear()
                        break
                                    
                    case _:
                        print("Invalid option. Returning to main menu...")
                        sleep(2)
            
        
        case '0':
            print("Exiting the system. Goodbye!")
            break