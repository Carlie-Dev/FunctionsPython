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