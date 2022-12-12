import subprocess


def login_to_CAS_Service():
    api_key = input("Enter your api-key: ")
    print("\nLogging to CAS Service ...\n")
    process = subprocess.run(['cas.exe', '--api-key', api_key, 'login'], stdout=subprocess.PIPE, universal_newlines=True)
    if process.returncode == 0:
        output = process.stdout
        print(output+"\n")
        return api_key
    print("Unable to login! Wrong api_key.")
    return -1