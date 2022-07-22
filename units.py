import datetime
symbol = input("Enter Symbols: ") 
if symbol.isalpha() == True and len(symbol) == 7 and symbol.isupper() == True: 
  print("Valid Symbols") 
else:
  print("Invalid Symbols") 

try:
  chart = int(input("Enter Chart Type: ")) 
  if chart == 1 or chart == 2:  
    print("Valid Chart Type") 
  else:
    print("Invaild Chart Type") 
except ValueError:
  print("Invaild Chart Type") 

try:
  time = int(input("Enter Time Series: ")) 
  if time > 0 and time < 5:  
    print("Valid Time Series") 
  else:
    print("Invaild Time Series")  
except ValueError:
  print("Invaild Time Series") 

date_string = input("Enter start date in the format YYYY-MM-DD: ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format) 
  print("Vaild date format")
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format") 

date_string = input("Enter end date in the format YYYY-MM-DD: ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format) 
  print("Vaild date format") 
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format") 
