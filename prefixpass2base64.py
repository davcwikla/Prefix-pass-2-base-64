import base64
import time

logo = """
______          __ _     ______              _____ ______                 ____    ___ 
| ___ \        / _(_)    | ___ \            / __  \| ___ \               / ___|  /   |
| |_/ / __ ___| |_ ___  _| |_/ /_ _ ___ ___ `' / /'| |_/ / __ _ ___  ___/ /___  / /| |
|  __/ '__/ _ \  _| \ \/ /  __/ _` / __/ __|  / /  | ___ \/ _` / __|/ _ \ ___ \/ /_| |
| |  | | |  __/ | | |>  <| | | (_| \__ \__ \./ /___| |_/ / (_| \__ \  __/ \_/ |\___  |
\_|  |_|  \___|_| |_/_/\_\_|  \__,_|___/___/\_____/\____/ \__,_|___/\___\_____/    |_/

Author: d4xc
Site: SOON
"""

print(logo)

pass_file = input("Set path for passwords file: ")

prefix = input("Set prefix for passwords: ")

animation = "|/-\\"
for i in range(20):
    time.sleep(0.1)
    print(f"Generating... {animation[i % len(animation)]}", end="\r")

print("\n")

try:
    with open(pass_file, 'r') as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print("Files dont exist.")
    exit()

passwords_with_prefix = [prefix + password for password in passwords]

encoded_passwords = [base64.b64encode(password.encode('utf-8')).decode('utf-8') for password in passwords_with_prefix]

with open('output.txt', 'w') as file:
    for encoded_password in encoded_passwords:
        file.write(encoded_password + '\n')

print("Encoding to Base64 is done. All is saved in file called output.txt")
