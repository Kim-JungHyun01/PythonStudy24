#결과를 텍스트로 저장
from os import write

import management
import option
import os.path


#현 재고 상황 저장
def re_stock(goods):
    f = open("재고/goods.txt", "w")   #새로 쓰기

    for i in goods.keys():
        f.write("{}/{}/{}/{}/{}\n".format(i, goods[i]['분류'], goods[i]['품목'], goods[i]['가격'], goods[i]['재고']))

    f.close()#파일 닫기
#ep.re_stock end

#일매출 저장
def make_day_sale(year,month,day, day_sale):
    f = open("관리/"+year+"/"+month+day+".txt", "w")

    for i in day_sale.keys():
        f.write("{}/{}\n".format(i, day_sale[i]))

    f.close()
#ep.make_day_sale end

#월매출파일여부확인
def make_month_file(year, month, goods):
    file = "관리/" + year + "/" + month + "-total.txt"
    if not os.path.exists(file):
        f = open(file, "wt") #빈파일 생성
        for i in goods.keys():
            f.write("{}/{}\n".format(i,0))
        f.write("{}/{}\n".format("card",0))
        f.write("{}/{}\n".format("cash", 0))
        f.close()

#월매출 저장
def make_month_sale(year,month,day_sale):
    tmp_dic = management.month_margin(year,month) #기존 월매출읽기
    month_sale = tmp_dic[month]
    f_dic = {}

    for i in month_sale.keys():
        total = month_sale[i] + day_sale[i]
        f_dic[i] = total

    f = open("관리/"+year+"/"+month+"-total.txt", "w")

    for i in f_dic.keys() :
        f.write("{}/{}\n".format(i,f_dic[i]))

    f.close()

#ep.make_month_sale end

#매출 저장 main
def main(goods, day_sale):
    year, month, day = option.pro_date()
    
    #텍스트 저장
    re_stock(goods) #재고 저장
    make_month_file(year, month, goods)
    make_day_sale(year,month,day, day_sale)  #일매출 저장
    make_month_sale(year,month,day_sale)     #월매출 저장
#ep.main() end