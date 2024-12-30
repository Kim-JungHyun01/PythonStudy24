#중복적인 메서드 저장공간
import datetime as t

#날짜 가공
def pro_date():
    now = t.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    year = str(year)

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    return year, month, day
#option.pro_date() end

#숫자 입력 try
def input_int(text):
    while True:
        try:
            num = int(input(text))
            return num
        except ValueError:
            print("숫자를 입력해주세요.")
#option.input_int() end

#
