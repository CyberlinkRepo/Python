
a=False
b=False
c=False

if a:
   print("a was true")
elif b:
    print("b was true")
elif c:
    print("c was true")
else:
    print("None of our boolean variables were true")   

the output was > a was true



if(7<4)and(6<9):
   print("Yup!")
else:
    print("Nope!")


    iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    # For each item, excute this code block
    print(item)


iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
   if item %2!=0:
    print(item)



iterable_variable = [1,2,3,4,5,6]
total = 0

for item in iterable_variable:
  total = total + item

print(total)


# Define a string to iterate over
for this_letter in "Glen Godinho":
 # Specify which letter to test for
 if this_letter == "G":
  # Found the test letter
  print(f"Woo hoo, found a {this_letter}!")
  # Exit the current loop
  break
else:
 # Didn't find the test letter
 print(f"Aww man, I didn't want a {this_letter}!")


my_list = [1,2,3,0]

for my_number in my_list:
  if my_number == 1:
     pass
  if my_number == 2:
     continue
  if my_number == 3:
     print(f"Found the number {my_number}")
  if my_number == 0:
     break


list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
  print(item)


# Tuple unpacking
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
  print(a)
  print(b)

for index in range(1, 100, 5):
 print(index)



scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
  print(f"Found a service on {ipv4} at {port}")