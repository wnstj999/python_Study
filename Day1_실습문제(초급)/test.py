students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88,
    "최동욱": 95}
total = sum(students.values())
print(f'총점: {total}')
average = total / len(students)
print(f'평균: {average}')
highest_score = max(students.values())
lowest_score = min(students.values())
print(f'최고 점수: {highest_score}')
print(f'최저 점수: {lowest_score}')
count = 0
for name, score in students.items():
    if score >= average:
        count += 1
print(count)