# sum = 0
# for i in range(1,101):
#     if i % 2 ==0:
#         sum += i
# print(sum)
# print(f"((sum for i in range(1, 101)) if i % 2 == 0 sum += i)")

print(sum(i for i in range(1, 101) if i % 2 == 0))

