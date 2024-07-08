### FILE HANDING ###

### .txt file

# txt_file = open("C:/Users/pepe/Documents/2024/30_DIAS_PYTHON/dia_19_manejo_de_ficheros/my_file.txt","r+")

txt_file = open("dia_19_manejo_de_ficheros/my_file.txt","r+")
# print(txt_file.read())
# print(txt_file.read(10))

# print(txt_file.readline())
# print(txt_file.readlines())
# for line in txt_file.readlines():
#     print(line)
txt_file.readlines()
txt_file.write("\nAunque tambien me gusta R")