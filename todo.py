import os
import re
import time


def today_todo(today_time, path):

    with open(path, "r") as f:
        text = f.read()

    find = len(re.findall(today_time, text))
    if find:
        return text
    else:
        return None


def new_todo(today_time, path):

    try:
        f = open(path, "r")
        f.close()
    except:
        f = open(path, "w")
        f.close()

    text1 = input("代办:")
    if today_todo(today_time, path) is not None:

        with open(path, "r") as f:
            last_line = f.readlines()[-1]
            index = int(re.findall("(.*)\..*", last_line)[0]) + 1
        with open(path, "a") as f:
            f.write("{}.{}\n".format(index, text1))
    else:
        with open(path, "a") as f:
            f.write("{}\n\n1.{}\n".format(today_time, text1))


def yes_todo(path):
    
    index = -1
    index1 = input("序号: ")
    index2 = "%s." % index1
    index4 = None
    text = list()
    
    with open(path, "r") as f:
        lines = f.readlines()

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
    
    with open(path, "w") as f:
        for a in text:
            f.write(a)
                

def max_num(path):
    
    nums = list()
    with open(path, "r") as f:
        lines = f.readlines()
    
    for line in lines:
        nums.append(len(line))
    
    num = max(nums)
    return num + 12


def printf(today_time, path):

    with open(path, "r") as f:
        lines = f.readlines()

    text = today_todo(today_time, path)
    num = max_num(path)
    os.system("clear")
    print("*" * num) 
    print(text)
    print("*" * num) 
    

def input_n_y(command, today_time, path):

    if command == "n" or command == "N":
        new_todo(today_time, path)
        printf(today_time, path)
        return 1
    elif command == "y" or command == "Y":
        printf(today_time, path)
        yes_todo(path)
        printf(today_time, path)
        return 1
    else:
        print("\n输入有误!")
        return 0


def main():

    today = time.localtime(time.time())
    today_time = "{}.{}.{}".format(today[0], today[1], today[2])
    path = "./all_todo_list/%s.txt" % today_time
    flag = False

    if os.path.exists(path):
        printf(today_time, path)
        flag = True
    else:
        command = input("今天还没有代办事项喔, 快来创建一个吧: ")
        if command == "n" or command == "N":
            if input_n_y(command, today_time, path):
                print("\n开启新的一天呀~")
                return
        else:
            print("\n输入有误!")
            return
            
    while True:
        if flag:
            command = input("今天也是美好的一天(๑•̀ㅂ•́)و✧: ")
            if not input_n_y(command, today_time, path):
                break
            
if __name__ == "__main__":
    main()
    
