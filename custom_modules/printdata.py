'''

Note :- need to install tabulate using pip install tabulate

We will first search for data using different search methods for different categories then view or print it on console
'''

import time
import pandas as pd
from tabulate import tabulate
# reference dictionary used in code below, no search by salary, email or phone
Dict={
    '1':'Emp_Id',
    '2':'Name',
    '3':'Age',
    '4':'Gender',
    '5':'Designation',
}

#******************* PRINT FUNCTION *****************

def printdata(opt, privilege_granted):
    req = input("Enter the " + Dict[opt] + " of the Employee: ")
    data_for_admin_only = pd.read_csv('emp_details.csv')
    data_for_admin_only['Age'] = data_for_admin_only['Age'].astype(str)
    data_for_general_use = data_for_admin_only.loc[:, ~data_for_admin_only.columns.isin(['Email', 'Phno'])]

    if privilege_granted in ['y', 'Y']:
        filtered_data = data_for_admin_only[data_for_admin_only[Dict[opt]].str.contains(req, case=False, na=False)]
    else:
        filtered_data = data_for_general_use[data_for_general_use[Dict[opt]].str.contains(req, case=False, na=False)]

    if not filtered_data.empty:
        # Use the tabulate library for formatting
        print(tabulate(filtered_data, headers='keys', tablefmt='grid'))
    else:
        print("No data found.")

'''
# working piece of code, above is more for beautiful representation

def printdata(opt, privilege_granted):

    req=input("Enter the " + Dict[opt] + " of the Employee : ")
    # Store entire raw data, can only be accessed by admins
    data_for_admin_only = pd.read_csv('emp_details.csv')

    # Convert age column to string
    data_for_admin_only['Age'] = data_for_admin_only['Age'].astype(str)

    # below ~ implies negation of the statement meaning avoid Email and Phno columns
    data_for_general_use = data_for_admin_only.loc[:, ~data_for_admin_only.columns.isin(['Email','Phno'])]

    if privilege_granted in ['y', 'Y']:
        #use admin data
        # Use str.contains() to search for the user substring in the specified column
        filtered_data = data_for_admin_only[data_for_admin_only[Dict[opt]].str.contains(req, case = False, na = False)]
        if not filtered_data.empty:
            print(filtered_data)
        else:
            print("No data found.")
    else:
        # use general data
        filtered_data = data_for_general_use[data_for_general_use[Dict[opt]].str.contains(req, case = False, na = False)]
        if not filtered_data.empty:
            print(filtered_data)
        else:
            print("No data found.")

'''
