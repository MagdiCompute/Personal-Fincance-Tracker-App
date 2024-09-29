from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I":"Income", "E":"Expense"}
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if not date_str and allow_default:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy format")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than 0 and non negative")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter category: ")
    if category not in CATEGORIES:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense")
        return get_category()
    return CATEGORIES[category]

def get_description():
    return input("Enter description(optional): ")