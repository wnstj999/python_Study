## 문제 2-6: 구구단 리스트로 만들기
## 3단을 리스트로 만드세요.


## for문
# dan= 3
# gugudan = [dan * i for i in range(1, 10)]
# print(f"3단 리스트: {gugudan}")

## 리스트 컴프리헨션
# dan = 3
dan = int(input("단 입력: "))
print(f"{dan}단 리스트: {[dan * i for i in range(1, 10)]}")
