# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.

# Code takes an integer input 
# Then a while loops starts as long as the input is positive it keeps looping
# Save the highest number inside a variable so that you can keep the highest input value
# If the input value is negative then break the loop
# Print that highest value that was input

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
highest_value = 0
while num_int > 0:
    num_int = int(input("Input a number: "))
    blonk = num_int
    if blonk >= highest_value:
        highest_value = blonk
    if num_int < 0:
        break
    max_int = highest_value
print("The maximum is", max_int)    # Do not change this line


# %%
type(-1)


# %%



