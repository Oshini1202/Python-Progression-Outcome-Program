# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID: 2019757

# Date:   13/04/2020

# Part 2 - Staff Version 

Progress = 0;                                                                 # set Progress count to zero
Trailer = 0;                                                                  # set Trailer count to zero
Retriever = 0;                                                                # set Retriever count to zero
Excluded = 0;                                                                 # set Excluded count to zero

def pro_intro():                                                              # let the user know how to get progression outcomes and quit from the program
    print('''\t\t\t University of Westminster
         \t\t    Academic Year 2020
          \t\t   Progression Outcome
          \t\t      Staff Version
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
                print('Requires a valid integer as Fail credit!')            # inform the user to input a valid integer as fail credit


def creditValidity(pass_credits ,defer_credits,fail_credit):                                                            # let the user know if credits are not in the range                                                           
    credit_range = [0, 20, 40, 60, 80, 100, 120]
    
    if (pass_credits not in credit_range or defer_credits not in credit_range or fail_credits not in credit_range):     # check the range validity of each input
        print('Range error!')                                                                                           # print Range error
        return False
    else:
        return True

def print_vertical_histogram():
    print()
    print('Progress',Progress,'  :',"*"*Progress)
    print('Trailer',Trailer,'   :',"*"*Trailer)
    print('Retriever',Retriever,' :',"*"*Retriever)
    print('Excluded',Excluded,'  :',"*"*Excluded)                           # https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
                                                                            # used the above link to get an idea to make vertical histogram using stars

    total_outcome = Progress + Trailer + Retriever + Excluded               # calculate total outcome to print its value under the histogram
    print('\n',total_outcome,'outcomes in total.')
    
#=============================================================================== ### Main Program ### =====================================================================================#

pro_intro()

user_input = input(' Another Student(y/q)')                                 # get user inputs of his requirements
user_input = user_input.lower()

credit_range = [0,20,40,60,80,100,120]

while (user_input == 'y'):                                                  # run the program until user input = 'y'
    pass_credits=input_valid_pass()
    defer_credits=input_valid_defer()
    fail_credits=input_valid_fail()
    
    if(not creditValidity(pass_credits,defer_credits,fail_credits)):
        continue  
   
    while True:
        total = pass_credits + fail_credits + defer_credits                 # assign 3 user input values to a variable to check is the total credits equals to 120 or not
        if total == 120:
            if pass_credits == credit_range[6]:                             # check whether the progression of user is  Progress
                print('Progress')                                           
                Progress += 1                                               # count Progress
                break
            elif pass_credits == credit_range[5]:                           # check whether the progression of user is  Trailer
                print('Progress-module trailer')
                Trailer += 1                                                # count Trailer
                break
            elif fail_credits > credit_range[3]:                            # check whether the progression of user is Exclude 
                print('Exclude')
                Excluded += 1                                               # count exclude
                break
            else:                                                           # check whether the progression of user is  Trailer
                print('Do not progress-module retriever')                   
                Retriever += 1                                              # count Retriever
                break
                
        else:
            print('Total is incorrect!')                                    # let the user know total is incorrect
            break
        
    user_input = input(' Another Student(y/q)')                             # requires user inputs for show the progression outcome of a student or quit the program
    user_input = user_input.lower()
else:        
    if user_input == 'q':                                                   # run the program until user input = 'q' and show the vertical histogram
        print_vertical_histogram()
    else:
        print("Valid string Required.")                                     # let the user know if he put a string other than 'q','Q','Y' or 'y'
