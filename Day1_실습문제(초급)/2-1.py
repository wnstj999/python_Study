#리스트 생성과 접근

numbers = [int(input(" 숫자 10개 기입 :")) for i in range(10)]
print(f"첫번째 요소: {numbers[0]}\n"
      f"마지막 요소: {numbers[-1]}\n"
      f"처음 5개 요소: {numbers[:5]}")
