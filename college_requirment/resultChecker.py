# # Function to convert letter grades to numeric scores
# def letter_to_numeric(letter_grade):
#     grades_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
#     return grades_mapping.get(letter_grade.upper(), 0)

# # Function to convert numeric scores to letter grades
# def numeric_to_letter(numeric_score):
#     grades_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}
#     return grades_mapping.get(numeric_score, 'F')

# # Function to compare scores with university standards
# def compare_with_standards(scores):
#     # University standards
#     university_standards = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

#     # Find the best scores from all subjects
#     best_score = min(scores)

#     # Compare with university standards
#     if best_score <= university_standards['B']:
#         print("Congratulations! You meet the university standards.")
#     else:
#         print("Sorry, you do not meet the university standards.")

# # Get input from the user for each subject
# num_subjects = 9
# subject_scores = []

# for i in range(num_subjects):
#     result = input(f"Enter the result for Subject {i+1} (A1 to F9): ")
#     score = letter_to_numeric(result)
#     subject_scores.append(score)

# # Compare scores with university standards
# compare_with_standards(subject_scores)


def letter_to_numeric(letter_grade):
    grades_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return grades_mapping.get(letter_grade.upper(), 0)

def numeric_to_letter(numeric_score):
    grades_mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}
    return grades_mapping.get(numeric_score, 'F')

def compare_with_standards(best_scores):
    # University standards
    university_standards = {'Math': 4, 'Physics': 4, 'Others': 5}

    # Check subjects against standards
    for subject, score in best_scores.items():
        max_accepted_score = university_standards.get(subject, 5)
        if score > max_accepted_score:
            return False  # Student does not meet the university standards

    return True  # Student meets the university standards

def main():
    # Get input from the user for each set of results
    num_subjects = int(input("Enter the number of subjects (between 7 and 9): "))
    
    results1 = {}
    results2 = {}

    for i in range(num_subjects):
        subject = input(f"Enter the subject name for Subject {i + 1}: ")
        result1 = input(f"Enter the result for Subject {i + 1} for Set 1 (A1 to F9): ")
        result2 = input(f"Enter the result for Subject {i + 1} for Set 2 (A1 to F9): ")

        score1 = letter_to_numeric(result1)
        score2 = letter_to_numeric(result2)

        # Store the scores in dictionaries
        results1[subject] = score1
        results2[subject] = score2

    # Calculate the best scores for each set
    best_scores1 = {subject: min(results1[subject], results2[subject]) for subject in results1}
    best_scores2 = {subject: min(results1[subject], results2[subject]) for subject in results2}

    # Compare best scores with university standards
    if compare_with_standards(best_scores1) and compare_with_standards(best_scores2):
        print("Both sets of results meet the university standards.")
    else:
        print("At least one set of results does not meet the university standards.")

if __name__ == "__main__":
    main()

