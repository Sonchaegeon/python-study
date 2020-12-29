#1
a_tuple = ("키움증권", "대신증권", "네이버증권")
print(type(a_tuple))

a_len = len(a_tuple)
print(a_len)


# a_tuple[0] == 키움증권
for value in a_tuple:
    print(value)

for index, value in enumerate(a_tuple):
        print(index)
        print(value)
