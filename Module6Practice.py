#Functions are ways we can modulize our program.

#Functions
def get_number(unclean_input):

    while True:
        
        try:
            clean_input = int(unclean_input)
            #print('clean_input:',type(clean_input))
            break
        except:
            print('that\'s not a number')

    return clean_input

    
    #print('user_input:',type(user_input))
    


#Main Program
#calculator

#declare variables
total = 0

numbers = get_number(input('Please enter how many numbers you want to add: '))

for i in range(numbers):
    input_num = get_number(input('Please enter a number to add: '))
    total += input_num

print(f'The total sum is {total}')


#Three different functions

#Function to just run code
def say_something_nice():
    print('Wow! Nice hair cut!')

#Function that needs parameters
def greeting(name):
    print(f'Hi {name}, how are you?')

#Function that returns something
def square_num(number):
    return number * number

#Main Program
say_something_nice()

greeting(input('What is your name? '))

print(square_num(get_number(input('Please enter a number: ')))) 