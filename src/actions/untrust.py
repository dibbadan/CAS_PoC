import subprocess
from tkinter import filedialog as fd

def untrust_asset(api_key):
    filename = fd.askopenfilename()
    process = subprocess.run(['cas.exe', '--api-key', api_key, 'untrust', filename], stdout=subprocess.PIPE, universal_newlines=True)   
    output = process.stdout
    print(output)