#uncomment the following codes to provide inputs


# mathematics1 = int(input('Enter maths grade: '))
# mathematics2 = int(input('Enter maths grade: '))

# english1 = int(input('Enter english grade: '))
# english2 = int(input('Enter english grade: '))

# physics1 = int(input('Enter physics grade: '))
# physics2 = int(input('Enter physics grade: '))

# chemistry1 = int(input('Enter chemistry grade: '))
# chemistry2 = int(input('Enter chemistry grade: '))

# further_maths1 = int(input('Enter further_maths grade: '))
# further_maths2 = int(input('Enter further_maths grade: '))

# engineering_science1 = int(input('Enter engineering_science grade: '))
# engineering_science2 = int(input('Enter engineering_science grade: '))

# technical_drawing1 = int(input('Enter technical_drawing grade: '))
# technical_drawing2 = int(input('Enter technical_drawing grade: '))

# economics1 = int(input('Enter economics grade: '))
# economics2 = int(input('Enter economics grade: '))

# geography1 = int(input('Enter geography grade: '))
# geography2 = int(input('Enter geography grade: '))

# biology1 = int(input('Enter biology grade: '))
# biology2 = int(input('Enter biology grade: '))

# science_core1 = int(input('Enter science_core grade: '))
# science_core2 = int(input('Enter science_core grade: '))

# agricultural_science1 = int(input('Enter agricultural_science grade: '))
# agricultural_science2 = int(input('Enter agricultural_science grade: '))

#compare the student results(two) and make a new result(best result) with the best grade from either result
Result_1 = {'mathematics': 3,
             'english': 3,
             'physics': 3,
             'chemistry': 5, 
             'further_maths': 5,
             'engineering_science':5,
             'technical_drawing': 6,
             'economics':6,
             'geography':6,
             'biology': 6,
             'science_core': 5,
             'agricultural_science':6}

Result_2 = {'mathematics': 5,
             'english': 2,
             'science_core': 1,
             'physics': 3,
             'chemistry': 5, 
             'further_maths': 2,
             'biology': 5,
             'engineering_science':7,
             'technical_drawing': 6,
             'economics':4,
             'geography':3,
             'agricultural_science':6}

# Result_1['mathematics'] = mathematics1
# Result_2['mathematics'] = mathematics2

# Result_1['english'] = english1
# Result_2['english'] = english2

# Result_1['physics'] = physics1
# Result_2['physics'] = physics2

# Result_1['chemistry'] = chemistry1
# Result_2['chemistry'] = chemistry2

# Result_1['further_maths'] = further_maths1
# Result_2['further_maths'] = further_maths2

# Result_1['engineering_science'] = engineering_science1
# Result_2['engineering_science'] = engineering_science2

# Result_1['technical_drawing'] = technical_drawing1
# Result_2['technical_drawing'] = technical_drawing2

# Result_1['economics'] = economics1
# Result_2['economics'] = economics2

# Result_1['geography'] = geography1
# Result_2['geography'] = geography2

# Result_1['biology'] = biology1
# Result_2['biology'] = biology2

# Result_1['science_core'] = science_core1
# Result_2['science_core'] = science_core2

# Result_1['agricultural_science'] = agricultural_science1
# Result_2['agricultural_science'] = agricultural_science2


Best_result = {'mathematics': None,
             'english': None,
             'physics': None,
             'chemistry': None, 
             'further_maths': None,
             'biology': None,
             'science_core': None,
             'technical_drawing': None,
             'economics':None,
             'geography':None,
             'engineering_science':None,
             'agricultural_science':None}

# Iterate through keys of the dictionaries using a for loop
for key in Best_result.keys():
    # Compare values at the current key using the min() function
    minimum_value = min(Result_1[key], Result_2[key])

    # Update the dictionary with the minimum value for the current key
    Best_result[key] = minimum_value
    
#categorise subjects from best result dictinory
CATEGORY1 = {key: Best_result[key] for key in Best_result.keys() & 
                   {'physics','mathematics','english'}}

# print('CATEGORY1 =', CATEGORY1)

CATEGORY2 = {key: Best_result[key] for key in Best_result.keys() & 
                   {'chemistry','science_core'}}

# print('CATEGORY2 =', CATEGORY2)

CATEGORY3 = {key: Best_result[key] for key in Best_result.keys() & 
                   {'technical_drawing',
                     'engineering_science', 
                     'biology',
                     'economics',
                     'geography',
                     'agricultural_science',
                     'further_maths' }}

