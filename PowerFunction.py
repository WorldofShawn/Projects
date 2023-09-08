def expon(num,pow):
    result = None
    for i in range(pow):
        if result == None:
            result = num
        else:
            result = result*num
    return result

user_num=int(input("Input a number \n"))
user_pow=int(input("input a power \n"))

print(expon(user_num,user_pow))