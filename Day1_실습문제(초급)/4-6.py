## 문제 4-6: 평균을 구하는 함수

#점수 리스트의 평균을 구하는 함수를 만드세요.

def avg_score(scores):
    return sum(scores) / len(scores)

print(avg_score([90, 80, 70, 60, 100]))  # 80.0