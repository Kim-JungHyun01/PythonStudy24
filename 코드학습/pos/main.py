import pay
import update
import gmanagement
import management
import ep

# 자판기
# 재고 및 물품정보 텍스트파일 읽기
f = open("재고/goods.txt","rt")

# goods.txt 내용 저장
# 물품 정보 및 재고 저장
goods = {}
#일 매출 정보 저장
day_sale = {"card" : 0, "cash" : 0}

while(True):
    tmp_dic = {}#임시 딕셔너리
    line = f.readline() #한줄씩 읽기
    line = line.rstrip("\n") #띄어쓰기기준

    #내용이 없으면 종료
    if(line == ""):
        break

    st_list = line.split("/") #/기준으로 내용나눔

    #물품 : 분류, 품목, 가격(int), 재고(int) 로 구분
    tmp_dic["분류"] = st_list[1]
    tmp_dic["품목"] = st_list[2]
    tmp_dic["가격"] = int(st_list[3])
    tmp_dic["재고"] = int(st_list[4])
    
    #물품번호 = tmp_dic의 key
    goods[st_list[0]] = tmp_dic
    day_sale[st_list[0]] = 0

#main 실행문
while True:
    #메뉴
    print("="*30)
    print("1. 결제 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
    print("=" * 30, end="\n")
    
    #숫자 예외처리 없애기 위한 int제외
    select_num = input('선택 : ')
    
    #결제
    if select_num == '1':
        tmp = pay.main(goods)
        update.main(goods,tmp,day_sale)

    # 물품관리
    elif select_num == '2':
        gmanagement.main(goods)

    #매출관리
    elif select_num == '3':
        management.main(goods,day_sale)

    #종료
    elif select_num == '9':
        ep.main(goods,day_sale)
        break
    else:
        print("잘못된 입력입니다.\n")

print("프로그램 종료")


