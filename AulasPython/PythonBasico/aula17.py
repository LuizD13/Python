"""
While em python
"""

i = 0
while i <= 10:
    if i == 0:
        i = i + 1
        continue #Pula o código e volta até a condição

    print(i)
    i += 1 #soma ele mesmo com mais 1, forma resumida (x = x + 1)
    break #finaliza o while, não importa o resultado


x = 0
y = 0

while x < 10:
    while y < 5:
        print(f'({x}),({y})')
        y += 1
    y = 0
    x += 1