import os

def dict(path):
    list = os.listdir(path)
    make_dict = {path: []}
    for i in list:
        make_path = os.path.join(path, i)
        if os.path.isfile(make_path):
            make_dict[path].append(make_path)
        else:
            make_dict[path].append(dict(make_path))
    return make_dict

print(dict("C:\\Users\\posto\\Desktop\\python"))