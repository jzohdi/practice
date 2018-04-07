#    /3/
#   \7\ 4 
#  2 \4\ 6 
# 8 5 \9\ 3
# Here comes the task...
# Let's say that the 'slide down' is a sum of consecutive numbers from the top to the bottom of the pyramid. 
# As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23
# Your task is to write a function longestSlideDown (in ruby: longest_slide_down) that takes a pyramid representation 
# as argument and returns its' longest 'slide down'. For example,
#
# longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
# # => 23
#
pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ]

# Solve with recursive Tree
class Tree(object):
    def __init__(self, pyr, start, level):
        if level < len(pyr):
            if start < len(pyr[level]):
                self.left = Tree(pyr, start, level+1)
                self.right = Tree(pyr, start+1, level+1)
                
                if self.left.value >= self.right.value:
                    self.value = pyr[level][start] + self.left.value
                else:
                    self.value = pyr[level][start] + self.right.value
        else:
            self.value = 0
pyrTree = Tree(pyramid, 0, 0)
print(pyrTree.value)

# Below both work better with very large pyramids

#solve with simple addition iteration from bottom 

def longSlide(pyramid):
    for x in range(len(pyramid) - 2, -1, -1):
        print(x)
        for y in range(len(pyramid[x])):
            if pyramid[x+1][y] >= pyramid[x+1][y+1]:
                pyramid[x][y] = int(pyramid[x][y]) + int(pyramid[x+1][y])
            else:
                pyramid[x][y] = int(pyramid[x][y]) + int(pyramid[x+1][y+1])
    print(pyramid)
longSlide(pyramid)

# solve with recursion and cache

def longSlide(pyramid):
    maxlevel = len(pyramid) - 1
    cache = {}
    def recur(pyramid, y, level):
        if level < maxlevel:
            if '{},{}'.format(y, level) not in cache:
                cache['{},{}'.format(y, level)] = max([recur(pyramid, y, level+1), recur(pyramid, y+1, level+1)])
            return pyramid[level][y] + cache['{},{}'.format(y, level)]
        else:
            return pyramid[level][y]
    
    return recur(pyramid, 0, 0)
    
    
print(longSlide(pyramid))
