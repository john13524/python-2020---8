import os.path
a = {}
if not os.path.isfile('md.txt'):
    of = open('md.txt','w')
    print('new file')
else:
    of = open('md.txt','r')
    print('old file')
for row in of.readlines():
    date = row.split(':')
    key = date[0]
    value = date[1]
    value = value.split()
    a[key]=value
print(a)
     
    
    

    
    
while True:
    print('1.建立字串')
    print("2.打出全部資料")
    print('3.英翻中')
    print('4.中翻英')
    print('5.考試')
    print('6.離開')
    b = input('輸入功能:')
    if b =='1':
        d = input('輸入中文:')
        c = input('輸入英文:')
        a[c]=d
        fo = open('md.txt','w')
        for k,v in d.items():
            of.write(k)
            of.write(':')
            of.write(v)
            of.write('\n')
    elif b =="2":
        for k,v in a.items():
            print(k,':',v)
    elif b == '3':
        f = input('輸入想翻譯的英文:')
        print(a[f])
    elif b == '4':
        f = input('輸入想翻譯的中文:')
        for k,v in a.items():
            if f == v:
                print(k)
    elif b == '5':
        F = 0
        for k,v in a.items():
            print(v,':')
            A = input('輸入答案')
            if A ==k:
                F = F + 1
                print('對')
        print('你的分數',F)
    elif b == '6':
        print('下班耶')
        print('看3小')
        print('error')
        for i in range(100000):
            print("errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror")
        break