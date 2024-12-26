#매출관리
import option

#년도 월별 매출 파일 읽어서 반환
def month_margin(year, month):
    f = open("관리/" + year + "/" + month + "-total.txt","r")
    tmp_dic = {}
    tmp_month = {}

    while True:
        line = f.readline()
        if line == '':
            break
        line = line.rstrip('\n')
        tmp_list = line.split('/')
        tmp_month[tmp_list[0]] = int(tmp_list[1])

    tmp_dic[month] = tmp_month

    return tmp_dic
#management.month_margin() end

#매출관리 main()
def main(goods, day_sale):
    #현재 달, 날짜
    year, month, day = option.pro_date()

    #메뉴출력
    while True:
        print("=" * 30)
        s_num = option.input_int("1. 일 매출 / 2. 월 매출 / 5. 종료 : ")
        print("=" * 30, end="\n")

        
        #일매출
        if s_num == 1:
            print("일매출")
            print("=" * 30)
            for i in day_sale.keys():
                if i == "card" or i == "cash":
                    continue
                else:
                    print("{}. {} : {}".format(i,goods[i]['품목'],day_sale[i]))

            print("=" * 30, end="\n")
            print("{} : {}\n{} : {}\n".format('card', day_sale['card'], 'cash', day_sale['cash']))
            print("=" * 30, end="\n")
            print()

        #월 매출
        elif s_num == 2:
            dic = month_margin(year,month)
            tmp_dic = dic[month]
            print("월매출")
            print("=" * 30)
            for i in tmp_dic.keys():
                if i == "card" or i == "cash":
                    continue
                else:
                    print("{}. {} : {}".format(i, goods[i]["품목"], tmp_dic[i]))

            print("=" * 30, end="\n")
            print("{} : {}\n{} : {}\n".format('card', tmp_dic['card'], 'cash', tmp_dic['cash']))
            print("=" * 30, end="\n")
            print()

        elif s_num == 5:
            break

        else:
            print("=" * 30)
            print("다시 입력하세요")
            print("=" * 30, end="\n")
            print()
#management.main() end