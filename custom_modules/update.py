'''
All the updation functions for code
'''

import csv
import time

def update(id,a):

    # open the csv file as read mode 
    f=open("emp_details.csv",'r')

    # set the found veriable for 0
    found=0


    csvr=csv.reader(f)

    # we create an empty list
    ml=[]
    for r in csvr:
        if(r[0]==id):
            if a==1:
                r[1]=input("Enter the new name of the Employee  :")
            if a==2:
                r[2]=input("Enter the new designation of the Employee  :")
            if a==3:
                r[3]=input("Enter the new salary of the Employee  :")
            if a==4:
                r[4]=input("Enter the new age of the Employee  :")
            if a==5:
                r[6]=input("Enter the new Email id of the Employee  :")
            if a==6:
                r[7]=input("Enter the new Phone no. of the Employee  :")

            found=1

        # we append all the updated row in the list
        ml.append(r)


    if found==0:
        print("No data Found!!!!")

    else:

        # here we open the csv file in write mode
        f=open("emp_details.csv","w",newline="")
        csvr=csv.writer(f)

        # write all the rows
        csvr.writerows(ml)

        # close the 
        f.close()



# ************************* Main function **************************************

def update_data():

    # Enter the id of the columns whose data you want to update
    id=input("Enter the ID of the Employee : ")



    while 1:

        print("1. Update Name ")
        print("2. Update Designation")
        print("3. Update Salary")
        print("4. Update Age")
        print("5. Update Email")
        print("6. Update Phone No. ")

        # enter the choice we want to update 
        a=int(input("Enter your choice :  "))

        # here we give the EMp_id and the choice to the update function 
        update(id,a)

        # if you want to update other columns then enter y and if you don't want to update other things then enter n
        x=input("Do you want update anything (y/n) : ")


        if x=='y':
            pass

        if x=='n':
            break

    #end of updation 
    print("\n\nData has been updated successfully!")
    time.sleep(2)
