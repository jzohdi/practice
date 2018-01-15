#
#
# Calling function KaprekarsConstant('####') returns the number of steps it takes to reach '6174' through Kaprekars routine
# the method follows: for input (some int, or str of integers), arrange the number once in ascending order,
# again in descending order, subract the latter from the former, and repeat this routine until reaching '6174'.
# 
# Here sorting functions bigSort(num) and smallSort(num) return the two sorted values.
#
# Function getnum() within KaprekarsConstant() recursively calls itself until number '6174' and returns the count
#


def bigSort(num):

    first = []
    # if num is not a string (ei. '1112') and instead input is an integer
    # add the next line
    # num = str(num)
    for i in range(len(num)):
        if len(first) == 0:
            first.append(num[i])
        else:
            for number in range(len(first)):
                if first[number] < num[i]:
                    first.insert(number, num[i])
                    break
                elif first[number] == num[i]:
                    first.insert(number, num[i])
                    break
                if all(x > num[i] for x in first):
                    first.insert(len(first), num[i])
                    break

    newnum = ''.join(first)

    return newnum

def smallSort(num):

    second = []
    for i in range(len(num)):
        if len(second) == 0:
            second.append(num[i])
        else:
            for index in range(len(second)):
                if second[index] > num[i]:
                    second.insert(index, num[i])
                    break
                elif second[index] == num[i]:
                    second.insert(index, num[i])
                    break
                if all(y < num[i] for y in second):
                    second.insert(len(second), num[i])
                    break

    newnum = ''.join(second)

    return newnum

def KaprekarsConstant(num):

    print(num);

    count = 0;

    def getnum(num, count):

        count += 1;

        x = bigSort(num)
        y = smallSort(num)
        num = str(int(x) - int(y))

        # this piece stops the function from looping too long if something goes wrong
        if count > 50:
            return False
        if num != '6174':
            return getnum(num, count)
        else:
            print(count)

    getnum(num, count)

