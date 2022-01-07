value = 90
for i in range(180):
    if i % 2 == 0: i *= -1
    value = i + value
    print(value)