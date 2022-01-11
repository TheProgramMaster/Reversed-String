#Ask user for input concerning text of string to reverse.
user_input = input("Please enter a string to reverse: ")
#Compartmentalize program as a singular function to execute when user runs program.
def reverse_string(string):
    #Create empty list.
    my_array = [0]*len(string)
    #Fill new list in reverse order of input string.
    for i in range(len(string)):
        my_array[i] = string[len(string)-i-1]
    #Create new reversed string, and fulfill contents of reversed string
    #in comparison to contents of initial string as an array.
    my_reversed_string = ""
    for i in range(len(my_array)):
        my_reversed_string += my_array[i]
    print(my_reversed_string)

#Execute main function to reverse string and return contents of reversed string
#to user via execution console.
reverse_string(user_input)        
