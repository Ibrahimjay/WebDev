# list1 = {'A': 5, 'B': 3, 'C': 4, 'D': 2, 'E': 7, 'F': 1, 'G': 3, 'H': 6}
# list2 = {'A': 2, 'B': 8, 'C': 6, 'D': 5, 'E': 3, 'F': 5, 'G': 6, 'H': 6}

# # Create a dictionary with keys 'A' to 'H' and initial values as None
# min_dict = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None, 'H': None}

# # Iterate through keys of the dictionaries using a for loop
# for key in min_dict.keys():
#     # Compare values at the current key using the min() function
#     minimum_value = min(list1[key], list2[key])

#     # Update the dictionary with the minimum value for the current key
#     min_dict[key] = minimum_value

# # Print the result
# # print("Minimum dict:", min_dict)
# print(min_dict)


# standard_dict = {'A':4, 'B':5, 'C':6, 'D':6, 'E':6, 'F':7, 'G':7, 'H':6 }


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
Student_result = {'math': 3, 'english': 3, 'physics': 3, 'chemistry': 5, 'f_maths': 5, 'biology': 1, 'sci_core': 3, 'technical_drawing': 6}
Requirement =    {'math': 4, 'english': 6, 'physics': 3, 'chemistry': 6, 'f_maths': 6, 'biology': 6, 'sci_core': 6, 'technical_drawing': 6}

# Call the function and print the result
result = compare_dictionaries(Student_result, Requirement)
if result == True:
    print("ACCEPTED")
else:
    print("REJECTED")


age = input('Enter Your age: ')

dict = {'name':'jay', 'age':20}

dict['age'] = age
print(dict)

#initalize a dictinory 
test_dict = {'one': 1, 'two': 2, 'three': 3}
#extracting specific keys fron dictinory using dictinory comprehension
res = {key: test_dict[key] for key in test_dict.keys() & {'two', 'three'}}
print(res)