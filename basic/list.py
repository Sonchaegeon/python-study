a_list = ["키움증권", "대신증권", "카카오증권"]
b_list = ["구글", "페이스북", "애플"]

a_list.append("카카오")
print(a_list)

del a_list[0]
print(a_list)

for index, value in enumerate(a_list):
    print("%s - %s" % (index, value))

for value in b_list:
    a_list.append(value)

print(a_list)