num1=float(input("enter the 1st number : "))
num2=float(input("enter the 2nd number : "))
num3=float(input("enter the 3rd number : "))

op=input("enter any one opertor for calculation: ,+,-,*,/ ")
if op=="+":
    add=num1+num2+num3
    print("the addition of the numbers is: ",add)
elif op=="-":
    sub=num1-num2-num3
    print("the subtraction of the numbers is:  ",sub)
elif op=="*":
    multiply=num1*num2*num3
    print("the multiplication of the numbers is:  ",multiply)
elif op=="/":
    if num1 or num2 or num3==0:
        print("not divisible by 0")
    else:
        div=num1/num2/num3
        print("the division of the numbers is:  ",div)
else:
    print("not valid opertor ")
