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

# Example usage with one key-value pair:
input_string = "name: John"
result = string_to_dict(input_string)
print(result)
print(type(result))


def compare_dictionaries(dict1, dict2):
    # Get the key and value from the first dictionary
    key, value = next(iter(dict1.items()))
    
    # Check if the key exists in the second dictionary
    if key in dict2:
        # Compare the values and return the dictionary with the lowest value
        if value < dict2[key]:
            print('Test Passed')
            return 'Test Passed'
        else:
            print('Test Failed')
            return 'Test Failed'
    else:
        print(f"Key '{key}' not found in the second dictionary.")
        return None

# Example dictionaries
dict1 = {"age": 4}  # Dictionary with one key-value pair
dict2 = {"name": 5, "age": 3, "city": "New York"}  # Dictionary with multiple key-value pairs

# Comparing dictionaries
compare_dictionaries(dict1, dict2)
print('HI')

age = input('Enter Your age: ')

dict = {'name':'jay', 'age':20}

dict['age'] = age
print(dict)

