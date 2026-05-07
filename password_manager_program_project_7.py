# Password Manager Program

import random # random module random password generate karne ke liye use hota hai
import string # string module letters aur digits lene ke liye use hota hai

passwords = {}

#load exiting password file
try:
    with open("passwords.txt","r") as file:  # passwords.txt file read mode me open ho rahi hai
        for lien in file:    # file ki har line ko read karega
            website,pwd = line.strip().split(":")
        
            # line ko ":" ke basis par split karega
            # Example:
            # google:1234
            # website = google
            # pwd = 1234
    
            passwords[website] = pwd

except: # Agar file exist nahi karti to error ignore karega
    pass


# Password generate karne ka function
def generate_password(): 
    chars = string.ascii_letters+ string.digits + "#%^@!*" # Password me use hone wale characters
    password = "".join(random.choice(chars) for _ in range(8))
    return password
sumary_line
while True:
    print("\n --  PERSONAL PASSWORD MANAGER ---")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice : ")

    # Save Password
    if choice =="1":
        site = input("Enter Website : ")
        pwd = input("Enter Psssword : ")

        passwords[site] =pwd

        with open("password.txt","a") as file:
            file.write(f"{site}:{pwd}\n")

            print("Saved!")


    #View Password
    elif choice =="2":
        if not passwords:
            print("No Data")

        else:
            for site,pwd in passwords.items():    # Dictionary ke saare website aur password print honge
                print(site, ":",pwd)

    
    # Generate Password
    elif choice == "3":
        print("Generate Password", generate_password())

    
    # Exit
    elif choice =="4":
        print("Ok Bye...")
        break

    else:
        print("In-Valid Input!")


