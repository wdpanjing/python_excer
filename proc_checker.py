import os

file_list = os.popen("ls *.v").readlines()
file_ls_tm = []
for file in file_list:
    file = file.replace("\n","")
    file_ls_tm.append(file)
    
file_list = file_ls_tm
print(file_list)

for file in file_list:
    temp = []
    with open(file,'r') as f_oj:
        for line in f_oj:
            temp.append(line)
    with open(file, 'w+') as f_oj:
        for line in temp:
            f_oj.write(line)
            if line.strip() == "initial":
                f_oj.write("begin\n")