#select and remove the best grade for each catogery
def key_with_lowest_value(input_dict):
    if not input_dict:
        return None

    # Find the key with the lowest value
    min_key = min(input_dict, key=input_dict.get)
    
    # Create a dictionary with the key-value pair having the lowest value
    result_dict = {min_key: input_dict[min_key]}
    
    return result_dict

CATEGORY1_requirment = {
        'mathematics': 1,
        'english': 5,
        'physics': 4
    }
print('CATEGORY1_requirment =', CATEGORY1_requirment)

CATEGORY2_requirment = {
        'chemistry': 6,
        'science_core':2
              }
print('CATEGORY2_requirment =', CATEGORY2_requirment)

CATEGORY3_requirment = {
        'technical_drawing': 6,
        'engineering_science': 6,
        'biology': 5,
        'economics': 6,
        'geography': 6,
        'agricultural_science': 6, 
        'further_maths': 7
    }
print( 'CATEGORY3_requirment =', CATEGORY3_requirment)


CATEGORY1_best = CATEGORY1
print('CATEGORY1_best =', CATEGORY1_best)

CATEGORY2_best = key_with_lowest_value(CATEGORY2)
print('CATEGORY2_best =', CATEGORY2_best)

CATEGORY3_best = key_with_lowest_value(CATEGORY3)
print('CATEGORY3_best =', CATEGORY3_best)

def compare_dictionaries_core(CATEGORY1_best, CATEGORY1_requirment):
    # Check if keys are the same in both dictionaries
    if set(CATEGORY1_best.keys()) != set(CATEGORY1_requirment.keys()):
        return False  # If keys are not the same, dictionaries are not comparable
    
    # Compare values for each key
    for key in CATEGORY1_best:
        if CATEGORY1_best[key] > CATEGORY1_requirment[key]:
            # print("CATEGORY1 Test Passed")
            return False  # If any value in Student_result is not less than the corresponding value in Requirement, return False
        # print("CATEGORY1 Test Failed")
    return True  # All values in Student_result are less than the corresponding values in Requirement


# Call the function and print the result
result_ct1 = compare_dictionaries_core(CATEGORY1_best, CATEGORY1_requirment)
if result_ct1 == True:
    print("CATEGORY1 Test Passed")
    
else:
    print("CATEGORY1 Test Failed")

def compare_category2(CATEGORY2_best, CATEGORY2_requirment):
    # Get the key and value from the first dictionary
    key, value = next(iter(CATEGORY2_best.items()))
    
    # Check if the key exists in the second dictionary
    if key in CATEGORY2_requirment:
        # Compare the values and return the dictionary with the lowest value
        if value <= CATEGORY2_requirment[key]:
            print('CATEGORY2 Test Passed')
            return True
        else:
            print('CATEGORY2 Test Failed')
            return False
    else:
        print(f"Key '{key}' not found in the second dictionary.")
        return None 


def compare_category3(CATEGORY3_best, CATEGORY3_requirment):
    # Get the key and value from the first dictionary
    key, value = next(iter(CATEGORY3_best.items()))
    
    # Check if the key exists in the second dictionary
    if key in CATEGORY3_requirment:
        # Compare the values and return the dictionary with the lowest value
        if value <= CATEGORY3_requirment[key]:
            print('CATEGORY3 Test Passed')
            return True
            # return 'CATEGORY3 Test Passed'
        else:
            print('CATEGORY3 Test Failed')
            # return 'CATEGORY3 Test Failed'
    else:
        print(f"Key '{key}' not found in the second dictionary.")
        return None  



# dict1 = CATEGORY2_best 
# dict2 = CATEGORY2_required
# print(CATEGORY2_best)
# print(CATEGORY2_required)
# compare_category2(CATEGORY2_best, CATEGORY2_requirment)
result_ct2 = compare_category2(CATEGORY2_best, CATEGORY2_requirment)


# dict1 = CATEGORY3_best 
# dict2 = CATEGORY3_requirment
# print(CATEGORY3_best)
# print(CATEGORY3_required)
# compare_category3(CATEGORY3_best, CATEGORY3_requirment)
result_ct3 = compare_category3(CATEGORY3_best, CATEGORY3_requirment)



if result_ct1 == True and result_ct2 == True and result_ct3 == True:
    print('Accepted')

else:
    print('Rejected')

