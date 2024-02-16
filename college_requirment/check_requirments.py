

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
Student_result = {'math': 5, 'english': 1, 'physics': 3 } 
Requirement =    {'math': 5, 'english': 1, 'physics': 4 }

# Call the function and print the result
result = compare_dictionaries(Student_result, Requirement)
if result == True:
    print("Test Passed")
else:
    print("Test Failed")