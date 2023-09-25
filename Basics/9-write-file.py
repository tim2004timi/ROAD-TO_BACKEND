try:
    with open("../text.txt", "a+", encoding="utf-8") as file:
        file.seek(0)
        print(file.read())

        # file.write("Something 1\n")
        # file.write("Something 2\n")
        # file.write("Something 3\n")
except:
    print("Something went wrong")

# a - append - дозапись в файл
# w - write - запись в файл
# r - read - чтение из файла
# a+ - append+ - добавление и чтение в файле

# ----------------------------------------------------

import pickle


# бинарная запись в файл
try:
    with open("../data.bin", "wb") as file:
        pickle.dump(["Hello", {0: False, 1: True}], file)
except:
    print("Something went wrong (writing)")

# бинарное чтение с файла
try:
    with open("../data.bin", "rb") as file:
        data = pickle.load(file)
        print(data)
except:
    print("Something went wrong (reading)")
