# 학생별 과목 점수
students = {
    "김철수": {"math": 85, "english": 90, "science": 88},
    "이영희": {"math": 92, "english": 98, "science": 95},
    "박민수": {"math": 78, "english": 85, "science": 82}
}

# 수학과 영어 1등 
print("=== 수학과 영어 1등 ===")
subjects = {"math", "english", "science"}
for test in subjects:
    if( )

    for name, scores in students.items():
    if (
        scores["math"] == max(s["math"] for s in students.values()) and
        scores["english"] == max(s["english"] for s in students.values())
    ):
        print(f"{name}이(가) 수학과 영어 모두 1등입니다!")