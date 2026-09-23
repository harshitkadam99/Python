Name = "Harshit"
age = 21
Gender = "Male"

# print("Hello",Name," your age is",age,"and your gender is",Gender)   ## using comma
# print("Hello " + Name + " your gender is " + Gender + " your age is " + str(age))    ## using + operator

# print(Name,age,Gender,sep=" - ")  ## sep is used to separate the values with a specific character or string. By default, it is a space.
# print(Name,age,Gender,sep="  ")

# print(Name, end=" ")   ## end is used to specify what to print at the end of the output. By default, it is a newline character.
# print(age)
# print(Gender)

# the print staement we will use is F-String     ## best to use     ## we can change the ouput also by adding some formatting to the output. For example, we can add a space between the values, or we can add a specific character or string between the values.
print(f"Hello my name is {Name}, i am {age} years old and i am a {Gender}")

## we can change the ouput also by adding some formatting to the output. For example, we can add a space between the values, or we can add a specific character or string between the values.
print(f"Hello my name is {Name}, i am {age+50} years old and i am a {Gender}")