# filename: zodiac
# Author: bavdu
# Date: 2019/04/02
# Usage: get user zodiac.

zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

years = int(input("please input your brithday (example: 2020, only input year.):"))
print("Your zodiac is: %s" %zodiac[years%len(zodiac)])