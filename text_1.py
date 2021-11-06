import random
import string
import os

def rd_str(lenght):
    letters = string.ascii_lowercase
    st = ''.join(random.choice(letters) for i in range(lenght))
    return st

def make_sentence(lenght_sentence):
    sentence = ' '.join(rd_str(random.randint(4,12)) for i in range(lenght_sentence))
    return str.capitalize(sentence)

def make_text(lenght_text):
    text = '. '.join(make_sentence(random.randint(1,30)) for i in range(lenght_text))
    return text


for i in range(10):
    folder_name = 'Folder'+ str(i)
    path_folder = "C:\\Users\\posto\\Desktop\\python"
    full_f_name = os.path.join(path_folder, folder_name)
    os.mkdir(full_f_name)

    for i in range(10):
        file_name = 'file'+ str(i) +'.txt'
        file = open(os.path.join(full_f_name, file_name), 'w')
        file.write(make_text(random.randint(10,100)))





