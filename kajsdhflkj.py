'''task 6'''
# n = int(input('введите номер месяца --> '))
# def season_events(number_of_month):
#     seasons = {
#         'winter':'За окном падал белый снег',
#         'summer':'Солнце светило ярче чем когда-либо',
#         'spring':'Птицы пели прекрасные песни',
#         'autumn':'Урожай был невероятным',
#     }
#     months = {
#         1: 'январь',
#         2: 'февраль',
#         3: 'март',
#         4: 'апрель',
#         5: 'май',
#         6: 'июнь',
#         7: 'июль',
#         8: 'август',
#         9: 'сентябрь',
#         10: 'октябрь',
#         11: 'ноябрь',
#         12: 'декабрь',
#     }
#     if number_of_month in [1,2,12]:
#         print(f"Вы родились в {months[number_of_month]}.{seasons['winter']}")
#     elif number_of_month in [3,4,5]:
#         print(f"Вы родились в {months[number_of_month]}.{seasons['spring']}")
#     elif number_of_month in [6,7,8]:
#         print(f"Вы родились в {months[number_of_month]}.{seasons['summer']}")
#     elif number_of_month in [9,10,11]:
#         print(f"Вы родились в {months[number_of_month]}.{seasons['autumn']}")
#     else:
#         print('нет такого месяца')
# season_events(n)


'''task 7'''
# def nums(number):
#     count = 0
#     for i in range(1,51):
#         if number % i == 0:
#             count += 1
#     if count > 2:
#         return 'составное'
#     else:
#         return 'простое'
# print(nums(13))


'''task 8'''
# def sorn(lst):
#     for i in range(len(lst)-1):
#         for k in range(len(lst)-1-i):
#             if lst[k] > lst[k+1]:
#                 lst[k],lst[k+1] = lst[k+1],lst[k]
#     return lst
# print(sorn([4,5,7,0,9,1,10,3,6,8,2]))


'''task 9'''
# def hesh():
#     a = [str(i) for i in input().split()]
#     out = {}
#     n = 0
#     for i in a:
#         if i in out:
#             out[i] += 1
#         elif not i in out:
#             out[i] = 1
#     for i in out:
#         if out[i] > n:
#             n = out[i]
#             res = f'{i} - {n}'
#     return res
#
# b = hesh()
# print(b)


'''палинтдромы,task 11'''
# n = str(input("--> "))
# def palind(string):
#     if string[::-1].lower() == string.lower():
#         return 'True'
#     else:
#         return 'False'
# print(palind(n))

'''task 13'''
# def search_substr(subst, st):
#     if subst in st:
#         print("Есть контакт!")
#     else:
#         print("Мимо!")
# search_substr('abc', 'sakljlhfabcoiwjefoi')

'''task 10, не работает'''
# def check_pass(pswd):
#     error = {
#         'len': 0,
#         'lw': 0,
#         'up': 0,
#         'symbs': 0,
#         'integ': 0,
#     }
#     error2 = {
#         'lw': "нет символа с низким регистром",
#         'up': "нет символа с высоким регистром",
#         'symbs': "нет спец символов",
#         'integ': "нет чисел",
#     }
#     inte = '1234567890'
#     low = 'qwertyuiopasdfghjklzxcvbnm'
#     upp = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     if len(pswd) == 8:
#         error['len'] = 1
#         for i in pswd:
#             low = i
#             if i in pswd:
#                 error['lw'] = 1
#                 break
#         for j in pswd:
#             upp = j
#             if j in pswd:
#                 error['up'] = 1
#                 break
#         for k in pswd:
#             inte = k
#             if k in pswd:
#                 error['integ'] = 1
#                 break
#         if '*' in pswd or '-' in pswd or '#' in pswd:
#             error['symbs'] = 1
#     elif len(pswd) < 8:
#         print('мало символов')
#     elif len(pswd) > 8:
#         print('много символов')
#     cnt = 0
#     mass_errors = []
#     for t in error:
#         if error[t] == 1:
#             cnt += 1
#         else:
#             mass_errors.append(error2[t])
#             print(cnt)
#     if cnt == 5:
#         print('пароль идеален')
#     else:
#         return False
#     print(mass_errors)
#
# n = input("введите пароль: ")
# func = check_pass(n)

'''task 17 tree'''
# def assimetr_tree(tree):
#     st_2 = 0
#     for i in tree:
#         if i == None:
#             tree.remove(i)
#     for i in range(1,len(tree)):
#         st_2 += 2**i
#         if len(tree) - 1 == st_2:
#             return True
#     else:
#         return False
# print(assimetr_tree([1,2,2,3,4,4,3]))

'''task 15 '''
# def prog(a,b,c):
#     razn = b-a
#     razn2 = c-b
#     if razn == razn2:
#         return True
#     else:
#         return False
# a = int(input('a'))
# b = int(input('b'))
# c = int(input('c'))
# print(prog(a,b,c))

import string
abc = string.ascii_lowercase
base_string = input("Введите строку: ")
secret = ""
for symbol in base_string:
   index = abc.index(symbol)
   if index < 23:
       new_index = index + 3
       new_symbol = abc[new_index]
       secret += new_symbol
   elif index == 23:
       new_index = index
       new_symbol = abc[new_index]
       secret += new_symbol
   elif index == 24:
       new_index = 1
       new_symbol = abc[new_index]
       secret += new_symbol
   elif index == 25:
       new_index = 2
       new_symbol = abc[new_index]
       secret += new_symbol
print(secret)
