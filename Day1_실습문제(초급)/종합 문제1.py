## 종합 문제 1: 성적 처리 프로그램

#학생들의 점수를 입력받아 다음을 출력하는 프로그램을 만드세요:
# - 총점
# - 평균
# - 최고점
# - 최저점
# - 평균 이상인 학생 수

students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88,
    "최동욱": 95}

print(f"총점: {sum(students.values())}점\n"
      f"평균: {sum(students.values()) / len(students)}점\n"
      f"최고점: {max(students.values())}점\n"
      f"최저점ㅋㅋ: {min(students.values())}점\n"
      f"평균 이상인 학생 수: {sum(1 for s in students.values() if s >= sum(students.values()) / len(students))}명"
      )
    
