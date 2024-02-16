def key_with_lowest_value(input_dict):
    if not input_dict:
        return None

    # Find the key with the lowest value
    min_key = min(input_dict, key=input_dict.get)
    
    # Create a dictionary with the key-value pair having the lowest value
    result_dict = {min_key: input_dict[min_key]}
    
    return result_dict

# Example dictionary
CATEGORY2 = {
        'chemistry': 1,
        'science core':7
              }

CATEGORY3 = {
        'technical_drawing': 6,
        'engineering science': 6,
        'biology': 5,
        'economics': 6,
        'geography': 6,
        'agricultural science': 6 
    }
# Find the key with the lowest value
CATEGORY2_best = key_with_lowest_value(CATEGORY2)
print(CATEGORY2_best)

CATEGORY3_best = key_with_lowest_value(CATEGORY3)
# print(CATEGORY3_best)

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
Student_result = { 'mathematics': 5,
                   'english': 4,
                   'physics': 3} 
CATEGORY1_requirment = {
        'mathematics': 4,
        'english': 6,
        'physics': 4
    }

# Call the function and print the result
result = compare_dictionaries(Student_result, CATEGORY1_requirment)
if result == True:
    print("CATEGORY1 Test Passed")
else:
    print("CATEGORY1 Test Failed")

def compare_dictionaries(dict1, dict2):
    # Get the key and value from the first dictionary
    key, value = next(iter(dict1.items()))
    
    # Check if the key exists in the second dictionary
    if key in dict2:
        # Compare the values and return the dictionary with the lowest value
        if value <= dict2[key]:
            print('CATEGORY2 Test Passed')
            # return 'CATEGORY2 Test Passed'
        else:
            print('CATEGORY2 Test Failed')
            # return 'CATEGORY2 Test Failed'
    else:
        print(f"Key '{key}' not found in the second dictionary.")
        return None  

CATEGORY2_required = {
        'chemistry': 4,
        'science core':2
              }

CATEGORY3_required = {
        'technical_drawing': 6,
        'engineering science': 6,
        'biology': 5,
        'economics': 6,
        'geography': 6,
        'agricultural science': 6 
    }

dict1 = CATEGORY2_best 
dict2 = CATEGORY2_required
# print(CATEGORY2_best)
# print(CATEGORY2_required)
compare_dictionaries(dict1, dict2)

# dict1 = CATEGORY3_best 
# dict2 = CATEGORY3_required
# print(CATEGORY3_best)
# print(CATEGORY3_required)
# compare_dictionaries(dict1, dict2)




