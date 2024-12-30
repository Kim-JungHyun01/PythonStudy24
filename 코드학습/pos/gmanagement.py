#물품관리

#재고출력
def chk_goods(goods):
    goods_key = list(goods.keys())
    print("=" * 30)
    print("현재 재고 현황 \n")
    print("=" * 30, end="\n")
    
    for i in goods_key:
        print(goods[i]["품목"], " : ", goods[i]["재고"])
    print("=" * 30, end="\n")
#gmanagement.chk_goods end

#발주필요 물품확인(재고부족 : 20개미만, 재고상환 : 150개)
def chk_order(goods):
    goods_key = list(goods.keys())
    count = 0
    order_list = {} #발주필요 목록
    print("=" * 30)

    for i in goods_key:
        # 재고부족 : 20개미만
        if goods[i]["재고"] < 20:
            print(goods[i]["품목"], "의 재고가", goods[i]["재고"], "개 입니다. 발주해주세요.")
            order_list[i] = goods[i]
            count += 1

    # 발주할 것이 없을 때
    if count == 0:
        print("발주할 품목이 없습니다.")
        print("=" * 30)

    else:
        #발주 재확인
        print("=" * 30)
        select = input("1. 발주 / 2. 취소")
        print("=" * 30, end="\n")

        if select == '1':
            for i in list(order_list.keys()):
                if i not in list(goods.keys()):
                    continue
                goods[i]["재고"] = 150
            print("=" * 30)

        elif select == '2':
            print("발주가 취소되었습니다.")

        else:
            print("잘못 입력하셨습니다.")
        print("=" * 30, end="\n")
#gmanagement.chk_order() end

def main(goods):
    while True:
        print("=" * 30)
        select = input("1. 재고확인 \n2. 발주필요품목확인 \n5.종료\n : ")
        print("=" * 30, end="\n")

        if select == '1':
            chk_goods(goods)
        elif select == '2':
            chk_order(goods)
        elif select == '5':
            break
        else:
            print("잘못 입력하셨습니다.")
            print("=" * 30, end="\n")


#gmanagement.main() end
