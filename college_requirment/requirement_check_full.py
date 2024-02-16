
#-----------------------------------------------1---------------------------------------------------------
#compare the student results(two) and make a new result(best result) with the best grade from either result
Result_1 = {'math': 3, 'english': 3, 'physics': 3, 'chemistry': 5, 'f_maths': 5, 'biology': 1, 'sci_core': 3, 'technical_drawing': 6}
Result_2 = {'math': 5, 'english': 6, 'physics': 4, 'chemistry': 5, 'f_maths': 2, 'biology': 3, 'sci_core': 1, 'technical_drawing': 6}

# Create a dictionary with keys 'A' to 'H' and initial values as None
Best_result = {'math': None, 'english': None, 'physics': None, 'chemistry': None, 'f_maths': None, 'biology': None, 'sci_core': None, 'technical_drawing': None}

# Iterate through keys of the dictionaries using a for loop
for key in Best_result.keys():
    # Compare values at the current key using the min() function
    minimum_value = min(Result_1[key], Result_2[key])

    # Update the dictionary with the minimum value for the current key
    Best_result[key] = minimum_value

# Print the result
print("Best_result = ", Best_result)

#--------------------------------------------------2------------------------------------------------------

#this code checks the three compulsory subjects against university requirments and determine pass or fail.
def compare_dictionaries(Student_result, Requirement):
    # Check if keys are the same in both dictionaries
    if set(Student_result.keys()) != set(Requirement.keys()):
        return False  # If keys are not the same, dictionaries are not comparable
    
    # Compare values for each key
    for key in Student_result:
        if Student_result[key] > Requirement[key]:
            return False  # If any value in Student_result is not less than the corresponding value in Requirement, return False
    
    return True  # All values in Student_result are less than the corresponding values in Requirement

# Example dictionaries
Student_result = {'math': 5, 'english': 6, 'physics': 3 } 
Requirement =    {'math': 5, 'english': 6, 'physics': 4 }

# Call the function and print the result
result = compare_dictionaries(Student_result, Requirement)
if result == True:
    print("ACCEPTED")
else:
    print("REJECTED")


#-------------------------------------------------------3-------------------------------------------------------
    

'''this code three optional subject and take the best one'''

three_subjects = {'eng_sci':2, 'f_maths':3, 'tech_drawing':1}
best_of_three_subject = ('Best Subject: {}: {}'.format(min(three_subjects, key=three_subjects.get), three_subjects[min(three_subjects, key=three_subjects.get)]))
print(best_of_three_subject)


'''this code compire two optional subjects and take the best one'''
two_subjects = {'chem':2, 'sci_core':6}
best_of_two_subjects = ('Best Subject: {}: {}'.format(min(two_subjects, key=two_subjects.get), two_subjects[min(two_subjects, key=two_subjects.get)]))
print(best_of_two_subjects)


'''
my issue now is putting everything togother 
1. check for the two optional (code-3) then append to code two dictinory or
2. if code 2 pass proceed to check code three then return accepted or rejected 
      else return rejected without checking code two 


    hope this make smoll sense n u able understand am smoll 
    iam a beginner you know so na for manage look am and help pleeeeaaaaasssseee
    thank yoooooouuuu!
'''


