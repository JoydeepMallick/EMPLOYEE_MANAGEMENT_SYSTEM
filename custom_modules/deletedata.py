"""
Writing into the emp_details.csv file stored within main folder

Functions defined below :-

    admin()
    delete_data()
    --------------------------


"""

import csv
import time
import pandas as pd

# user id and password
USERID="BCREC"
PASSWORD='admin'


# ************* THis function is used for user and password verification ******************
def admin():

    '''
        This function "admin()" prompts the user to enter an admin user ID and password. If the user 
        enters the correct user ID and password, the function calls another function called 
        delete_data() to delete a column. If the user enters an incorrect user ID or password, 
        the function prints an error message and decrements a counter for the number of tries 
        remaining. The function repeats this process until either the correct user ID and 
        password are entered or there are no more tries remaining.

    '''
    # there will be 3 trail for password verification
    tries_left=3

    while tries_left:

        # give the user input for userid and password
        userid=input("Enter admin UserID : ")
        user=input("Enter admin password : ")

        # If the user id and password is correct then it will call delete function to delete the Column
        if user==PASSWORD and userid==USERID:
            print("Permission Granted!!!!!")
            time.sleep(1)
            # Here we call the delete_data function.
            delete_data()
            time.sleep(2)
            break

        # the next three if condition for either wrong userid or wrong password

        if user!=PASSWORD and userid==USERID:
            print("Wrong Password !!!!!")

        if user==PASSWORD and userid!=USERID:
            print("Wrong userID !!!!!")

        if user!=PASSWORD and userid!=USERID:
            print("Wrong userID and wrong Password  !!!!!")
        # here we decrease the tries_left variable
        tries_left-=1
        print("Tries left : ",tries_left)

#****************** MAIN DELETE FUNCTION ********************
def delete_data():

    '''
        This function "delete_data()" reads a CSV file called emp_details.csv into a pandas DataFrame. 
        It then prompts the user to enter an employee ID to delete. If the DataFrame does not contain 
        any rows with the specified ID, the function prints an error message. If the DataFrame contains 
        one or more rows with the specified ID, the function removes those rows from the DataFrame and 
        saves the updated DataFrame back to the CSV file. Finally, the function prints a message 
        indicating that the employee was deleted successfully.

    '''
    # First we store the dataframe in df
    df=pd.read_csv('emp_details.csv')

    # then call the loop
    while 1:
        # user input for the Employee id
        id=input("Enter the ID of the Employee to delete : ")

        # if the dataframe shape is 0 ,then it will show the print function 
        if(df[df.Emp_Id==id].shape[0]==0):
            print("NO DATA FOUND !!!! Please enter valid Employee ID.")

        # If the dataframe shape is not 0.
        else:

            # first we drop the columns whose Emp_id match with the delete Emp_id
            df=df.drop(df[df.Emp_Id==id].index)

            # Then it load the dataframe to the csv file
            df.to_csv('emp_details.csv',index=False)

            print("\n\nDeleted Employee ID no. "+id+" Sucessfully.")
            time.sleep(2);
            break
