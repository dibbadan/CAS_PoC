from actions.login_to_cas import login_to_CAS_Service
from actions.notarize import notarize
from actions.authenticate import authenticate
from actions.inspect import select_artifact_and_inspect
from actions.untrust import untrust_asset

menu_options = {
    1: 'Login',
    2: 'Notarize',
    3: 'Authenticate',
    4: 'Inspect',
    5: 'Untrust',
    6: 'Exit',
}



def show_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    print("\n")


def menu():
    api_key = ''    
    while(True):
        show_menu()
        
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please, enter a valid number ...')

        if option == 1:
            api_key = login_to_CAS_Service()
        elif option == 2:
            if api_key == -1 or api_key == '':
                print("You need to login first!\n")
                continue
            notarize(api_key)
        elif option == 3:
            if api_key == -1 or api_key == '':
                print("You need to login first!\n")
                continue
            if authenticate(api_key) == -1:
                print("Auth gone wrong!\n")
                continue
            continue
        elif option == 4:
            if api_key == -1 or api_key == '':
                print("You need to login first!\n")
                continue
            select_artifact_and_inspect(api_key)
        elif option == 5:
            if api_key == -1 or api_key == '':
                print("You need to login first!\n")
                continue
            untrust_asset(api_key)
        elif option == 6:
            exit(0)
        else:
            print('Invalid option. Please enter a number between 1 and 5\n')