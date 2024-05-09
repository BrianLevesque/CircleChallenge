from circleChallenge import Circle
print("Welcome to the Circle Tester")
circ = Circle(int(input("Please enter a radius for the circle: ")))
print(circ)
growing = True
while growing:
    grow = input("Would you like your circle to grow? (y/n)")
    if grow == "y":
        print("Stand by while your circle magically grows...")
        circ.grow()
        print(circ)
    else:
        print("goodbye")
        growing = False




