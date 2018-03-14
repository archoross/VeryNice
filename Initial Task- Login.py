# @archoross on Github

def createAccount():
    global name
    name = str(input("What is your first name: "))
    global email
    email = str(input("What is your email adress: "))
    global password
    password = str(input("Create a password: "))  
    repassword = str(input("Confirm your password: "))
    if password == repassword:
        print ("\nThank you for registering", name)
    if password != repassword:
        print ("Passwords did not match. Please refill everything")
        createAccount()
 
 
def login(attempts):
    tryEmail = str(input("\nEnter your email adress: "))
    tryPassword = str(input("Please enter your password: "))
    global password
    if tryPassword == password and email == tryEmail:
        print ("You are logged in,", name)
        change = str(input("Input 1 to change your password or 0 to do nothing: "))
        if change == "1":
            password = str(input("Please enter your new password: "))
    elif attempts == 2:
        print ("You ran out of attempts!")
    elif tryPassword != password or email != tryEmail:
        print ("Email does not matched password try again!")
        attempts = attempts + 1
        login(attempts)
    
        
createAccount()
useless = (input("Press enter to login!\n"))
login(0)

