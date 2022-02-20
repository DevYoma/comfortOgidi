#codes of this color signifies a comment
print("This is a Python program to calculate the Determinant of a 3x3 matrix 🚀")

print(
    '''
        The input will take this format
                a1 a2 a3
                b1 b2 b3
                c1 c2 c3
    '''
)

a1 = int(input("a1 input: "))
a2 = int(input("a2 input: "))
a3 = int(input("a3 input: "))
b1 = int(input("b1 input: "))
b2 = int(input("b2 input: "))
b3 = int(input("b3 input: "))
c1 = int(input("c1 input: "))
c2 = int(input("c2 input: "))
c3 = int(input("c3 input: "))


determinantOne = ((b2*c3) - (b3*c2))
determinantTwo = ((b1*c3) - (b3*c1))
determinantThree = ((b1*c2) - (b2*c1))
print(determinantOne, determinantTwo, determinantThree)
determinant = ((a1 * determinantOne) -(a2 * determinantTwo) + (a3 * determinantThree))
print(f"The determinant of the matrix is {determinant}")