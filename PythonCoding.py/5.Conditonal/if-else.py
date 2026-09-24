## indentation is very important in python (4 spaces or 1 tab)
## if you would not use the else staement so it would come in the "empty output" form.

age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

## Q: write a program to grade on the basics of range of marks obtained by the student. above 90 - A grade, above 80 - B grade, above 70 - C grade, above 60 - D grade, below 60 - F grade.
## (also we will chek with -10 and 1000000)

## Nested if-else statement (if one if comes under another if statement then it is called nested if-else statement)
age = 20
certificte = True
if age >= 18:
    pass    ## the pass statement is used to avoid the error of empty body in the if statement.
else:
    print("you are not eligible to vote")


if age >= 18:
    if certificte == True:
        print("you are hirted")
    else:
        print("you are not hirted")
else:
    print("you are not eligible to vote")


## else kai andar bhi if eslse aenge aa sakte haii 


## Ternary operator (conditional expression) is a one line if-else statement. It is used to assign a value to a variable based on a condition.
age = int(input("enter your age: "))
status = "eligible to vote" if age >= 18 else "not eligible to vote"
print(status)


