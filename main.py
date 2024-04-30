from prettytable import PrettyTable


def printTable(data, flag):
    table = PrettyTable()

    if flag == 'userData':
        table.field_names = ['Process', 'Arrival Time', 'Burst Time']
    elif flag == 'outputData':
        table.field_names = ['Process', 'Arrival Time', 'Burst Time', 'Completion Time', 'Waiting Time', 'Turnaround']

    # add rows to table
    for row in data:
        table.add_row(row)

    print(table)

def printMenu():
    menu = PrettyTable()

    # add table data
    menu.field_names = ["Option #", "Algorithm"]
    menu.add_row([1, "First Come First Serve (FCFS)"])
    menu.add_row([2, "Round Robin (RR)"])
    menu.add_row([3, "Shortest Process Next (SPN)"])
    menu.add_row([4, "Shortest Remaining Time (SRT)"])
    menu.add_row([5, "Highest Response Ratio Next (HRRN)"])
    menu.add_row([6, "Feedback (FB)"])
    menu.add_row([-1, "Quit"])
    
    print(menu)

def acceptData():
    inputData = []
    rowData = []

    continueInput = True
    row = input('Enter Data in Format: Processes Name, Arrival Time, Burst Time (-1 to Stop)\n> ')
    while continueInput:
        if row == '-1':
            continueInput = False
            break
        else:
            rowData = row.split(',') # split into its separate value

            inputData.append(rowData) if len(rowData) == 3 else print('Requires Three Values Only')
            

        row = input('> ')

    printTable(inputData, 'userData')

def FCFS():
    acceptData()

def RR():
    acceptData()

def SPN():
    acceptData()

def SRT():
    acceptData()

def HRRN():
    acceptData()

def FB():
    acceptData()

if __name__ == "__main__":

    menuSelection = {
    '1': FCFS,
    '2': RR,
    '3': SPN,
    '4': SRT,
    '5': HRRN,
    '6': FB,
    }

    continueAlgo = True
    while continueAlgo:
        
        printMenu()
        userInput = input('Enter Your Algorithm Options: ')
        try:
            # exist if input -is -1
            if userInput == '-1':
                continueAlgo = False
                break

            menuSelection[userInput]() # call selected algorithm
        except:
            # user inputs a selection that doesn't exist
            print("Option Doesn't Exist.. Try Again")



   