# 주가 데이터
# prices = []

# for i in range(0,10):
#     test= int(input("데이터 기입:"))
#     prices.append(test)

prices= [int(input("데이터 기입:")) for i in range(0,10)]

# 3일 이동 평균 계산
window = 3 
# moving_avg = []
# for i in range(len(prices) - window + 1):
#     window_data = prices[i:i+window]
#     avg = round(sum(window_data) / window, 2)
#     moving_avg.append(avg)
    
# print(f"원본 데이터: {prices}")
# print(f"{window}일 이동 평균: {moving_avg}")

# 리스트 컴프리헨션으로
moving_avg_short = [round(sum(prices[i:i+window])/window,3)
                    for i in range(len(prices)-window+1)]
print(f"간단한 방법: {moving_avg_short}")

# 상승/하락 추세 판단
# trends = []
# for i in range(1, len(moving_avg)):
#     if moving_avg[i] > moving_avg[i-1]:
#         trends.append("상승")
#     elif moving_avg[i] < moving_avg[i-1]:
#         trends.append("하락")
#     else:
#         trends.append("보합")
# print(f"추세: {trends}")
mas = moving_avg_short
trends_short = ["상승" if mas[i] > mas[i-1] 
                else "하락" if mas[i] < mas[i-1]
                else "보합"
                for i in range(1, len(mas))]
print(f"간단한 방법 추세: {trends_short}")
                