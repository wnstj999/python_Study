a = 15
b = 27
c = 191
# if a > b and a > c:
#     print(f"{a}가 가장 큽니다.")
# elif b > a and b > c:
#     print(f"{b}가 가장 큽니다.")
# else:
#     print(f"{c}가 가장 큽니다.")

# print(f"{a if a > b and a > c else b if b > c and b > a else c}가 가장 큽니다.")


largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print(f"{largest}가 가장 큽니다.")
