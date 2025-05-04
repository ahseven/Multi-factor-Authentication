import pyotp, qrcode, time
import pandas as pd
from hashlib import sha256

database = pd.read_csv(r"D:\Coding\Python Fundemental\project\database.csv") # Importing the data from a CSV file (Acting database)

def signup(username, password):

    secret_key = pyotp.random_base32() # Generate a random secret key for the user

    # Create a new row for the user in the database
    new_row = {
    "Username": f"{username}",
    "Password": f"{password}",
    "Secret Key(Base32)": f"{secret_key}" }

    database.loc[len(database)] = new_row # Add the new row to the Database (CSV file)
    database.to_csv(r"D:\Coding\Python Fundemental\project\database.csv", index=False) # Save the new row to the CSV file (Database)
    
    totp = pyotp.TOTP(secret_key) # Activate Time-based OTP

    auth_usr = totp.provisioning_uri(name = username, issuer_name="SKME APP") # Convert Time based OTP into a link

    img = qrcode.make(auth_usr) # convert That OTP link into a scannable QRCode for MFA using Google Authenticator

    # Print out the QR code for the user to scan
    print("\nCaution! Scan this QR code in Google Authenticator for Multifactor Authentication when signing into this account.\nThis QR Code will only be generated once when first signing up!")
    print("Save this QR code in a safe place, as it will not be generated again!")

    # Count down to generate a QR Code
    counter = 5
    for i in range(5):
        time.sleep(1)
        print(f"\nGenerating QR Code in {counter}....")
        counter -= 1
    time.sleep(1)
    print("\nQR Code generated!\n")
    
    img.show() # Show the QR code to the user
    return f"Signup successfully!\n"

def login(username, password):
        
        database['Password'] = database['Password'].astype(str) # Convert the Password column to string type for comparison

        # Check if the username and password are correct
        if not ((database['Username'] == f"{username}") & (database['Password'] == f"{password}")).any(): 
            return ("Username or Password is incorrect!")
        
        # Get the secret key for the user's account
        key = database[database["Username"] == f'{username}']
        key = key['Secret Key(Base32)'].values[0]

        # Calculate the 6 digits code through secret key
        totp = pyotp.TOTP(key) 
         
        text = 'Multifactor Authentication Needed!'
        print(f"\n{text.center(45, '-')}") # for aesthetic purposes

        OTP = input("Enter your verification code from Google Authenthicator: ").strip()

        # Verification
        if totp.verify(OTP):
            return f"\nLogin Successfully, Welcome {username}!\n"
        else:
            return "\nVerification failed.\n"

def hash_password(password):
    """Hash the password using SHA-256."""
    return sha256(password.encode()).hexdigest()

def main():

    while True:
        a = "SKME APP" # for aesthetic purposes
        print(f"\n{a.center(20, '-')}") # for aesthetic purposes
        print("Choose your options:")
        user = input("1. Login\n2. Signup\n3. Quit\nYour Choice: ")

        if user == "1":
            username = input("Enter your username: ") 
            password = input("Enter your password: ")
            password = hash_password(password) # Hash the password using SHA-256
            message = login(username, password)
            if message == "Username or Password is incorrect!" or message == '\nVerification failed.\n':
                print(message)
                continue
            else:
                print(message)
                break # If the login is successful, break out of the loop
            
        elif user == "2":
            while True:
                username = input("Enter your username: ")
                # Check if the username already exists in the database
                available = database['Username'].isin([username])
                if available.any(): # If the username already exists, return an error message
                    print("Username already exists")
                    continue
                break
            password = input("Enter your password: ")
            password = hash_password(password) # Hash the password using SHA-256
            print(signup(username, password))

        elif user == "3":
            print("\nGoodbye!\n")
            break

        elif user == "dev":
            print("\nDeveloper Mode Activated")
            df = database.copy() # Create a copy of the database for display purposes
            # df = df.drop(columns=["Secret Key(Base32)"]) # Drop the secret key column for security reasons
            print(f"Database:\n\n{df}")
        
 # Call the main function to start the program

main()
