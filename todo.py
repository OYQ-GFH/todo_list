import os
import re
import time


def today_todo(today_time, today):

    f = open(today)
    text = f.read()
    f.close()

    find = len(re.findall(today_time, text))
    if find:
        return text
    else:
        return None


def new_todo(today, today_time):

    try:
        f = open(today, "r")
    except:
        f = open(today, "w")
        f.close()
        f = open(today, "r")

    text1 = input("代办: ")
    if today_todo(today_time, today) is not None:
        last_line = f.readlines()[-1]
        index = int(re.findall("(.*)\..*", last_line)[0]) + 1
        f.close()
        f = open(today, "a")
        f.write("{}.{}\n".format(index, text1))
        f.close()
        text2 = today_todo(today_time, today)
        os.system("clear")
        print(text2)
    else:
        f.close()
        f = open(today, "a")
        f.write("{}\n\n1.{}\n".format(today_time, text1))
        f.close()
        text2 = today_todo(today_time, today)
        os.system("clear")
        print(text2)


def yes_todo(path):
    
    index = -1
    index1 = input("序号: ")
    index2 = "%s." % index1
    index4 = None
    text = list()
    f = open(path, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        text.append(line)
    
    for a in text:
        index += 1
        if index2 in a:
            index3 = re.findall("(.*)\..*", a)[0]
            if index1 == index3:
                new_text = text.pop(index) 
                new_text = new_text.replace('\n', '')
                text.insert(index, "%s\t√\n" % new_text)
    
    f = open(path, "w")
    for a in text:
        f.write(a)
    f.close()
                

def main():

    today = time.localtime(time.time())
    today_time = "{}.{}.{}".format(today[0], today[1], today[2])
    path = "./all_todo_list/%s.txt" % today_time
    os.system("clear")

    while True:
        command = input("今天也是美好的一天(๑•̀ㅂ•́)و✧: ")
        if command == "n" or command == "N":
            new_todo(path, today_time)
        elif command == "y" or command == "Y":
            text2 = today_todo(today_time, path)
            os.system("clear")
            print(text2)
            yes_todo(path)
            text2 = today_todo(today_time, path)
            os.system("clear")
            print(text2)
        else:
            print("\n输入有误!")
            break
        

if __name__ == "__main__":
    main()
    
