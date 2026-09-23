# Implicit - where python does the conversion automatically. 
# Explicit - where we do the conversion manually using built-in functions like int(), float(), str(), etc.

num1 = "100"
num2  = "200"

num3 = int(num1)
num4 = int(num2)

print(num3+num4)
print (num1+num2)
print(int(num1)+int(num2))
# also we can do float to integer conversion and vice versa. For example:
# a = 10.5
# b = int(a)
# print(b)  # Output: 10
# c = 20
# d = float(c)
# print(d)  # Output: 20.0