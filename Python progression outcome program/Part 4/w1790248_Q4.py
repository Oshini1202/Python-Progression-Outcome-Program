# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019757

# Date: 16/04/2020

# Part 4 – Alternative Staff Version (optional extension)

# data accessed from a list

print('''\t\t\t University of Westminster
         \t\t    Academic Year 2020
          \t\t   Progression Outcome
          \t\t Alternative Staff Version   
          \t\t===========================\n''')

test_input = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,0],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

for test_input_no in range(10):
    print(test_input_no +1,"\t",test_input[test_input_no],"\t",end="")
    
    check_input = test_input[test_input_no]
    total = check_input[0] + check_input[1] + check_input[2]


    def progress():                                                                     # check whether progression outcome  is progress
        if check_input[0] == 120:
            print("Progress")                                                           # Print progression as Progress
        else:
            trailer()                                                                   # calling the next function - trailer

       
    def trailer():                                                                      # check whether progression outcome  is trailer
        if (check_input[0] == 100):
            print("Progression Outcome : Progress - module trailer")
        else:
            exclude()                                                                   # calling the next function - exclude

            
    def exclude():                                                                      # check whether progression outcome is exclude
        if (check_input[2] > 60):
            print("Progression Outcome : Exclude")
        else:
            retriever()                                                                 # calling the next function - retriever

            
    def retriever():                                                                    # check whether progression outcome is retriever
        fail_credit = total - (check_input[0] + check_input[1])
        if fail_credit<=60:
            print("Progression Outcome : Do not progress – module retriever")

    progress()                                                                          # calling the progress function 

