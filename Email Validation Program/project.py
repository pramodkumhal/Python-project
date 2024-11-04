email = input("Enter Your Email: ")  # e.g. g@g.com or g@g.in
k = 0
j = 0
d = 0

if len(email) >= 6:  # 1. Minimum length should be exact 6 eg. g@g.in
    if email[0].isalpha():  # 2. First character should be alphabet
        if ("@" in email) and (email.count("@") == 1):  # 3. Exactly one '@'
            if (email[-3] == ".") ^ (email[-4] == "."):  # 4. Check the dot position 
                for i in email:
                    if i.isspace():  # 5. No spaces allowed
                        k = 1
                    elif i.isalpha():  #Check if it's a letter
                        if i.isupper():  # 5. No uppercase letters allowed
                            j = 1
                    elif i.isdigit():  # Digits are allowed
                        continue
                    elif i in "_@.":  # Special characters allowed _ or @ or .
                        continue
                    else:  # Invalid character found
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email (5)")
                else:
                    print("Valid Email address")
            else:
                print("Wrong Email (4)")
        else:
            print("Wrong Email (3)")
    else:
        print("Wrong Email (2)")
else:
    print("Wrong Email (1)")