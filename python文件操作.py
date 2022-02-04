f=open("shotgun.txt","r+")    #"r" ,"w" , "a",  "r+" , "w+" , "a+" ，"rb" , "wb"

f.seek(2,0)                    #从文件开头位置移动文件指针到第2字节位置           #0是开头，1是当前位置   ，2是末尾

print(f.tell())              #打印文件指针位置

aa=f.read()               #读文件所有内容
bb=f.read(3)             #读取当前指针到第3个字符的单个字符，并移动指针到这个位置
cc=f.readline()          #读取单行，并移动指针到这个位置
dd=f.readlines()        #读文件所有内容,按照换行符分割没一行，比存入一个列表
if (f.readlines()):
    for i in f:
          print(i,end="")     #f是一个迭代器

if (f.writable):   #判断f是否可写入内容
    f.write("aaaaaaa")    #把字符串写入文件

f.flush()   #刷新缓冲区

f.close()  #关闭文件，释放内存

