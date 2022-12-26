"""
Class template by JOR
Revision History
06OCT22: Alpha
"""
class MyTemplate():
 pass
# Instantiate the class
my_object = MyTemplate()
# Check the object and type
print(type(my_object

# Constructor, called whenever an instance of the class is created.
 def __init__(self) -> None:
 print("Constructor ran")
 
 # Constructor, called whenever an instance of the class is created.
 def __init__(self, attribute1: str, attribute2: bool) -> None:
 print("Constructor ran")
 # Take in an argument and assign it to a meaningful attribute name
 self.attr1 = attribute1
 self.attr2 = attribute2
 
 # Instantiate the class
my_object = MyTemplate("John", True)


# Define a class object attribute, it will be the same for any instance of the class
 semi_major_axis = 6378137
 semi_minor_axis = 6356752
 
 
 # Instantiate the class
my_object = MyTemplate("John", True)
# Check the object
print(my_object.semi_major_axis, my_object.semi_minor_axis)


