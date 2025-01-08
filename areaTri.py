# code for finding area of triangle



#first we will take input from user for all 3 sides of triangle

side1 = int(input("Enter 1st side triangle length : "))
side2 = int(input("Enter 2nd side triangle length : "))
side3 = int(input("Enter 3rd side triangle length : "))

def areaTriangle(side1, side2, side3):  #defining fuctions to calculate area of triangle by using semi perimeter 
    semiPerimeter = (side1 + side2 + side3)/2
    return (semiPerimeter*(semiPerimeter-side1)*(semiPerimeter*side2)*(semiPerimeter*side3))**0.5

print("Area = {:.2f}".format(areaTriangle(side1, side2, side3))) # calling function and print the area

