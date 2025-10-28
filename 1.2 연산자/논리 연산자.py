a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# 실전 예시

age = 5
has_license = True
can_drive = age >= 18 and has_license
print(f"운전 가능 여부: {can_drive}")  # 운전 가능 여부