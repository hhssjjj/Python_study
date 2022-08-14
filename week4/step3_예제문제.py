
line = 4
def StarCount2(height):

    for i in range(1, line+1) :
        star = ""
        for _ in range(i) :
            star += "*"
        print(star)

StarCount2(int(input("height: ")))