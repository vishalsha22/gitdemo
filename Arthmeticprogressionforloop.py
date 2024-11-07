Initial_term = int(input("Enter the Initial Term "))
Common_difference = int(input("Enter the Common Difference "))
Number_of_terms = int(input("Enter the Number of Terms "))

for t in range(Initial_term,Initial_term+Number_of_terms*Common_difference,Common_difference):
    print('The AP series based on your input is ',t)

#formula for range of AP series endpoint is a+n*d
