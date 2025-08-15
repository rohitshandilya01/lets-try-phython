"""
1st lenght must be more than 6 charcter
2nd first character must be alphabet
3rd @ is present only one time
4th email ke end me 3rd or 4th position pe . hona chahiye
5th 

"""



email = input(str("Enter Your Mail : ")) #minimun f@gmail.com

j,k,d=0,0,0
if len(email)>=6:
    if email[0].isalpha(): #isalpha is used to check it is alphabet or not
        
        if ("@" in email) and (email.count("@")==1):
             if (email[-4] == ".") ^ (email[-3]=="."):
                for i in email:
                    if i ==i.isspace():
                        K=1
                    elif i ==i.isalpha():
                        if i==i.upper():
                           j=1

                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="." or i=="@":
                        continue
                       
                    else:
                         d=1
                        

                if k==1 or j==1 or d==1:
                    print("invalid invalid")
             else:
                 print("Invalid due to . place is wrong")
          
        else:
            print("Invalid Email due to @ problem")

       
    else:
        print("Invaild Email first letter is not alphabet")
else:
    print("Invalid Email length")


print(f"Correct {email}")