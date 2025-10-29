text = "python is great python is fun python is powerful fun fun zen zen zen"

# 단어 분리
words = text.split() # 단어 띄어쓰기 하나하나 다  words에 저장

print(words)

# 빈도수 계산
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1    
    else:
        word_count[word] = 1
        
print("단어 빈도수:")

# for word, count in word_count.items():
#     print(f"{word}: {count}번")
    
# 가장 많이 나온 단어
# max_word = max(word_count, key=word_count.get)
max_word = max(word_count)
print(max_word)
# print(f"\n가장 많이 나온 단어: {max_word} ({word_count[max_word]}번)")

