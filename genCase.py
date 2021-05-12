para = []
txt = input("Press enter to end input: ")
while txt != "":
    para.append(txt)
    txt = input("Press enter to end input: ")

result = []
for p in para:
    while p != "":
        line = p[0] + " O\n"
        p = p[1:]
        result.append(line)
    result.append("\n")

with open("data/customTest/test.txt", 'w') as f:
    for line in result:
        f.write(line)