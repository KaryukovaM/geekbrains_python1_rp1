import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

path_for_dir =[('dir_' + str(i + 1)) for  i in range(9)] 
def make_one_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - this dir is already exist')
def del_one_dir(paths):
    dir_path = os.path.join(os.getcwd(),paths)
    try:
        #print(dir_path)
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - error remove dir')
def make_all_dir():       # Напишите скрипт, создающий директории
    for i in path_for_dir: 
       make_one_dir(i)

def del_all_dir():      # И второй скрипт, удаляющий эти папки.
    for i in path_for_dir: 
        del_one_dir(i)
#make_all_dir()
del_all_dir()   


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path):
    for _ in os.listdir(path):
        print(_)
cur_path = os.path.abspath(os.curdir)
print(cur_path)
list_dir(cur_path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(first_file,backup_file):
    shutil.copy(first_file,backup_file)
 
first_file = sys.argv[0]
backup_file = first_file + '.backup'
print(backup_file)
copy_file(first_file,backup_file)