import json
'''this code three optional subject and take the best one'''

CATEGORY3 = {
        'technical_drawing': 6,
        'engineering science': 6,
        'biology': 5,
        'economics': 6,
        'geography': 6,
        'agricultural science': 6 
    }
best_of_category3 = ('Best Subject: {}: {}'.format(min(CATEGORY3, key=CATEGORY3.get), CATEGORY3[min(CATEGORY3, key=CATEGORY3.get)]))
print(best_of_category3)


'''this code compire two optional subjects and take the best one'''
CATEGORY2 = {
        'chemistry': 6,
        'science core':6
              }
best_of_category2 = ('\'{}: {}\''.format(min(CATEGORY2, key=CATEGORY2.get), CATEGORY2[min(CATEGORY2, key=CATEGORY2.get)]))


def string_to_dict(input_string):
    # Split the string by comma and space
    items = input_string.split(", ")
    
    # Create an empty dictionary
    dictionary = {}
    
    # Iterate through the items and split each item by colon
    for item in items:
        key, value = item.split(":")
        # Remove leading and trailing whitespaces
        key = key.strip()
        value = value.strip()
        # Add key-value pair to the dictionary
        dictionary[key] = value
    
    return dictionary
print(best_of_category2)
print(string_to_dict(best_of_category2))
print(type(best_of_category2))