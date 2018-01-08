# python function that takes in, a list of queen chess board coordinates (x,y) 
# and returns the first item in list that is able to take another queen

queens = ("(1,1)", "(7,2)", "(4,3)", "(6,4)", "(8,5)", "(2,6)", "(5,7)", "(3,8)")

def EightQueens(arr):

    space=""
    for i in range(8):
        for x in range(1, 8):
            if i + x < len(arr):
                if arr[i][1] == arr[i+x][1] and space =="":
                    space = "({},{})".format(arr[i][1], arr[i][3])

                elif arr[i][3] == arr[i+x][3] and space=="":
                    space = "({},{})".format(arr[i][1], arr[i][3])

                for y in range(1, 6):
                    if i + y < len(arr):
                        upright = "{},{}".format(str(int(arr[i][1]) + x), str(int(arr[i][3]) + x))
                        other_p = "{},{}".format(arr[i+y][1], arr[i+y][3])
                        if upright == other_p and space== "":
                            space = "({},{})".format(arr[i][1], arr[i][3])

                        downright = "{},{}".format(str(int(arr[i][1]) + x), str(int(arr[i][3]) - x))
                        if downright == other_p and space =="":
                            space = "({},{})".format(arr[i][1], arr[i][3])

                        upleft = "{},{}".format(str(int(arr[i][1]) - x), str(int(arr[i][3]) + x))
                        if upleft == other_p and space =="":
                            space = "({},{})".format(arr[i][1], arr[i][3])

                        downleft = "{},{}".format(str(int(arr[i][1]) - x), str(int(arr[i][3]) - x))
                        if downleft == other_p and space == "":
                            space = "({},{})".format(arr[i][1], arr[i][3])

    if space != "":
        print(space)
    if space == "":
        return True
