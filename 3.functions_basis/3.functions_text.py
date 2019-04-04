# filename: functions_text.py

def traver(tlist):
    '''
    :usage: 输入一个列表, 然后程序会输出所有列表的元素
    :param tlist: example: list01 = [1, 2, 3, 4, 5]
    :return:list01[x]
    '''
    for i in range(len(tlist)):
        print(tlist[i])

help(traver)