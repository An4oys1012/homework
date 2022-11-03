import os
import shutil

print(os.name)
print(os.getcwd())
folder = folder_new = os.getcwd()

list_folder = ["py_file","json_file","csv_file","txt_file"]
for items in list_folder:
    os.mkdir(items)

def move():
    files = os.listdir(folder)
    for items in files:
        extension = items.split(".")
        if len(extension) > 1 and extension[1].lower() == "py":
            file = folder + "/" + items
            new_path = folder_new + "/py_file/" + items
            shutil.move(file, new_path)
        elif len(extension) > 1 and extension[1].lower() == "json":
            file = folder + "/" + items
            new_path = folder_new + "/json_file/" + items
            shutil.move(file, new_path)
        elif len(extension) > 1 and extension[1].lower() == "csv":
            file = folder + "/" + items
            new_path = folder_new + "/csv_file/" + items
            shutil.move(file, new_path)
        elif len(extension) > 1 and extension[1].lower() == "txt":
            file = folder + "/" + items
            new_path = folder_new + "/txt_file/" + items
            shutil.move(file, new_path)
move()

print('В папку с расширением py/" перемещено файлов: ', len(os.listdir('py_file')))
size_py = 0
for el in os.scandir("py_file"/"):
    size_py += os.path.getsize(el)
print("их суммарный размер равен: ", size_py, "байт")

print("В папку с расширением "/json/" перемещено файлов: ", len(os.listdir("json_file")))
size_json = 0
for el in os.scandir("json_file"):
    size_json += os.path.getsize(el)
print("их суммарный размер равен: ", size_json, "байт")

print("В папку с расширением "/csv/" перемещено файлов: ", len(os.listdir("csv_file")))
size_csv = 0
for el in os.scandir("csv_file"):
    size_csv += os.path.getsize(el)
print("их суммарный размер равен: ", size_csv, "байт")

print("В папку с расширением "/txt/" перемещено файлов: ", len(os.listdir("txt_file")))
size_txt = 0
for el in os.scandir("txt_file"):
    size_txt += os.path.getsize(el)
print("их суммарный размер равен: ", size_txt, "байт")

os.startfile('marks.txt')
os.startfile('функции.py')
print("После запуска файла функции.py получен результат: ")
from функции import hello

os.rename('decor.py', 'декоратор.py')
print("Файл 'decor.py' успешно переименован в 'декоратор.py'")

os.remove('111.py')





