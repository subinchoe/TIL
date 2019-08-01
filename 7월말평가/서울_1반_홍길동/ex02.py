# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """

    numbers = equation.split('+')
    # print(numbers)

    result = ''
    for number in numbers:
        num = list(map(int, number))
        if type(num) == int:
            result += num
        else:
            pass
        # if '-' in number:
        #     pass
        # else:
        #     result += number
        # items = list(map(int, result))
    return num

    # for item in minus:
    #     if '+' in item:
    #         pass
    #     else:
    #         result += item
        
    # return result

    # wow = list(map(int, equation))
    # print(wow)
    # if '+' in plus:
    # for num in numbers:
    #     print(num)
        



# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))