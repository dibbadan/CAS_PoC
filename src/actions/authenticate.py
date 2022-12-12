import subprocess
from tkinter import filedialog as fd

def authenticate(api_key):
    filename = fd.askopenfilename()
    process = subprocess.run(['cas.exe', '--api-key', api_key, 'a', filename], stdout=subprocess.PIPE, universal_newlines=True)   
    if process.returncode == 0:
        output = process.stdout
        print(output)
        return
    return -1
