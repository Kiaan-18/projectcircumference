def calculate_circumference(radius):
    pi=3.14
    circumference=2*pi*radius
    return circumference
r=float(input("Enter the radius of the circle:"))
result=calculate_circumference(r)
print("the circumference of this circle is ",result)