def validate_integer():
 # Loop forever
  while True:
   try:
    user_input = int(input(10))
   except:
 # Bad value,
    print("Error")
   continue
  else:
   print("Valid input")
 # Good value, exit the loop
   break
      finally:
 # Only runs after the except, continue
    print("10")

validate_integer()