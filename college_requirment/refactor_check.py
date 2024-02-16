# Define the subject category requirements
REQUIREMENTS = {
    'CATEGORY1': {
        'mathematics': 5,
        'english': 6,
        'physics': 4
    },
    'CATEGORY2': {
        'chemistry': 6,
        'science core': 6
    },
    'CATEGORY3': {
        'technical_drawing': 6,
        'engineering science': 6,
        'biology': 5,
        'economics': 6,
        'geography': 6,
        'agricultural science': 6 
    }
}

# Function to find the minimum grades for each subject from two result sets
def get_best_grades(result1, result2):
    # Combine all unique subjects from both result sets
    subject_submitted = {**result1, **result2}.keys()

    # Create a dictionary with subjects as keys, initialized all values to None
    best_result = dict.fromkeys(subject_submitted)

    # Iterate over each subject and find the minimum grade from result1 and result2
    for key, _ in best_result.items():
        # Use get() to handle cases where a subject is missing in one of the result sets
        best_result[key] = min(result1.get(key, 9999), result2.get(key, 9999))

    # Return the dictionary containing the best grades for each subject
    return best_result

def check_category_1(best_grades, category1):
    raise NotImplementedError("Not implemented yet")

def check_category_2(best_grades, category2):
    raise NotImplementedError("Not implemented yet")

def check_category_3(best_grades, category3):
    raise NotImplementedError("Not implemented yet")


# Define the grades for two sets of results
result1 = {
    'mathematics': 3, 'english': 3, 'physics': 3, 
    'chemistry': 5, 'further mathematics': 5, 'biology': 1, 
    'science core': 3, 'technical drawing': 6
}
result2 = {
    'mathematics': 5, 'english': 6, 'physics': 4, 
    'chemistry': 5, 'further mathematics': 2, 'biology': 3, 
    'science core': 1, 'technical drawing': 6
}

# Get the best grades from the two result sets
best_grades = get_best_grades(result1, result2)
print(best_grades)

# Extract category requirements
category_1 = REQUIREMENTS['CATEGORY1']
category_2 = REQUIREMENTS['CATEGORY2']
category_3 = REQUIREMENTS['CATEGORY3']

# Check if the best grades meet the requirements for all three categories
if (
    check_category_1(best_grades, category_1) and
    check_category_2(best_grades, category_2) and 
    check_category_3(best_grades, category_3)
):
    print("ACCEPTED")
else:
    print("REJECTED")
