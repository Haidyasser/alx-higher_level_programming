#find last id in file
def lastId():
    l = 0
    with open("project1.txt", "r+") as file:
        for line in file:
            l = line.split()[0]
    return int(l)

# writing a record to a file
def writeToFile():
    ch = 'y'
    with open("project1.txt", 'a') as file:
        Id = str(lastId() + 1)
        name = input("enter your name : ")
        age = input("enter age :  ")
        balance = input("Enter the amount of your balance : ")
        while int(balance) < 500 :
            print("Sorry you can't create an account :( \n Your balance can't be less than <<500>> \n Put another maount  .... )")
            balance = input("Enter the amount of your balance : ")
        file.write(Id + '\t' + name + '\t' + age + '\t' +balance+'\n')
        print("Record added sucessfully  :) ")
#--------------------------------------------------------------------------- 
#read all data from a file
def readFromFile():
    flag = False
    try:
        with open("project1.txt", "r") as file:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("ID\tName\tAge\tBalance")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for line in file:
                flag = True
                print(line, end="")
                print("--------------------------------")
    except:
        print("File not found")
    if flag == False:
        print("No data found")     
#---------------------------------------------------------------------------                
#Update a record
def UpdateToFile():
    import os
    flag = False
    tmp = open("tmp.txt", "w")
    with open("project1.txt", "r") as file:
        Id = input("Enter your id : ")
        for line in file:
            if line.startswith(Id):
                print("Your Data :")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("ID\tName\tAge\tBalance")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(line, end="")
                print("----------------------------------------")

                ch = input("Do you want to update your name ? y/n ")
                if ch == 'y':
                    name = input("Enter your new name : ")
                    flag = True
                else:
                    name = line.split()[1]
                ch = input("Do you want to update your age ? y/n ")
                if ch == 'y':
                    age = input("Enter your new age : ")
                    flag = True
                else:
                    age = line.split()[2]
                l = line.split()
                l[1] = name
                l[2] = age
                
                tmp.write(l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + l[3] + '\n' )
            else:
                tmp.write(line)
    tmp.close()
    os.remove("project1.txt")
    os.rename("tmp.txt", "project1.txt")
    if flag == False:
        print("There is no data for this id")
    else:
        print("your data updated successfully ")
#--------------------------------------------------------------------------- 
#delete a record 
def DeleteRecordFromFile():
    import os
    id = input("Enter id for deleteing ")
    file = open("project1.txt",'r')
    tempFile = open("temp.txt",'w')
    flag = False
    for line in file:
        l = line.split('\t')
        if id != l[0]:
            tempFile.write(line)
        else:
            flag = True
    file.close()
    tempFile.close()
    os.remove("project1.txt")
    os.rename("temp.txt","project1.txt")
    if not flag:
        print("record does not exit in the file!!!")
    else:
        print("record was deleted successfully!!")
#--------------------------------------------------------------------------- 
# search and show specific record --> by name 
def search():
    name=input("Enter the name of Customer:\n")
    with open ("project1.txt","r")as f:
        flag=False
        for line in f:
            st=line.split("\t")
            if st[1]==name:
                flag=True
                print("ID     :",st[0])
                print("Name   :",st[1])
                print("Age    :",st[2])
                print("Balance:",st[3])
        if not flag:
            print("Account not found!\n")
#--------------------------------------------------------------------------
def dep(id,amt):
    
    import os
    flag = False
    tmp = open("tmp.txt", "w")
    with open("project1.txt", "r") as file:
        for line in file:
            l = line.split('\t')
            
            
            if id == l[0]:
                flag = True
               
                l[3] = int(l[3]) + int(amt)
                tmp.write(l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + str(l[3]) + '\n')
                print("Your Balance updated successfully ")

            else:
                tmp.write(line)
                      
    tmp.close()
    os.remove("project1.txt")
    os.rename("tmp.txt", "project1.txt")
    
    if flag == False:
        print("Your id not found")
    else:
        print("your Balance updated successfully ")
#---------------------------------------------------------------------------
def withdraw(id):
    import os
    flag = False
    tmp = open("tmp.txt", "w")
    with open("project1.txt", "r") as file:
        for line in file:
            l = line.split('\t')
            
            
            if id == l[0]:
                while flag == False :
                    print("---------------------------------------")
                    amt = input(" Enter amount to be Withdrawed :  \n")
                    
                    if (int(l[3]) - int(amt) < 500 ) :
                        print("Sorry you can't withdraw this amount :( \n Your balance can't be less than <<500>> \n Put another maount  .... )")
                    else :
                        flag = True
                        l[3] = int(l[3]) - int(amt)
                        tmp.write(l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + str(l[3]) + '\n')
                        print("Your Balance updated successfully ")

            else:
                tmp.write(line)
                      
    tmp.close()
    os.remove("project1.txt")
    os.rename("tmp.txt", "project1.txt")
    
    if flag == False:
        print("Your id not found")
    else:
        print("your Balance updated successfully ")
#---------------------------------------------------------------------------
def deposit_withdraw(op):
    search()
    id = input("Enter ID : ")
    if (op == 1 ):
        print("---------------------------------------")
        amt=input(" Enter amount to be deposited  : ")
        dep(id, amt )
 
    if (op == 2 ):
        withdraw( id )            
#--------------------------------------------------------------------------- 
# main function            
def main():
        c='y'
        while(c=='y'):
            print("---------------------------------------------------------")
            print("|              H  e   l   l   o    In                   |")
            print("|          Bank      Mangement      System              |")
            print("---------------------------------------------------------")
            print("\n")
            print("******************  MAIN  MENU  ******************")
            print("            -----------------------------")
            print("            | 1 | Create  Account       |")
            print("            -----------------------------")
            print("            | 2 | Deposite              |")
            print("            -----------------------------")
            print("            | 3 | Withdraw              |")
            print("            -----------------------------")
            print("            | 4 | Show Your Acount      |") #search
            print("            -----------------------------")
            print("            | 5 | Delete Your Acount    |")
            print("            -----------------------------")
            print("            | 6 | Update Your Account   |")
            print("            -----------------------------")
            print("            | 7 | Show all Accounts     |")
            print("            -----------------------------")
            
            L = [writeToFile,deposit_withdraw,deposit_withdraw,search,DeleteRecordFromFile,UpdateToFile,readFromFile]
            op=input("\nEnter Number Of Transaction You Want: ") 
            try:
                op = int(op)
                L[op - 1]()
            except:
                print("Invalid input")
                    
            c=input("\nDo you want to continue?y/n.\n")
            if c=='n':
                print("Thank you for using our system :)")
main()