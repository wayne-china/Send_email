import collections
import os
import re



def count_word(file_name):
    f = open(file_name)

    line = f.readline()
    line_counter=0
    space_counter=0
    comment_counter = 0


    while line:
        line_counter = line_counter+1
        if re.match("\s*#",line):
            comment_counter = comment_counter+1
        if re.match("\s*$",line):
            space_counter = space_counter +1
        
        line = f.readline()

    f.close()
    print "%s : %s %s %s"%(file_name,line_counter,comment_counter,space_counter)


def get_all_file():
    current_dir = os.getcwd()
    all_file = os.listdir(current_dir)
    txt_file = []
    for i in all_file:
        if os.path.splitext(i)[1] == ".py":
            txt_file.append(i)

    return txt_file


if __name__ == '__main__':
    all_txt = get_all_file()
    for txt in all_txt:
        count_word(txt)
    
