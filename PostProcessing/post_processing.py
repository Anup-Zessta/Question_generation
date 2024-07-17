import re
import random

def modify_operators(code):
    operator_mapping = {
        '<': '>',
        '>': '<',
        '+': '-',
        '-': '+',
        '*': '/',
        '/': '*',
        '==': '!=',
        '!=': '==',
        '<=': '>=',
        '>=': '<=',
        'not':'',
       
    }
    
    # Randomly select 2 or 3 keys from operator_mapping
    num_keys_to_modify = random.choice([3,10])
    keys_to_modify = random.sample(list(operator_mapping.keys()), num_keys_to_modify)
    
    # Define the regex pattern to match selected operators
    pattern = '|'.join(re.escape(op) for op in keys_to_modify)
    
    # Use re.sub with a lambda function to replace operators
    modified_code = re.sub(pattern, lambda m: operator_mapping[m.group(0)], code)
    
    return modified_code

def ensure_code_modification(original_code):
    modified_code = modify_operators(original_code)
    
    # Keep modifying the code until a change is detected
    while modified_code == original_code:
        modified_code = modify_operators(original_code)
    
    return modified_code

#Test case for a given code
original_code = """
def maxSubArray(nums):
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
"""

# Modify 2 or 3 random keys from operator_mapping
modified_code = ensure_code_modification(original_code)
print(modified_code)
