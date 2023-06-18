
# список - если большой массив данных и надо работать с каждым элементом независимо от того повторяется он или нет

family_1 = ['Alex','Ira','Semen','Mary','Alex']
print(family_1)

# множества - выводятся рандомно только единичные объекты, при этом регистрозависимо
#          - если большой массив данных и надо отсортировать повторяющиеся и использовать только одиночные

family_2 = {'Alex','Ira','Semen','Mary','Alex'}
print(family_2)

family_2 = {'alex','Ira','Semen','Mary','Alex'}
print(family_2)

# словарь - (ключ:значение)

family_3 = { 'dad':'Alex', 'mom':'Ira', 'son':'Semen', 'daughter':'Mary' }
print(family_3['dad'])      # Alex

family_3 = { 'dad':'Alex', 'mom':'Ira', 'son':'Semen', 'daughter':'Mary' }
for k, v in family_3.items():
    print(k)        # dad mom son daughter

family_3 = { 'dad':'Alex', 'mom':'Ira', 'son':'Semen', 'daughter':'Mary' }
for k, v in family_3.items():
    print(k + ' - ' + v)        # dad - Alex , mom - Ira, son - Semen, daughter - Mary