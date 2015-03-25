import collections
import os
import re



def count_word(file_name):
    f = open(file_name)

    line = f.readline()
    word_counter = collections.Counter()

    while line:
        words = re.findall("\w+", line.lower())
        word_counter.update(words)
        
        line = f.readline()

    f.close()
    sorted_list = sorted(word_counter.items(), key=lambda x:x[1],reverse=True)
    print sorted_list[0][0]


def get_all_file():
    current_dir = os.getcwd()
    all_file = os.listdir(current_dir)
    txt_file = []
    for i in all_file:
        if os.path.splitext(i)[1] == ".txt":
            txt_file.append(i)

    return txt_file
 
if __name__ == '__main__':
 #   count_word('english.txt')
    all_txt = get_all_file()
    for txt in all_txt:
        count_word(txt)
