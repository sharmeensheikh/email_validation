email=input("Enter you Email: ")
k = 0
j = 0
l = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-3] == ".") ^ (email[-4] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        l = 1
                if k == 1:
                    print("Whitespace not Allowed!")
                elif j == 1:
                    print("Uppercase not Allowed!")
                elif l == 1:
                    print("Special character not allowed!")
                else:
                    print("Accepted!")
            else:
                print("Invalid Email 2")
        else:
            print("Invalid Email 1.")
    else:
        print("First character is not alphabet")
else:
    print("Email cannot be less then 6 character.")