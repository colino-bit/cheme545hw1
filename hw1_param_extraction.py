#function to read out process parameters when process unit, process parameter, and index are input
def extract_parameter(user_input1,user_input2,user_input3):  
    #implementing try and except function to read out input error if input not found in dictionary
    try:
        value = unit_operations_data[user_input1][user_input2][user_input3]
        printout = user_input1 + "_" + user_input2 + "_" + str(value)
       
    except (KeyError,IndexError,ValueError): #will print out 'Invalid input' if incorrect unit or incorrect index entered
        printout = 'Invalid input'

    return printout