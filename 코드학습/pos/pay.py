#날짜, 시간 패키지
import datetime as t
import lotto
from option import input_int

#고객 성별정보
def choice_gender(guset_log):
    print("=" * 30)
    gender = input("\n성별 입력\n 1.남자 / 2.여자 : ")
    print("=" * 30, end="\n")

    if gender == '1':
        guset_log["gender"] = "man"
    elif gender == '2':
        guset_log["gender"] = "woman"
    else:
        return True

    return False

#고객 나이정보
def choice_age(guest_log) :
    print("="*30)
    print("\n나이 입력\n0. 10대 이전\n1. 10대\n2. 20대\n3. 30대\n4. 40대\n5. 50대\n6. 60대\n7. 60대 이상")
    print("="*30,end="\n")
    age = input("선택 : ")
    print()

    if age == '0':
        guest_log['age'] = 0
    elif age == '1':
        guest_log['age'] = 10
    elif age == '2':
        guest_log['age'] = 20
    elif age == '3':
        guest_log['age'] = 30
    elif age == '4':
        guest_log['age'] = 40
    elif age == '5':
        guest_log['age'] = 50
    elif age == '6':
        guest_log['age'] = 60
    elif age == '7':
        guest_log['age'] = 70
    else :
        return True

    return False

#물품선택 및 수량선택 & 재확인
def select_goods(tmp, goods):
    tmp_list = list(goods.keys()) #물품번호만
    count = 0  # 수량 초기화

    #물품출력
    print("=" * 30)
    for i in tmp_list:
        print("\n{}.\t{}\t/\t금액\t:\t{}".format(i, goods[i]['품목'], goods[i]['가격']))
    print("=" * 30, end="\n")

    s_num = 0
    #상품선택
    while True:
        s_num = input("\n구매상품 번호 : ")
        #상품번호가 있을 경우 break
        if s_num in goods:
            break

    # 수량선택
    while True:
        count = input_int("\n구매상품 수량 : ")
        break


    #상품 10번 : 로또
    if s_num == '10':
        lotto.main(count)


    #구매 재확인
    while True:
        print("=" * 30)
        print("제품 : {} / 수량 : {}".format(goods[s_num]['품목'], count))
        print("=" * 30, end="\n")
        num = input("1. 확인 / 2.취소 : ")
        print("=" * 30, end="\n")

        if num == '1':
            tmp[s_num] = count
            return False
        elif num == '2':
            return True


# 구매하고자 하는 물건, 종류, 수량 선택
def flow_choice(guest_log, goods):
    boolean = True
    service = 0
    tmp_goods = guest_log['판매'] #임시장바구니
    
    while boolean:
        boolean = select_goods(tmp_goods, goods)
    
    guest_log['판매'] = tmp_goods #실제장바구니이동
    
    #물품 추가선택여부
    while True:
        print("=" * 30)
        end_flag = input("1. 다음 / 2. 다른 물품 선택 : ")
        print("=" * 30, end="\n")

        if end_flag =='1':
            return False
        elif end_flag == '2':
            return True #select_goods다시 이동

#영수증 및 장바구니
def calc_cost(tmp_dic, goods):
    total = 0 #총금액계산용
    tmp_list = list(tmp_dic.keys()) #물품번호
    sale_dic = {} #최종 장바구니

    #총금액 계산 & 장바구니출력
    count = 0
    for i in tmp_list:
        tmp = {}
        count += 1
        t = goods[i]['가격'] * tmp_dic[i]
        total += t
        tmp['품목'] = goods[i]['품목']
        tmp['수량'] = tmp_dic[i]
        tmp['총금액'] = t
        sale_dic[count] = tmp

    return sale_dic, total

#영수증 출력
def print_calc(sale_dic,total):
    print()
    print()
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    print()

    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]['품목'], sale_dic[i]['수량'], sale_dic[i]['총금액']))
    print()
    print("=" * 30, end="\n")
    print("\ntotal : {}".format(total))
    print("=" * 30, end="\n")

#결제수단 선택
def select_payment():
    print("=" * 30)
    payment = input("1. 카드 / 2. 현금 : ")
    print("=" * 30, end="\n")
    tmp = 0 #수단선택 초기화

    if payment == '1':
        tmp = 1
    elif payment == '2':
        tmp = 2
    else:
        return True, tmp
    return False, tmp

#결제수단 : 카드시
def select_card(total,guest_log):
    #재확인
    tmp = input("1. 확인 / 2. 취소 : ")
    print("=" * 30, end="\n")

    if tmp == '1':
        print("결제 완료")
        print("=" * 15)
        guest_log["결제"] = "card"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = None #카드이기에 없음
        return False
    elif tmp == '2':
        print("결제 취소")
        print("=" * 15)
        return True
    else:
        print("다시 입력하세요")
        return True


#결제수단 : 현금시
def select_cash(total,guest_log):

    while True:
        tmp = input_int("\n받은 현금 : ")
        lack = total - tmp
        break

    if lack > 0:
        print("=" * 30, end="\n")
        print("받은 현금이 부족하며, 반환되었습니다.")
        print("부족한 금액 : ",lack)
        print("=" * 30, end="\n")
        return True
    else:
        print("=" * 30, end="\n")
        print("\n결제 완료")
        print("=" * 30, end="\n")
        print("잔돈 : {}원".format(abs(lack)))
        print("=" * 30, end="\n")
        guest_log["결제"] = "cash"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = abs(lack)
        return False

#결제수단
def flow_payment(guest_log, goods):
    boolean = True
    select_num = 0 #결제수단선택용
    tmp_goods = guest_log["판매"]
    #총 장바구니, 총금액
    sale_dic, total = calc_cost(tmp_goods, goods)
    
    #결제수단 선택
    while boolean:
        boolean, select_num = select_payment()

    boolean = True #while용 초기화
    print_calc(sale_dic, total)
    if select_num == 1: #카드
        while boolean:
            boolean = select_card(total,guest_log)
    elif select_num == 2: #현금
        while boolean:
            boolean = select_cash(total,guest_log)

    return False

# 결제 main
def  main(goods):
    now = t.datetime.now() #현재시간
    guest_log = {'판매' : {}} #고객정보
    print("=" * 30)
    print(now)
    print("=" * 30, end = "\n")

    #성별
    while choice_gender(guest_log):
        print("\n다시 입력")

    #나이
    while choice_age(guest_log):
        print("\n다시 입력")

    #장바구니 & 물품선택
    while flow_choice(guest_log, goods):
        continue
    
    #결제수단
    while flow_payment(guest_log, goods):
        continue

    #구매시간 일/시간
    now_time = "{}-{}-{}/{}:{}".format(now.year,now.month,now.day,now.hour,now.minute)
    guest_log["일시"] = now_time

    print("=" * 30, end="\n")
    print()

    return(guest_log)
