# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 2019757

# Date:  02/04/2020

# Part 1 - Student Version

def pro_intro():                                                              # let the user know how to get progression outcomes and quit from the program
    print('''\t\t\t University of Westminster                                 
         \t\t    Academic Year 2020
          \t\t   Progression Outcome
          \t\t      Student Version
          \t\t===========================\n''')

    print('''Please enter:
        y         Another Student
        q         Exit\n''')                                                  


def input_valid_pass():                                                       # get valid input as pass credit
    while True:
            try:
                pass_credits = int(input('Pass credit:\n'))                   # check whether is it an integer
                return pass_credits
            except ValueError:
                    print('Requires a valid integer as Pass credit!')         # inform the user to input a valid integer as pass credit
                    

def input_valid_defer():                                                      # get valid input as defer credit
    while True:
         try:
            defer_credits = int(input('Defer credit:\n'))                     # check whether is it an integer
            return defer_credits
         except ValueError:
                print('Requires a valid integer as Defer credit!')            # inform the user to input a valid integer as defer credit
                

def input_valid_fail():                                                       # get valid input as fail credit
     while True:
         try:
            fail_credits = int(input('Fail credit:\n'))                       # check whether is it an integer
            return fail_credits

         except ValueError:
                print('Requires a valid integer as Defer credit!')            # inform the user to input a valid integer as fail credit


def creditValidity(pass_credits ,defer_credits,fail_credit):                                                            # let the user know if credits are not in the range                                                           
    credit_range = [0, 20, 40, 60, 80, 100, 120]
    
    if (pass_credits not in credit_range or defer_credits not in credit_range or fail_credits not in credit_range):     # check the range validity of each input
        print('Range error!')                                                                                           # print Range error
        return False
    else:
        return True                

#=============================================================================== ### Main Program ### =====================================================================================#


pro_intro()
credit_range = [0, 20, 40, 60, 80, 100, 120]

user_input = input(' Another Student(y/q)')                                                             # get user inputs of his requirements
user_input = user_input.lower()

while (user_input == 'y'):                                                                              # run the program until user input = 'y'

    pass_credits=input_valid_pass()                                                                     # assign the correct input value to the pass_credits
    defer_credits=input_valid_defer()                                                                   # assign the correct input value to the defer_credits
    fail_credits=input_valid_fail()                                                                     # assign the correct input value to the fail_credits

    if(not creditValidity(pass_credits,defer_credits,fail_credits)):
        continue    
                
   
    while True:
        total = pass_credits + fail_credits + defer_credits                                             
        if total == 120:                                                                                # check whether the total credits = 120
            if pass_credits == credit_range[6]:                                                         # check whether the progression of user is  Progress
                print('Progress')
               
                break
            elif pass_credits == credit_range[5]:                                                       # check whether the progression of user is  Trailer
                print('Progress-module trailer')
                
                break
            elif fail_credits > credit_range[3]:                                                        # check whether the progression of user is Exclude
                print('Exclude')
                
                break
            else:                                                                                       # check whether the progression of user is  Trailer
                print('Do not progress-module retriever')
                
                break
                
        else:
            print('Total is incorrect!')                                                                # let the user know the total is incorrect                                                                    
            break
        
    user_input = input(' Another Student(y/q)')                                                         # requires user inputs for show the progression outcome of a student or quit the program   
    user_input = user_input.lower()        
    
        
