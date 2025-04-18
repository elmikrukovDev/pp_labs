result = 0
for n in range(1, 11):
    result += n ** 2

with open(__file__, 'r') as file:
    code = file.read()

print(code)
print(result)