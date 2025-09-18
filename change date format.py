from datetime import datetime
def convert_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d-%m-%Y')
        return formatted_date
    except ValueError:
        return "Invalid date format. Please enter it in yyyy-mm-dd format."

date_input = input("enter a date in yyyy-mm-dd format:")
converted_date = convert_date(date_input)
print("Converted date:", converted_date)