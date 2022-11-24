import time
import xmltodict
import json

t0 = time.time()
for i in range(100):
    file3 = open("3.txt", "w", encoding="utf8")
    with open("1.txt", encoding="utf8") as file:
        doc = xmltodict.parse(file.read())
        b = json.dumps(doc)

    b = b.replace("\",", "\",\n           ")
    b = b.replace("}, {", "\n        },\n        {\n            ")
    b = b.replace("{\"root\": {\"data\": {\"root\": {\"rows\": [{",
                  "{\n" + "    \"root\"" + ":\n" + "    {\n" + "        \"rows\"" + ": [\n" + "        {\n            ")
    b = b.replace("}]}}}}", "\n		}]\n	}\n}")
    b = b.replace(", \"", ",\n            \"")
    file3.write(b)

    file3.close()
    file.close()

t1 = time.time() - t0
print("Time elapsed: ", t1)