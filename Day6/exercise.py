#Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that is being ordered. 
# Call the function three times, using a different number of arguments each time

#tuple
def sandwich(*items):
#    for item in items:
 #       print (item)

#    print(f"This sandwich has these items {items}")

     print("This sandwich has these items",", ".join(items))


sandwich("chicken","cheese","chilli")
sandwich("Lettuce","beef","peppers")
sandwich("Tomato","gherkin","cheese")
print("done that will be £35")
