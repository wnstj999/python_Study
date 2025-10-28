
try:
# 물건 가격 계산
    price = 65000
    quantifty = 4
    total = price * quantifty
    print(f"총 가격: {total}원")

# 거스름돈 계산
    payment =int(input("지불한 금액을 입력하세요: "))
    change = payment - total
    if change > 0:
        print(f"거스름돈: {change}원")
    else:
        print("금액이 부족합니다.")

except ValueError:
        print("숫자가 아닙니다!")