import string

SUPER_SECRET_ANSWER = [14235559, 79805, 79790, 31012838, 14235543, 232339379, 232339347, 5846936, 31012757, 1652633]

def decode_message(list_of_ints, key_string):
  key = key_string.encode()
  decoded = []
  for i, num in enumerate(list_of_ints):
    result = num ^ key[i % len(key)]
    # Проверяем диапазон и корректируем результат, если необходимо
    if result < 0 or result > 0x10FFFF:
      result = (result % 0x110000)
    decoded.append(chr(result))
  return ''.join(decoded)

key = "int 	  	finally 	  	for 	  	new 	  	-42  \n   finally\n            true\nelse\nabstract\nvoid\n            ()"

ans = decode_message(SUPER_SECRET_ANSWER, key)
print(ans)