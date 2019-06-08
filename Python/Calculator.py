def add(num1, num2) :
    return num1 + num2

def minus(num1, num2) :
    return num1 - num2

def multiply(num1, num2) :
    return num1 * num2

def division(num1, num2) :
    return num1 / num2

if __name__ == "__main__" :
    flag = True
    while flag :
        s = input("수식을 띄어서 입력하세요. [ex)1 + 3] 종료를 원하시면 0을 입력하세요.\n")
        num = s.split(' ')
        if len(num) == 3 :
            if num[1] == '+' :
                print('{0} + {1} = {2}'.format(num[0], num[2], add(int(num[0]), int(num[2]))))
            elif num[1] == '-' :
                print('{0} - {1} = {2}'.format(num[0], num[2], minus(int(num[0]), int(num[2]))))
            elif num[1] == '*' :
                print('{0} * {1} = {2}'.format(num[0], num[2], multiply(int(num[0]), int(num[2]))))
            elif num[1] == '/' :
                print('{0} / {1} = {2}'.format(num[0], num[2], division(int(num[0]), int(num[2]))))
            else :
                print('수식을 잘못 입력하였습니다')
        elif s == '0' :
            flag = False
            print('0을 입력하셨습니다. 종료합니다.')
