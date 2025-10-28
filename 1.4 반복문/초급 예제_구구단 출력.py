dan = int(input("단을 입력하세요: "))

for dan in range(dan , 10):
    print(f"=={dan}단==")
    for i in range(1,10):
        print(f"{dan} x " f"{i}= " f"{dan*i}")
