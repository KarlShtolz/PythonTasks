"""
Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.
Input1:
2
abcaz
Output1:
4

Input2:
2
helto
Output2:
3
"""
k = int(input())
s = input()
start = 0
frequency_map = {}
max_frequency = 0
longest_substring_length = 0
for end in range(len(s)):
    frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1
    max_frequency = max(max_frequency, frequency_map[s[end]])
    is_valid = (end + 1 - start - max_frequency <= k)
    if not is_valid:
        frequency_map[s[start]] -= 1
        start += 1
    longest_substring_length = end + 1 - start
print(longest_substring_length)

