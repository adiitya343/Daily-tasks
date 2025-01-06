# code for finding area of triangle



#first we will take input from user for all 3 sides of triangle

s1 = int(input("Enter 1st side triangle length : "))
s2 = int(input("Enter 2nd side triangle length : "))
s3 = int(input("Enter 3rd side triangle length : "))

def areaTriangle(s1, s2, s3):  #defining fuctions to calculate area of triangle by using semi perimeter 
    s = (s1+s2+s3)/2
    return (s*(s-s1)*(s*s2)*(s*s3))**0.5

print("Area = {:.2f}".format(areaTriangle(s1, s2, s3))) # calling function and print the area

