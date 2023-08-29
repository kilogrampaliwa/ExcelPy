
# imports and declarations
#_____________________________________

import csv as CSV
import os as OS
import re as RE



# functions used in program
#_____________________________________

# primary functions

def run():
    "Function that starts everything."
    # Here I intruduce myself.
    OS.system('cls')
    textLid()
    print("Welcome in shifter. I will separate columns of csv file.\n")
    input("...press enter continue")

    # Here I made main loop.
    continueFlag = True

    while continueFlag:

        result = masterFunction()

        if result:
            # I ask if client want to use me once again.
            OS.system('cls')
            textLid()
            print("Do you want to create another file? (y/n) \n")
            ans = input()
            continueFlag = y_n_recognizer(ans)


def masterFunction():
    "Function consoliding all secondary functions in this program."

    try:
        # Here I ask if user pasted file. I ask as long as she/he does not confirm.
        answer = False

        while answer!=True:

            OS.system('cls')
            textLid()
            print("Did you copied your .csv file to program folder? (y/n) \n")
            ans = input()
            answer = y_n_recognizer(ans)

        # Here I ask for name of this file. I ask as long as she/he does not print it properly.
        answer = False
        table : list
        name_old : str

        while answer!=True:

            OS.system('cls')
            textLid()
            print("Please print name of the file. Do not print extension.\n")
            name_old = input()
            result = loadData(name_old)

            if result:
                table = result
                answer = True

        # Here I ask for name for new file.
        name : str
        OS.system('cls')
        textLid()
        print("Please print name of new file.\n")
        name = input()

        # Here I ask for numbers of column to copy.  I ask as long as she/he does not print it properly.
        answer = False
        col_nums : list

        while answer!=True:

            OS.system('cls')
            textLid()
            print("Which of the columns would you have in new file?")
            print("Please separate col numbers by comas:  f.in.:    1, 2, 5 \n")
            ans = input()
            processed = readUserNum(ans)

            if processed:
                col_nums = processed
                answer = True

        # Here realize my mission - I create proper table
        tableOfColumns = []
        new_table=[]

        # I save all needed columns to one list (will be "2D")
        try:
            for n in col_nums:
                n = n-1
                tableOfColumns.append(giveMeColumn(table, n))
        except:
            errorPrinter("number of columns in original file")
            return False

        # I will transform table od Columns and save it as new_table.
        try:
            # To do so, I need the length of table. I took 1st row to check it.
            for i in range(len(tableOfColumns[0])):

                # "line" list will be my new row
                line = []

                for n in tableOfColumns:

                    line.append(n[i])

                # now I can add new line to my new, transformed table

                new_table.append(line)
        except:
            errorPrinter("table transformation")
            return False

        #Here I will save my work

        saveToFile(name, new_table)

        return True
    except:
        errorPrinter("master function")
        return False


# secondary functions

def loadData(name):
    "Function for reading .csv file."

    name += ".csv"
    outputTable = []

    try:
        tableCSV = [] # list format from csv

        with open(name, 'r') as file:
            tableCSV = list(CSV.reader(file))

        return tableCSV

    except:
        errorPrinter("file reading")
        return False


def giveMeColumn(table, colNumber):
    "Function for collumn extraction"

    output = [] # list

    try:
        for n in table:
            output.append(n[colNumber])
        return output
    
    except:
        errorPrinter("column extraction")
        return False


def saveToFile(fileName, readyTable):
    "Function to save data to file."

    try:
        fileName += ".csv"
        with open(fileName, 'x', newline='', encoding='utf-8') as file:
            writer = CSV.writer(file)
            writer.writerows(readyTable)
        return True
    except:
        errorPrinter("saving file")
        return False


def readUserNum(unsplitted):
    "Function for decoding user chosen columns."

    try:
        splittedStr = RE.split(', |,',unsplitted)
        splittedInt = []
        for x in splittedStr:
            splittedInt.append(int(x))
        if isListInt(splittedInt):
            return splittedInt
        else:
            errorPrinter("reading user's input")
            return False
    except:
        errorPrinter("reading user's input")
        return False

# tetriary functions

def y_n_recognizer(toCheck):
    if toCheck == 'y':
        return True
    else:
        return False


def isListInt(listToCheck):
    "Function to check if list is int."

    flag = False
    for x in listToCheck:
        if isinstance(x, int): flag = True
        else:
            flag = False
            return False
    if flag:
        return True
    else:
        return False


def errorPrinter(duringWhat):
    "Function to print error."

    print("Error during " + duringWhat + ".")
    print('\n')
    input("...press enter to exit")


def textLid():
    print("_________________________________________")
    print("                                         ")
    print("             columns shifter             ")
    print("_________________________________________")
    print("\n")


run()