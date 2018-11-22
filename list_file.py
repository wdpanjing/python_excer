import os
def list_file(path):
    l = os.listdir(path)
    for f in l:
        tmp = os.path.join(path,f)
        if os.path.isdir(tmp):
            list_file(tmp)
        if os.path.isfile(tmp):
            print(tmp)

def walk_file(path):
    file_list = []
    for root,dirs,files in os.walk(path):
        for file in files:
            file_list.append(file)
        for dir in dirs:
            walk_file(dir)
    return file_list

if __name__ == "__main__":
    a=walk_file(os.getcwd()+"\\for_os")
    print(a)
