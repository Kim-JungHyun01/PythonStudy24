import random
from option import input_int
#lotto : 수동, 자동

#main(구매갯수) : 수동, 자동선택
def main(count):
    print("="*30)
    while True:
        print("=" * 30)
        s_num = input("1. 수동 \n2. 자동\n : ")

        if s_num == '1': #수동
            print("=" * 30)
            for i in range(count):
                lotto_num = manual()
                print("로또 번호 : ", lotto_num)
            break

        elif s_num == '2':#자동
            print("=" * 30)
            for i in range(count):
                lotto_num = auto()
                print("로또 번호 : ", lotto_num)
            break

        else:
            print("=" * 30)
            print("다시 입력하세요")
            print("=" * 30, end="\n")
        print("=" * 30, end="\n")
#lotto.main() end

#수동
def manual():
    while True:
        num1 = input_int("첫번째 수 : ")
        num2 = input_int("두번째 수 : ")
        num3 = input_int("세번째 수 : ")
        num4 = input_int("네번째 수 : ")
        num5 = input_int("다섯번째 수 : ")
        num6 = input_int("여섯번째 수 : ")
        print("=" * 30, end="\n")

        manual = [num1, num2, num3, num4, num5, num6]

        dupli = check(manual)
        
        #중복확인
        if dupli == False:
            print("\n중복값이 있습니다. 다시 입력하세요\n")
            print("="*30,end="\n")
            continue
        else:
            manual.sort() #정렬
        
        #정렬 후 숫자 45이상인것 확인
        if manual[-1] > 45:
            print("\n45 이하 의 숫자로 다시 입력하세요\n")
            print("="*30,end="\n")
            continue
        else:
            break

    return manual
#lotto.manual() end

#자동
def auto():
    while True:
        num1 = random.randrange(1,45)
        num2 = random.randrange(1,45)
        num3 = random.randrange(1,45)
        num4 = random.randrange(1,45)
        num5 = random.randrange(1,45)
        num6 = random.randrange(1,45)

        auto = [num1, num2, num3, num4, num5, num6]
        
        #중복확인
        dupli = check(auto)

        if not dupli: #False을 경우
            continue
        else:
            auto.sort()
            break

    return auto
#lotto.auto() end

#중복 확인
def check(lotto_num):
    i = 0
    dupli = True #중복여부

    while i<45:
        #중복 수 찾기
        if lotto_num.count(i)<2:
            i += 1
            continue
        else:
            dupli = False
            break
            
    return dupli
#lotto.check() end