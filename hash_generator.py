import hashlib
import time
import os
from datetime import datetime

red="\033[91m"
green="\033[92m"
yellow="\033[93m"
blue="\033[94m"
purple="\033[95m"
reset="\033[0m"
     

while True:
    for i in range(20):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    letters1=  "Hash generator"  .center(20).upper()
    
    for l in letters1:
        print(l, end="" , flush=True)
        time.sleep(0.02)
    print()
    
    for i in range(20):
        print("=", end="", flush=True)
        
    print(yellow + "\n[$] Initializing" + reset, end="", flush=True)
    
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.1)
    print()
    
    print(yellow + "[$] Loading Modules" + reset, end="", flush=True)
    
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.1)
    print()
    
    text=str(input( "Enter Text: \n "))
    hash1=hashlib.sha256(text.encode()).hexdigest()
    leng1=len(hash1)
    current=datetime.now()
    
    
    full="█"
    empty="░"
    
    print("[#] Generating SHA-256 Hash")
        
    for i in range(11):
        percent=i*10
        print(f"\r{full*i}{empty*(10-i)} {percent}%",end="", flush=True)
        time.sleep(0.25)
    print()
    
    print("Hash Generated Successfully!")
    
    for i in range(30):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    letters2="Hash report".upper().center(30)
    
    for l in letters2:
        print(l, end="", flush=True)
        time.sleep(0.2)
    print()
    
    for i in range(30):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    report=f"""
    Original Text : {text} \n
    Algorithm    : SHA-256 \n
    
    Hash Length  : {leng1} Characters \n
    
    Generated Hash : \n {hash1} \n    
    
    Date : {current.strftime("%d-%m-%Y")} \n
    Time : {current.strftime("%H:%M:%S")}
    
    """
    print(report)

    for i in range(30):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    choice=str(input("[$] Do you want to save the report? (Y/N):")).upper()
    if choice == "Y":
        file1=str(input("Enter report file name:"))  
        if not file1.endswith(".txt"):
            file1+=".txt"
    elif choice == "N":
        print("[!] Exiting", end="", flush=True)
        
        for i in range(10):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()
        break
    else:
        print(red + "Enter only Y or N!" + reset)
        continue

    file2=open(file1,"w")
    file2.write(report)
    file2.close()
    
    print("[$] Saving Report",end="",flush=True)
    
    for i in range(11):
        percent=i*10
        print(f"\r{full*i}{empty*(10-i)} {percent}%",end="", flush=True)
        time.sleep(0.25)
    print()
    
    print("[/] Report Saved Successfully!")
    
    path1=os.path.abspath(file1)
    
    print(f"[$] Location : \n{path1}")
    
    for i in range(30):
        print("=", end="", flush=True)
        time.sleep(0.02)
    print()
    
    text1="thank you for using\nHash generator".upper()
    
    for t in text1:
        print(t,end="",flush=True)
        time.sleep(0.1)
    print()
    
    print("[!] Exiting", end="", flush=True)
    
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.1)
    print()
    break
