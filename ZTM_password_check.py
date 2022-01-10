username=input("Enter username")
password=input("enter password")
password_hidden=len(password)
print(f"hie! Your username is {username} and your password is {'*'* password_hidden}")