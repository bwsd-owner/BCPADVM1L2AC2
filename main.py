user_str = input("Please enter any String: ")

rev_str = ('')

for i in user_str:
    rev_str = i + rev_str
    
print("\nThe Original String = ", user_str)
print("The Reversed String = ", rev_str)
