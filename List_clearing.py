#This is a Python Program to demonstrate clearing a list using clear and Reinitializing 

# Initializing lists 
list1 = [1, 2, 3] 
list2 = [5, 6, 7] 

# Printing list1 before deleting 
print ("List1 before deleting is : "
+ str(list1)) 

# deleting list using clear() 
list1.clear() 

# Printing list1 after clearing 
print ("List1 after clearing using clear() : "
+ str(list1)) 

# Printing list2 before deleting 
print ("List2 before deleting is : "
+ str(list2)) 

# deleting list using reinitialization 
list2 = [] 

# Printing list2 after reinitialization 
print ("List2 after clearing using reinitialization : "
+ str(list2)) 
