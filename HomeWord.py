#""" №1 Создадим пустую функцию,
#которая ничего не возвращает"""
def function():   # функция пустая
 	pass          # отмена ее возврата

   


#""" №2 Написать функцию,
#которая принимает число,
#возвращает его значение
#умноженное на два"""
def func(a):      # обозначение функции 
 	 return a*2   # функция умноженная на два

print(func(94))   #  функция приняла число




#""" №3 Написать функцию, которая определяет
#параметр на четность. Если четное число
#пишем("yes") в ином случае("no")."""
def funct(b):          # функция
	if b % 2 == 0:     # определяет четное ли число
		return("yes")  # вернуть да, если четное
	else:              # иначе
		return("no")   # вернуть нет

print(funct(int(input(7))))#написать:функция-числа-вернуть(число)




#""" №4 Написать функцию, принимающую два аргумента.
#После чего проверим, если первое число больше 10,
#пишем("да"), если меньше("нет").
def fun(c,d):             # функция с двумя аргументами
	if c > 10:            # условие
		return("yes" )    # если верно вернуть да
	else:                 # иначе
		return("no")      # вернуть нет
	print(fun(7,20))      # написать функция-число-число




#""" №5 Написать лямбда-функцию, которая делит
#по модулю(%) два аргумента."""
function = lambda x, y: x % y   # функция с условияими

print(function(9, 5))           # написать функцию-число-число




#""" №6 Создать функцию с простыми командами.
#Обернуть ее в декоратор, который бы дополнял возможности 
#функции"""
def decorator(Say_Hello):   # создание функции
	def wrap():             # обертываем функцию
		print("======")     # пишем первую обертку
		Say_Hello()         # текст-вывод в консоль
		print("======")     # пишем последнюю обертку
	return wrap             # вернуть упаковку
	
@decorator                  # создание декорации
def Say_Hello():            # название функции
	print("Hello world")    # пишет текст

Say_Hello()




#""" №7 Использовать функцию map и filter"""
#                'filter'
num = [1, 2, 3, 4, 5, 6, 7, 8]   # создание переменной

def check(x):                    # функция
	return x >2                  # возвращение функции

num = list(filter(check, num))   # использование filter функции
print(num)                       # пишем результат

 #                 'map'
a =[1, 2, 3, 4, 5, 6, 7, 8]     # создание переменной
def ten(x):                     # функция
	return x // 2               # возвращение функции
a = list(map(ten, a))           # использование map функции
print(a)                        # пишем результат




#""" №8 Создать чистую и не чистую функцию"""
#               ' чистая'
def pure_func(x, y):           # создание функции
	temp = x + 2*y             # условия функции
	return temp / (2*x + y)    # возвращение функции

               # 'не чистая'
some_list =[]                 # создание переменной
def impure(arg):              # создание функции
	some_list.append(arg)     # изменила состояние списка


#""" №9 Сделать функцию поиска минимума
#  и максимума в списке"""

a=[4,7,9,32,67,86,43]        # создание переменной
print(min(a), max(a))        # пишет результат




#""" №10 Написать функцию, которая определяется
# как год високосный. Пользователь возвращает год,
#если функция возвращает True. Если нет, то False.""""

def year(x):                # создание функции
	if x % 4 == 0:          # условие функции
		return("True")      # возвращение если истенно
	else:                   # иначе
		return("False")     # возвращение не верно




#""" №11 Создать функцию season, принимающую один
#аргумент- номер месяца ( от 1 до 12), которому 
#этот месяц принадлежит(зима, весна, лето, осень)"""
def season(a):
	if a == 1 in a == 2 in a ==12:
		return('Это зимний месяц')
	elif a == 3 in a == 4 in a == 5:
		return('Это весенний месяц')
	elif a == 6 in a == 7 in a == 8:
		return('Это летний месяц')
	elif a == 9 in a == 10 in a == 11:
		return('Это осенний месяц')
	
print(season(int(input()))

