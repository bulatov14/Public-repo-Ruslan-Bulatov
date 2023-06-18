# fw = open('doc/file.txt', 'a')
# fw.write('Hello world\n')
# fw.close()      # открыть doc. создать файл, записать в конец 'Hello', с новой строки записать в след.раз, закрыть

# a - запись новых данных в файл и помещение новых данных в конец файла

# w - запись новых данных, но с удалением старых данных

# var = input('Write here something: ')
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

# fw = open('doc/file2.txt', 'w')
# fw.write('hi')
# fw.close()      # запись с перезаписью данных

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()
print(text)