from time import sleep
import platform
import uuid
import hashlib
import math
import random
import string
import smtplib
import zlib
import time
import base64
from time import sleep
from random import randint
import datetime
from datetime import *
from datetime import date
print("\nThis program IS caps sensitive\n")
char = []
num = []
def pw_gen(length, alphabet):
    return "".join(random.choice(alphabet) for i in range(length))
account = input("Do you already have an account? [y/n] ")
while True:
    if account == ("y"):
        username = input("What is your username? ")
        newFile = open('Random_Passwords.js')
        nameFound = False
        while not nameFound:
            if username in newFile.readline():
                nameFound = True
                lineWithPassword = newFile.readline()
                pWPW = input("\nWhat is your password? ")
                encode = pWPW.encode('utf-8')
                hash_object = hashlib.sha512(encode)
                hex_dig = hash_object.hexdigest()
                LZ2 = hex_dig
                realPassword = lineWithPassword.replace("Password: ", "")
                realPassword = realPassword.replace("\n", "")
                if realPassword == LZ2:
                    print("Correct Entry!")
                    menawk = True
                    while menawk == True:
                        choice = input("Press 'v' to view current calendar, press 'a' to add assignments to the calendar ")
                        if choice == "v":
                            currentDT = datetime.now()
                            print("\nToday is",currentDT.strftime("%m-%d-%y"),"\n")
                            import calendar
                            c = calendar.TextCalendar(calendar.SUNDAY)
                            str = c.formatmonth(int(currentDT.strftime("%Y")),int(currentDT.strftime("%m")))
                            print(str+"\n")
                            checkDate = input("What day would you like to see? [yyyy-m-d] ")
                            testTheWaters = open(username+"Calendar"+checkDate+".txt","a+")
                            testTheWaters.close()
                            calendar = open(username+"Calendar"+checkDate+".txt")
                            calendar2 = open(username+"Calendar"+checkDate+".txt","r+")
                            calendar3 = open(username+"Calendar"+checkDate+".txt","r+")
                            count = len(calendar.readlines())
                            count /= 2
                            length = int(count)
                            r = []
                            while count > 0:
                                read = calendar2.readline()
                                read = read.rstrip()
                                readVal = calendar2.readline()
                                readVal = readVal.rstrip()

                                
                                import string
                                class Del:
                                  def __init__(self, keep=string.digits):
                                    self.comp = dict((ord(c),c) for c in keep)
                                  def __getitem__(self, k):
                                    return self.comp.get(k)

                                DD = Del()
                                num.append(int(read.translate(DD)))
                                
                                r.append((readVal, read))
                                count -=1
                            r.sort(reverse=True, key=lambda x: x[0])
                            res_list = [x[1] for x in r]                   
                            readCal = '\n'.join(res_list)
                            if readCal == []:
                                print("\nYou have no events scheduled!\n")
                            else:
                                hour = 0
                                minute = 0
                                tSum = sum(num)/10
                                print("\n")
                                print(readCal,"\n")
                                print("For a total of:",tSum,"minutes of work today")
                                hour = math.floor(tSum/60)
                                minute = tSum % 60
                                print("AKA",hour,"Hours and",minute,"Minutes\n\n")
                                num = []
                        elif choice == "a":
                            title = input("What is the name of the assignment? ")
                            dueYear = int(input("What year is this assignment due? "))
                            dueMonth = int(input("What month is this assignment due? "))
                            dueDay = int(input("What day is this assignment due? "))
                            dueDate = date(dueYear,dueMonth,dueDay)
                            today = date.today()
                            totalDate = str(dueYear)+"-"+str(dueMonth)+"-"+str(dueDay)
                            totalDate = totalDate.replace(" ","")
                            diff = dueDate - today
                            estimatedLength = float(input("How long will this take? (Estimation in minutes) "))
                            eventType = input("Is this: homework [h], project [p] ")
                            if eventType == "h":
                                def sigmoid(x):
                                    return 1/ (1+(math.e)**(4+-.1*x))
                                sig = (sigmoid(int(estimatedLength)/int(diff.days)))*10
                            elif eventType == "p":
                                def sigmoid(x):
                                    return 1/ (1+(math.e)**(4+-.1*x))
                                sig = (sigmoid(int(estimatedLength)/int(diff.days)))*10 + 5
                            cal = open(username+"Calendar"+totalDate+".txt","a+")
                            cal.write(title+"-"+str(estimatedLength)+" minutes\n"+str(sig)+"\n")
                            cal.close()
                            
                                
    elif account == ("n"):
        username = input("What will be your username? ")
        new_file = open("Random_Passwords.js")
        if username in new_file.read():
            print("\nUsername already in use! Try a new one\n")
            account == "n"
        else:
            newPw = input("Would you like to create a custom password [c], or have the computer generate a random password [g]? ")
            if newPw == "c":
                LZ = input("What will the password be? ")
                encode = LZ.encode('utf-8')
                hash_object = hashlib.sha512(encode)
                hex_dig = hash_object.hexdigest()
                LZ2 = hex_dig
                text_file = open("Random_Passwords.js", "a")
                text_file.write("\n")
                text_file.write("Username:" + " " + username + " " + " " + "\n" + "Password:" + " " + LZ2 + "\n" + "\n")
                text_file.close()
                print("\n")
                print("Your password is: " + LZ)
                print("\n")
            elif newPw == "g":
                pw_len = int(input("How many characters should the password have? "))
                incl_upper_alpha = input("Include upper alpha (A-Z) [Y/n]? ")
                incl_lower_alpha = input("Include lowercase (a-z) [Y/n}? ")
                incl_digits = input("Include digits [Y/n]? ")
                incl_special = input("Include special characters [Y/n]? ")
                chars = list(char)
                if incl_upper_alpha.lower() in ["", "y"]:
                    chars += string.ascii_uppercase
                if incl_digits.lower() in ["", "y"]:
                    chars += string.digits
                if incl_special.lower() == "y":
                    chars += string.punctuation
                if incl_lower_alpha.lower() in ["", "y"]:
                    chars += string.ascii_lowercase
                if len(chars) > 0:
                    LZ = (pw_gen(pw_len, chars))
                    encode = LZ.encode('utf-8')
                    hash_object = hashlib.sha512(encode)
                    hex_dig = hash_object.hexdigest()
                    LZ2 = hex_dig
                    text_file = open("Random_Passwords.js", "a")
                    text_file.write("\n")
                    text_file.write("Username:" + " " + username + " " + " " + "\n" + "Password:" + " " + LZ2 + "\n" + "\n")
                    text_file.close()
                    print("\n")
                    print("Your password is: " + LZ)
                    print("\n")
                else:
                    exit()
                    sleep(1)
            else:
                newPw = "g"
            account = "y"
    
