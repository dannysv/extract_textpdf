import os
def main(fullpath_file, only_name, fulloutput_file):
    command = 'pdf2xml '+ fullpath_file + ' >' + fulloutput_file +'.xml'
    #command = 'tikapp --jar tika-app-1.20.jar -f '+fullpath_file +' -t'
    print(command)
    os.system(command)


#list the all files in 
path = '../Dataset-BG-Petrobras'
path_to = 'extr'
lista = os.listdir(path)
for item in lista:
    #print(item.replace)
    item = item.replace(' ', '\ ')
    text = main(path+'/'+item, item, path_to+'/'+ item)
