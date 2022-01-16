import fleep
import os
from tqdm import tqdm
import sys
from colorama import Fore, Back, Style
from rich.console import Console
console = Console()
import tkinter.messagebox as tkmsg

if sys.platform == 'win32':
    mvcom = 'move'
else:
    mvcom = 'mv'
args = sys.argv[1:]
args = ['/home/vovak/noex']
if len(args) != 1:
    # print(Fore.RED + 'Ошибка в ввдении аргментов командной строки')
    # print(Fore.WHITE + 'python3' + Fore.CYAN + ' app.py ' + Fore.GREEN + ' директория '+Style.RESET_ALL)
    tkmsg.showerror('Ошибка','Ошибка в ввдении аргментов командной строки\npython3 app.py директория')
    exit()



# mvcom = 'mv'
dirPath = r""+args[0]
print(dirPath)
result = next(os.walk(dirPath))[2]

per,file_count = len(result),len(result)
if per == 0:
    exit()
filepercent = 100/per
completepercent = 0
i = 0
with console.status("[bold green]Отдумка...") as status:
    for file in tqdm(result):
        i+=1
        filee = dirPath + '/' + file
        fileeex = file
        with open(filee, "rb") as file:
            info = fleep.get(file.read(128))
            info.extension.append('no')
            if info.extension[0] == 'no':
                print('error {}'.format(fileeex))
                taskx = 'error'
                continue
            taskx = 'complete'
            del info.extension[-1]
            if len(info.extension) > 1:
                # print(fileeex,info.extension)
                info.extension[0] = '-'.join(info.extension)
                info.mime[0] = 'file/multiple'
            fileex = filee+'.'+info.extension[0]
            dir = info.mime[0].split('/')[1]

            path = dirPath + '/' + dir + '/'
            if os.path.isdir(path):
                command = '{} "{}" "{}"'.format(mvcom,filee,(str(dirPath)+'/'+str(dir)+'/'+fileeex+'.'+info.extension[0]))
                # print(command)
                os.system(command)
            else:
                os.makedirs(path)
                command = '{} "{}" "{}'.format(mvcom,filee,(str(dirPath)+'/'+str(dir)+'/'+fileeex+'.'+info.extension[0]))
                # print(command)
                os.system(command)
tkmsg.showinfo('Успех', 'Восстановление прошло успешно!')