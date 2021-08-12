#
while True:
    marks=int(input("enter_marks"))
    print("enter_marks", marks)
    isinteger = isinstance(marks,int)
    print(isinteger)
    if 91 <= marks <= 100:
        print("A")
    elif 81 <= marks <= 90:
        print("B")
    elif 71 <= marks <= 80:
        print("C")
    elif 61 <= marks <= 70:
        print("D")

    else:
        print ("FAIL")
