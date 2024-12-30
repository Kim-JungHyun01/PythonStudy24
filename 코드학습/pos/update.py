#일 매출 & 재고 정보

def main(goods,guest_log,day_sale):
    guest_dic = guest_log["판매"]
    guest_dic_key = list(guest_dic.keys())
    
    #일매출입력
    for i in list(day_sale.keys()):
        if i not in guest_dic_key:
            continue

        day_sale[i] = guest_dic[i] * goods[i]['가격']
        goods[i]['재고'] -= guest_dic[i]
        
        #금액입력
        if guest_log['결제'] == 'cash':
            day_sale["cash"] += guest_log["판매금액"]

        elif guest_log['결제'] == 'card':
            day_sale["card"] += guest_log["판매금액"]
# update.main() end