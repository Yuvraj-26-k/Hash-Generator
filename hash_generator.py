import hashlib
from datetime import datetime
import os
import time

# ----------------------------+
# Hash Generation Function    |
# ----------------------------+

def generate_hash(algorithm):

    text = input("[#] Enter Text : ")

    if algorithm == "MD5":
        hash_value = hashlib.md5(text.encode()).hexdigest()

    elif algorithm == "SHA1":
        hash_value = hashlib.sha1(text.encode()).hexdigest()

    elif algorithm == "SHA224":
        hash_value = hashlib.sha224(text.encode()).hexdigest()

    elif algorithm == "SHA256":
        hash_value = hashlib.sha256(text.encode()).hexdigest()

    elif algorithm == "SHA384":
        hash_value = hashlib.sha384(text.encode()).hexdigest()

    elif algorithm == "SHA512":
        hash_value = hashlib.sha512(text.encode()).hexdigest()
    print(f"{purple}[#] Generating {algorithm} Hash{reset}")

    full="█"
    empty="░"

    for i in range(11):
        percent=i*10
        print(f"\r{purple}{full*i}{empty*(10-i)} {percent}%{reset}",end="",flush=True)
        time.sleep(0.1)

    print()
    print(f"{green}[/] Hash Generated Successfully!{reset}")


    return text, hash_value, algorithm


# ----------------------------
# Report Function
# ----------------------------
def report(text, hash_value, algorithm):

    current = datetime.now()
    
    for i in range(40):
        print("=", end="", flush=True)
        time.sleep(0.01)
    print()
    
    letter="Generated report".upper().center(40)
    
    for l in letter:
        print(l, end="", flush=True)
        time.sleep(0.01)
    print()
    
    for i in range(40):
        print("=", end="", flush=True)
        time.sleep(0.01)
    print()
    
    report = (f"""
{'='*40}
Original Text : {text}         \n
Hash Length   : {len(hash_value)} Characters \n
Algorithm : {algorithm}
Generated Hash: \n
{hash_value}    \n

Date : {current.strftime('%d-%m-%Y')}
Time : {current.strftime('%H:%M:%S')}
{'='*40}
""")
    
    print(report)


# ----------------------------
# Main Program
# ----------------------------

red="\033[91m"
green="\033[92m"
yellow="\033[93m"
blue="\033[94m"
purple="\033[95m"
reset="\033[0m"

while True:

    for i in range(40):
       print(yellow + '=' + reset, end="", flush=True)
       time.sleep(0.02)
    print()
    
    letter="Hash generator".upper().center(40)
    
    for l in letter:
        print(blue + l + reset, end="", flush=True)
        time.sleep(0.01)
    print()
  
    for i in range(40):
        print(yellow + '=' + reset, end="", flush=True)
        time.sleep(0.01)
        
    menu = (f"""
[1] MD5
[2] SHA1 
[3] SHA224
[4] SHA256
[5] SHA384
[6] SHA512
[7] Exit
""")
    
    print(menu)

    try:
        choice = int(input(yellow + "[</>] Enter Choice : " + reset))
    except ValueError:
        print(yellow + "[!] Enter numbers only!" + reset)
        continue

    if choice == 7:
        print(green + "[$] Thank you!" + reset)
        break

    if choice == 1:
        result = generate_hash("MD5")

    elif choice == 2:
        result = generate_hash("SHA1")

    elif choice == 3:
        result = generate_hash("SHA224")

    elif choice == 4:
        result = generate_hash("SHA256")

    elif choice == 5:
        result = generate_hash("SHA384")

    elif choice == 6:
        result = generate_hash("SHA512")

    else:
        print(red + "[!] Invalid Choice!" + reset)
        continue

    text, hash_value, algorithm = result

    report(text, hash_value, algorithm)

    save = input(green + "\n[!] Save Report? (Y/N): " + reset).upper()

    if save == "Y":

        filename = input(blue + "[#] File Name : " + reset)

        if not filename.endswith(".txt"):
            filename += ".txt"

        with open(filename, "w") as file:

            file.write(f"""
            Original Text : {text}
            Algorithm : {algorithm}

            Generated Hash : {hash_value}

            Date : {datetime.now().strftime("%d-%m-%Y")}
            Time : {datetime.now().strftime("%H:%M:%S")}
                                                        """)

        print(green + "[/] Report Saved Successfully!" + reset)
        location = os.path.abspath(filename)

        print(f"{blue}[$] Location : {location}{reset}")
    
    elif save == "N":
        print(blue + "[#] Exiting".upper() + reset, end="", flush=True)
        for i in range(7):
            print(blue + "." + reset, end="", flush=True)
            time.sleep(0.1)
        print()
        break
        
    else:
        print(f"{red}[!] Enter only Y or N!{reset}")
        continue
        