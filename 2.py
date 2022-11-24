import re
import time

t0 = time.time()
for i in range(100):
    file = open("1.txt", encoding="utf8")
    file2 = open("2.txt", "w", encoding="utf8")
    b = file.read()
    s = re.findall("col[1-9]", b)
    s = str(s[-1])
    s = int(s[-1])
    j = str(s)

    file2.write("{\n"+"    \"root\""+":\n"+"    {\n"+"        \"rows\""+": [\n"+"        {\n")

    b = re.sub("&lt;", "<", b)
    b = re.sub("&gt;", ">", b)
    b = re.sub("&quot;", "\\\"", b)
    a = []
    a1 = []

    for i in range(len(b)):
        if b[i]=='<' and b[i+1]=='c' and b[i+2]=='o' and b[i+3]=='l':
            a.append(i)
    for i in range(len(b)):
        if b[i]=='<' and b[i+1]=='/' and b[i+2]=='c' and b[i+3]=='o':
            a1.append(i)


    k1, k2 = 0, 0
    for i in range(10):
        l = 0
        for k in range(1, 6):
            l+=1
            n = (str(k))
            x = b[a[k1]:a1[k2]]
            if l!=int(j):
                if "<col"+n+">" in x:
                    x = re.sub("<col"+n+">", "         \"col"+n+"\": "+"\"", x, 1)
                    x = re.sub("</col"+n+">\n", ",", x, 1)
                    x = x.encode('unicode-escape').decode('utf-8')
                    x = re.sub("\\\\\"", "\\\"", x)
                    file2.write("   "+x+"\",\n")

            else:
                x = re.sub("<col" + n + ">", "         \"col" + n + "\": " + "\"", x, 1)
                x = re.sub("</col" + n + ">\n", "", x, 1)
                x = x.encode('unicode-escape').decode('utf-8')
                x = re.sub("\\\\\"", "\\\"", x)
                file2.write("   "+x+"\"\n")
                if i!=9:
                    file2.write("		},\n		{\n")
            k1 = k1+1
            k2 = k2+1

    file2.write("		}]\n	}\n}")

    file.close()
    file2.close()
t1 = time.time() - t0
print("Time elapsed: ", t1)

