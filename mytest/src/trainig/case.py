#coding=utf-8

list = []
list4 = []
list1 = ['physics', 'chemistry', 'haha']
list2 = ['fe', 'feg' , 'fafa']
list3 = ['ert', 'feg', 'feaf']
list.append(list1)
# list.append(list2)
# list.append(list3)
length = len(list)
if length == 1:
    print list[0],list[1],list[2]
else:
    for i in range(0, len(list)):
        temp = list[i]
        print temp[0],temp[1],temp[2]
