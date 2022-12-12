import subprocess
import base64
from tkinter import filedialog as fd

def select_artifact_and_inspect(api_key):
    filename = fd.askopenfilename()
    process = subprocess.run(['cas.exe', '--api-key', api_key, 'inspect', filename], check=True, stdout=subprocess.PIPE, universal_newlines=True)   
    output = process.stdout
    encoded_signerID = output[727:output.index("Apikey")]
    if encoded_signerID != '':
        signerID = base64.b64decode(encoded_signerID).decode()
        print("\nLast notarization performed by signerID: ", signerID)
    print(output)