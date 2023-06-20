import subprocess
import re
import pywifi
from pywifi import const

def retrieve_wifi_passwords():
    try:
        command = "netsh wlan show profile name=* key=clear"
        output = subprocess.check_output(command, shell=True, encoding="utf-8")
        
        passwords = re.findall(r"Key Content\s+:\s(.+)", output)

        return passwords

    except subprocess.CalledProcessError:
        return "Failed to retrieve Wi-Fi passwords."


wifi_passwords = retrieve_wifi_passwords()
print("Wi-Fi Passwords:")
for wifi_password in wifi_passwords:
        print(wifi_password)