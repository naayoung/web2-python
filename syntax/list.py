s = [1, 'four', 9, 16, 25]
print(s)  # [1, 'four', 9, 16, 25]
print(s[1])  # four
print(len(s))  # 5

s[1] = 4
print(s)  # [1, 4, 9, 16, 25]

del s[2]
print(s)  # [1, 4, 16, 25]

s.append('egoing')
print(s)  # [1, 4, 16, 25, 'egoing']
