# filename: zodiac,constellation.

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

constellation_name = (u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
	u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座', u'摩羯座')

constellation_days = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22),
	(7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22))

dict_zodiac = {}
for key in range(len(chinese_zodiac)):
    dict_zodiac[chinese_zodiac[key]] = 0


dict_constellation = {}
for key in range(len(constellation_name)):
    dict_constellation[constellation_name[key]] = 0


while True:
    years = int(input("please your input brithday's years: "))
    month = int(input("please your input brithday's month: "))
    days = int(input("please your input brithday's days: "))


    zodiac = chinese_zodiac[years%12]
    n = 0
    while constellation_days[n] <= (month, days):
        if month == 12 and days >= 23:
            break
        n += 1

    print("Your zodiac is: ", zodiac)
    print(constellation_name[n-1])

    dict_zodiac[zodiac] += 1
    dict_constellation[constellation_name[n-1]] += 1

    for name in dict_zodiac.keys():
        print("%s include %d nums." %(name, dict_zodiac[name]))

    for name in dict_constellation.keys():
        print("%s include %d nums." %(name, dict_constellation[name]))
