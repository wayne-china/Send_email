# -- coding: utf-8 -- # 
# 用来生成邀请码


import random
import os
import torndb

def generate(number,length):
    codelist = []
    for n in range(number):
        string = ''
        for x in range(length):
            result = random.randint(0,9)
            string = string + str(result)
 
        codelist.append(string+"\n")
 
    return codelist

def write_to_file():
    fp = open("result.txt",'ab')
    code = generate(2000,20)
    for x in code:
        fp.write(x)

    fp.close()

def write_to_mysql():
    db = torndb.Connection("127.0.0.1","prac","root","daoli123")  
    table_name = "codelist"
    code = generate(20,20)
    for x in code:
        sql = "INSERT INTO %s VALUES('%s')" % (table_name,x)
        db.execute(sql)
    
        


if __name__ == "__main__":
    import pdb
  #  pdb.set_trace()
   # write_to_file()
    write_to_mysql()
 

