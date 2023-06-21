personal = ['Alex','Ivan','Ira','Mary']
result = personal[0] + ' + ' + personal[2]
print(result + ' - the best pair') # Alex + Ira - the best pair

personal = ['Alex','Ivan','Ira','Mary']
print(personal[0])   # Alex

personal = ['Alex','Ivan','Ira','Mary']
print(len(personal))    # 4 - count number of items

personal = ['Alex','Ivan','Ira','Mary']
print(personal[-1])   # Mary - print last item

personal = ['Alex','Ivan','Ira','Olga']
print(personal[0:2])    # Alex Ivan - с 0 до 2го (не включительно)

personal = ['Alex','Ivan','Ira','Olga']
print(personal[1:])     # Ivan, Ira, Olga - с 1го и до конца

personal = ['Alex','Ivan','Ira','Olga']
personal.append('Fedor')
print(personal) 	# Alex, Ivan, Ira, Olga, Fedor - add item 'Fedor'

personal = ['Alex','Ivan','Ira','Olga']
num = [1, 2, 3, 4]
pn = []
pn.append(personal)
pn.append(num)
print(pn)       # [['Alex', 'Ivan', 'Ira', 'Olga'], [1, 2, 3, 4]] - sum of some Lists