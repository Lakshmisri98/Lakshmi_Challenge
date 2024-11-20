import re

def is_valid_credit_card(card_number):
    # Check if the card number matches the regex for format
    pattern = r'^[456]\d{3}(-\d{4}){3}$'
    
    # If the card number doesn't match the basic pattern, it's invalid
    if not re.match(pattern, card_number):
        return "Invalid"
    
    # Remove hyphens for consecutive digit check
    card_number = card_number.replace('-', '')
    
    # Check for four consecutive repeated digits
    for i in range(len(card_number) - 3):
        if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
            return "Invalid"
    
    return "Valid"

# Input number of test cases
n = int(input())

# Input credit card numbers and validate each
for _ in range(n):
    card_number = input().strip()
    print(is_valid_credit_card(card_number))
