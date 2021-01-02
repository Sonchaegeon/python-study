a_dict = {"종목명": "삼성전자", "등락율(%)": 0.0, "고가대비(%)": -0.97,
          "보유수량": 7, "현재가": 80000}

print(type(a_dict))
print(len(a_dict))
print("키 %s, 값: %s" % ('종목명', a_dict.get('종목명')))
print("키 %s, 값: %s" % ('종목명', a_dict['종목명']))

# for key in a_dict.keys():
#     print(key)
#     print(a_dict[key])

for key, value in a_dict.items():
    print("키: %s, 값: %s" % (key, value))

a_dict.update({'종목명': '삼성전자우'})
a_dict.update({'보유수량': 6, '현재가': 74000})
a_dict.update({'없는키': 123})
print(a_dict)
