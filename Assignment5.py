# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 21:48:50 2022

@author: Emeka
"""

#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# COsuji, 2022-Aug-06, Added functionality to load in existing text data file
# COsuji, 2022-Aug-06, Added Functionality to delete data entries
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        l = objFile.read().split("\n")
        objFile.close()
        loadedList = []
        for i in l:
            loadedList.append(i.split(","))
        loadedList.pop()

        for row in loadedList:
            load = {'intID':int(row[0]), "strTitle": row[1] , "strArtist": row[2]}
            lstTbl.append(load)
        
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        lstRow = {"intID": intID, "strTitle": strTitle , "strArtist": strArtist}
        lstTbl.append(lstRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row["intID"],row["strTitle"],row["strArtist"], sep = " ,")
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry   
        idDelete = int(input("Enter the associated ID for the row you wish to delete: "))    
        for row in lstTbl:
            if row["intID"] == idDelete:
                lstTbl.remove(row)
                
                
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(row[item]) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

