# if 문

stock_name = "키움증권"
if stock_name == "키움증권":
    print("키움 증권입니다")
elif stock_name == "카카오증권":
    print("카카오증권입니다")
else:
    print("위에 조건들이 맞지 않습니다~")

stock_price = 3000
if stock_price < 2000:
    print("2000보다 작습니다")
elif stock_price <= 3000:
    print("3000보다 같거나 작네요")

stock_rate = 2.5
if stock_rate > 2.5:
    print("2.5보다 크네요")
elif stock_rate >= 2.5:
    print("2.5이상입니다")

# or
if stock_name == "키움증권" or stock_name == "대신증권":
    print("키움증권 또는 대신증권이네요!")

elif stock_name == "카카오증권" or stock_name == "KB증권":
    print("카카오증권 또는 KB증권")

# and
if stock_price == 3000 and stock_name == "대신증권":
    print("대신증권 3000")

elif stock_price == 3000 and stock_name == "키움증권":
    print("키움증권 3000")

# in
stock_name = "삼성전자"
if stock_name in ["LG전자", "대한과학", "삼성전자"]:
    print("리스트에 삼성전자가 있습니다!")