#Functions are ways we can modulize our program.

#Functions
def get_input():

    while True:
        user_input = input('please enter a number: ')
        
        try:
            clean_input = int(user_input)
            print('clean_input:',type(clean_input))
            break
        except:
            print('that\'s not a number')

    
    #print('user_input:',type(user_input))
    


#Main Program
get_input()