import time

t0 = time.time()
for i in range(100):
    file = open("1.txt", encoding="utf8")
    file2 = open("2.txt", "w", encoding="utf8")
    b = file.read()
    s = b.rfind("col")+3       #ищем индекс цифры последнего col
    j = str(b[s])              #ищем саму цифру последнего col

    file2.write("{\n"+"    \"root\""+":\n"+"    {\n"+"        \"rows\""+": [\n"+"        {\n")

    b = b.replace("&lt;", "<")
    b = b.replace("&gt;", ">")
    b = b.replace("&quot;", "\\\"")
    a = []                     #записываем индексы открывающих col
    a1 = []                    #записываем индексы закрывающих col

    for i in range(len(b)):                                              #заполнение a
        if b[i]=='<' and b[i+1]=='c' and b[i+2]=='o' and b[i+3]=='l':
            a.append(i)
    for i in range(len(b)):                                              #заполнение a1
        if b[i]=='<' and b[i+1]=='/' and b[i+2]=='c' and b[i+3]=='o':
            a1.append(i)


    k1, k2 = 0, 0
    for i in range(10):             #(10) потому что всего 10 блоков
        l = 0                       #на каком col мы находимся (после последнего col нет запятой)
        for k in range(1, 6):       #пять блоков
            l+=1
            n = (str(k))            #цифра col в строчном формате
            x = b[a[k1]:a1[k2]]     #строка с которой работаем
            if l!=int(j):
                if "<col"+n+">" in x:
                    x = x.replace("<col"+n+">", "         \"col"+n+"\": "+"\"", 1)
                    x = x.replace("</col"+n+">\n", ",", 1)
                    x = x.encode('unicode-escape').decode('utf-8')
                    x = x.replace("\\\\\"", "\\\"")                      #заменяет \\" на \"
                    file2.write("   "+x+"\",\n")

            else:
                x = x.replace("<col" + n + ">", "         \"col" + n + "\": " + "\"", 1)
                x = x.replace("</col" + n + ">\n", "", 1)
                x = x.encode('unicode-escape').decode('utf-8')
                x = x.replace("\\\\\"", "\\\"")
                file2.write("   "+x+"\"\n")
                if i!=9:                           #т.е. последняя строчка последнего блока
                    file2.write("		},\n		{\n")
            k1 = k1+1
            k2 = k2+1

        file2.write("		}]\n	}\n}")

    file.close()
    file2.close()
t1 = time.time() - t0
print("Time elapsed: ", t1)







