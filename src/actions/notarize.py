import subprocess
from tkinter import filedialog as fd

def notarize(api_key):
    filename = fd.askopenfilename()
    process = subprocess.run(['cas.exe', '--api-key', api_key, 'n', filename], stdout=subprocess.PIPE, universal_newlines=True)   
    output = process.stdout
    print(output)