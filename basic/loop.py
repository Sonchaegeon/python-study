# for
for i in range(0, 5): # [0, 1, 2, 3, 4]
    print(i)

for i in ['키움', '삼성', '카카오']:
    print(i)

for i, value in enumerate(['키움', '삼성', '카카오']):
    print("%s %s" % (i, value))

# while
cnt = 0
repeat_boolean = True
while repeat_boolean:
    cnt += 1
    print(cnt)

    if cnt == 100:
        repeat_boolean = False

