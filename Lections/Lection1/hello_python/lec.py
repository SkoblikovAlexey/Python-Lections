#print("Hello, world")   

#Типы данных: int, float, boolean, str, list, None
#value = None;
#print(type(value))
#a = 123
#b = 1.23
#print(type(a))
#print(type(b))
#value = 2234
#print(type(value))

#s = 'hello,\n world' # \ - с помощью него можем добавлять знаки, например n - переход на новую строку
#print(s)
#print(a, '-', b, '-', s)
#print('{} - {} - {}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#f = True
#print(f)
#list = [1,2,3]
#print(list)

#print('Введите a');
#a = int(input())
#print('Введите b');
#b = int(input())
#print(a,'+', b, "=", a + b)

# // - деление в целых числах
# ** - возведение в степерь
# round(значение, кол-во знаков после запятой) - округление

#a = 1 < 3 < 5< 10
#print(a)

#f = [1,2,3,4]
#print(2 in f)
#print(not 2 in f)

#is_odd = not f[0] % 2
#print(is_odd)

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b)

#elif:

from operator import inv


original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

for i in 1,2,3,4,5:
    print(i**2)

list = range(10)
for i in list:
    print(i)

for i in 'qwe - rty':
    print(i)

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
 print(i)
# 100 80 60 40 20
for i in range(5):
 print(i)
# 0 1 2 3 4

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

#Работа со строками

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
 print(c)

 text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#списки

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

#Функции

def f(x):
 return x**2
def f(x):
 if x == 1:
 return 'Целое'
 elif x == 2.3:
 return 23
 else:
 return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneTyp