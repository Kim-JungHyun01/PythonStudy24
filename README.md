# PythonStudy24
Python AI 기초학습과정 2024

mbc 아카데미 컴퓨터교육센터 수원점

AI 기초학습으로 파이썬 학습 진행용

파이썬 버전 : 3.11.2

사용도구
- 파이참
- GitKraken
- Colab
- Visualize : https://jgirl.ddns.net/VisualCode/visualize.html#mode=display

학습교재
1. 점프 투 파이썬 :  https://wikidocs.net/book/1
2. Colab단축키 : https://surfonmedia.tistory.com/1

```
#예제
#관리자가 커피 가격과 커피명을 정하고 개수입력
#소비자가 커리를 구매하는데 잔돈이 나와야함
#판매 종료 후 관리자가 커피 판매한 총액을 파악할수 있어여함

coffee = ["", 0, 0] #커피명/ 갯수/ 가격
result = ["", 0, 0] #총 판매 / 갯수/ 가격
money = 0           #투입된 금액

guest_menu = """
==============
커피 자판기
==============
1. 돈투입
2. 커피구매
3. 이용 종료
==============
"""

#관리자모드 :  100
admin_menu = """
================
관리자 모드
================
101. 메뉴관리
102. 판매관리
999. 관리자모드 종료
"""

#커피 상태 출력
def print_coffee(list):
    print("-------------------------------------------------------")
    print("커피 명 : %s | 갯수 : %d개 | 가격 : %d원" % (list[0], list[1], list[2]))
    print("-------------------------------------------------------")

# 거스름돈 계산
def output_money(money):
    print("거스름돈은 총 %d원입니다." % money)
    money_list = [500, 100, 50, 10]
    for i in money_list:
        if money // i != 0:
            print("%d원 : %d개" % (i, money // i))
        money %= i

input_menu = 100 #관리자모드 바로 진입
while True:
    if input_menu == 1:
        print("================\n돈투입\n================")
        print("현재 투입된 돈은 총 %d원입니다." % money)
        money += int(input("돈을 투입하세요 : "))
        print("총 투입된 금액은 총 %d원입니다." % money)

    elif input_menu == 2:
        print("================\n커피구매\n================")
        input_coffee = int(input("커피구매 갯수 입력 : "))
        
        # 커피재고 부족시
        if coffee[1] < input_coffee:
            print("커피가 부족합니다.")

        # 투입금액 부족시
        elif money < (coffee[2]* input_coffee):
            lack_money = coffee[2]* input_coffee - money
            print("%d원이 부족합니다." % lack_money)

        else:
            check = int(input("%d개 구매가 맞습니까?(1 : yes, 0: no) : " % input_coffee))
            if check == 1:
                print("구매가 완료되었습니다.")
                #판매 갯수 & 금액 계산
                coffee[1] -= input_coffee
                result[1] += input_coffee
                money -= (coffee[2]* input_coffee)
                result[2] += coffee[2]* input_coffee
                print("총 구매액은 %d입니다. 잔액은 총 %d원입니다." % (coffee[2]* input_coffee, money))
            else:
                print("구매가 취소되었습니다.")

    elif input_menu == 3:
        output_money(money)
        print("프로그램 종료")
        break

    elif input_menu == 100:
        while True:
            print(admin_menu)
            input_menu = int(input("관리자 메뉴입력 : "))
            if input_menu == 101:
                print("================\n메뉴관리\n================")
                while True:
                    if coffee[0] == "" or coffee[1] == 0:
                        coffee[0] = input("커피명 입력 : ")
                        coffee[1] = int(input("커피 갯수 입력 : "))
                        coffee[2] = int(input("커피 가격 입력 : "))
                        print_coffee(coffee)
                        check = int(input("위의 내용이 맞습니까?(1 : yes, 0: no, 99: 취소) : "))
                        if check == 1:
                            result[0] = coffee[0]
                            print("저장되었습니다.")
                            break;
                        elif check == 99:
                            print("취소되었습니다.")
                            break;
                        else:
                            print("다시 입력해주세요.")
                    else:
                        print("이미 커피가 등록되어 있습니다.")
                        print_coffee(coffee)
                        break;

            elif input_menu == 102:
                print("================\n판매관리\n================")
                print_coffee(result)

            elif input_menu == 999:
                print("관리자모드 종료")
                input_menu=0
                break

            else:
                print("잘못된 숫자입니다.")
    else:
        print("잘못된 숫자입니다.")

    print(guest_menu)
    print_coffee(coffee)
    input_menu = int(input("메뉴입력 : "))
```
