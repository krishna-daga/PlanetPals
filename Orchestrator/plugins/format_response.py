import json
import ast
# def format_string_to_list(input_string: str) -> list:
#     """
#     Formats a string to a list, assuming the string is in the format of a JSON array.

#     :param input_string: The input string to be formatted.
#     :return: A list of strings.
#     """
#     # Remove any leading or trailing whitespace and newlines
#     trimmed_string = input_string.strip()

#     # Check if the string starts and ends with square brackets
#     if not (trimmed_string.startswith('[') and trimmed_string.endswith(']')):
#         raise ValueError("Input string must be a JSON array format.")

#     # Use the json module to parse the string into a list
#     list_from_string = json.loads(trimmed_string)

#     # Ensure all elements in the list are strings
#     if not all(isinstance(item, str) for item in list_from_string):
#         raise ValueError("All elements in the input string must be strings.")

#     return list_from_string

# # Example usage:
# input_string = '[ \n "Turn off 3 lights or electronics for 1 hour to reduce energy consumption.",\n "Use reusable bags or containers for 1 grocery shopping trip.",\n "Use a refillable water bottle for all your drinks throughout the day."\n]'
# formatted_list = format_string_to_list(input_string)
# print(formatted_list)

def format_string_to_list(input_string):
    try:
        # Convert the input string to a Python list
        result_list = ast.literal_eval(input_string)
        
        # Ensure that the result is a list
        if isinstance(result_list, list):
            return result_list
        else:
            raise ValueError("The input string does not represent a list.")
    except (ValueError, SyntaxError) as e:
        # Handle exceptions if the input string is not valid
        print(f"Error: {e}")
        return None
    
input_string = '[ \n "Turn off 3 lights or electronics for 1 hour to reduce energy consumption.",\n "Use reusable bags or containers for 1 grocery shopping trip.",\n "Use a refillable water bottle for all your drinks throughout the day."\n]'
print(format_string_to_list(input_string))