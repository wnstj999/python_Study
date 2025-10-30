## 종합 문제 2: 간단한 메뉴 시스템

#다음과 같은 메뉴 시스템을 만드세요:

menu = {
    "1": "회원가입",
    "2": "로그인",
    "3": "종료"}
# 메뉴 출력
for key, value in menu.items():
    print(f"{key}. {value}")
cho = str(input("번호선택= "))
if cho == "1":
    print("회원가입")
elif cho == "2":
    print("로그인")
elif cho == "3":
    print("종료")
else:
    print("마 숫자 제대로 쳐라")
# 사용자 선택 (여기서는 하드코딩)choice = "2"# 선택에 따른 메시지 출력# 여기에 코드 작성