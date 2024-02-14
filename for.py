# For function


# For Loop list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  


# For loop Break 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)



# For loop continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
  
  
# For Loop range
for x in range(6):
  print(x)
  
  
  
# For loop using parameter
for x in range(2, 6):
  print(x)
  
# for x in range(Start, stop):
#   print(x)

for x in range(2, 30, 3):
  print(x)

# for x in range(Start, Stop, Gap):
#   print(x)




# For Loop else statement
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
# The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
  


# For Loop Nested loop

# The "inner loop" will be executed one time for each iteration of the "outer loop"

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    

# For Loop pass

#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass