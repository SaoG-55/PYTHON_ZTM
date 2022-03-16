import re

pattern_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern_password = re.compile(r"[A-Za-z0-9$%#@]{8,}\d$")
# password
# 8 char long
# contain any sort letters,no.s $%#@
# has to end with a no.
while True:
    str1 = input("enter email:")
    str2 = input("enter password(it has to be 8 or morechar long,special char$%#@,has to end with a no.):\n")
    a = pattern_email.search(str1)
    b = pattern_password.search(str2)
    if (a != None and pattern_password.fullmatch(str2) != None):
        print(f"Your email-id is {pattern_email.findall(str1)}")

        print(f"Sucessfully logged in!")
        break
    elif (a == None):
        print("Enter correct email")
    else:
        print("enter correct password")
