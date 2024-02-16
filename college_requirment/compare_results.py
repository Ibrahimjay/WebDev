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
             'science_core': 3,
             'agricultural_science':6}

Result_2 = {'mathematics': 3,
             'english': 1,
             'science_core': 7,
             'physics': 3,
             'chemistry': 5, 
             'further_maths': 2,
             'biology': 1,
             'engineering_science':2,
             'technical_drawing': 6,
             'economics':4,
             'geography':3,
             'agricultural_science':6}


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

# Print the result
# print("Best_result = ", Best_result)

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

# print('CATEGORY3 =', CATEGORY3)








