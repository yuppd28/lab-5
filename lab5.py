import csv
import sys

filename="mydata.txt"

def read(filename):
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()
    print("зчитування файлу виконано")
    
    
import random

filename="mydata.txt"

def append(filename): 
    fd = open(filename, "a")
    for i in range(15):
        A = random.uniform(2, 5)
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("дозапис у кінець файлу виконано") 
 
filename = "mydata.txt"

def write(filename):
    fd = open(filename, "w")
    for i in range(9):
        A = i*15
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("запис файлу виконано")
    
    
import shutil
import os

def copy(filename):
    shutil.copyfile("C:\\ICS-485770\\mydata.txt", "C:\\Games\\lab5.txt")
    print("копіювання файлу виконано")     
def rename(filename):
    os.rename("C:\\ICS-485770\\mydata.txt", "C:\\ICS-485770\\mydata12.txt")
    print("перейменування файлу виконано")
def delete(filename):
    os.remove("C:\\ICS-485770\\mydata.txt")
    print("видалення файлу виконано")     


x=int(input("виберіть режим роботи з файлом: \n :: 1 - читати файл :: \n :: 2 - записати у файл :: \n :: 3 - дозапис у файл :: \n :: 4 - перейменувати файл :: \n :: 5 - видалити файл :: \n :: 6 - зробити копію файлу ::\n"))          

mode=' '
if x==1:
    read(filename)
elif x==2:
    write(filename)
elif x==3:
    append(filename) 
elif x==4:
    rename(filename)
elif x==5:
    delete(filename)         
elif x==6:
    copy(filename)
else:
    print("такого варіанту немає")    