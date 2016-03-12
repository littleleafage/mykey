#coding=utf-8

class Verifi(object):

    def veri(self):
        a = 0
        result = []
        for j in range(1, 25, 1):  # (1, 100000, 1)
            a += 1
            list = str(a).zfill(6)  # 返回指定长度的字符串，原字符串右对齐，前面填充0
            result.append(list)
        print result
