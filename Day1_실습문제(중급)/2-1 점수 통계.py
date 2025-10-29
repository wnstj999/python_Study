scores = [85, 92, 78, 90, 88, 76, 95, 89]
total = sum(scores)
average = total / len(scores)
best = max(scores)
worst = min(scores)

print(f"총점: {total}"
      f"\n평균: {average:.2f}"
      f"\n최고점: {best}"
      f"\n최저점: {worst}")