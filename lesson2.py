""" Задача 1
i = 0
while i < 5:
    i = i +1;
    print(i, 0)
"""

""" Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.

number = 0
for i in range(1, 11):
    a = input("Введите цифру: ")
    if a == "5":
        number += 1
print('Количество введенных цифр 5 составляет',number)
"""

""" Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

pro = 1
for i in range(1,11):
    pro *=i
print(pro)
"""

""" Задача 6
Найти сумму цифр числа.

integer_number = 5679                           
print('Сумма числа',integer_number,"равна: ")   
sum = 0                                         
while integer_number>0:                         
    sum += integer_number % 10                  
    integer_number = integer_number//10         
print(sum)      
"""

""" Задача 7  
Найти произведение цифр числа.

integer_number = 679                                   
print('Произведение числа',integer_number,"равно: ")   
pro = 1                                                
while integer_number>0:                                
    pro *= integer_number % 10                         
    integer_number = integer_number//10                
print(pro)
"""


""" Задача 9
Найти максимальную цифру в числе

number = 8976543                                             
print('Максимальной цифрой в числе',number,'является: ')     
digit = 0                                                    
                                                             
while number>0:                                              
    if number % 10 > digit:                                  
        digit = number % 10                                  
    number = number//10                                      
                                                             
print(digit)                                                 
"""

""" Задача 10
Найти количество цифр 5 в числе   

integer_number = 43256789553493
print('Количество введенных цифр 5 в числе',integer_number,'составляет: ')
number = 0

while integer_number>0:
    if integer_number % 10 == 5:
        number += 1
    integer_number = integer_number//10

print(number)
"""
