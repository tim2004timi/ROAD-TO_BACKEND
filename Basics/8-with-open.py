try:
    with open("../text.txt", "r", encoding="utf-8") as file:
        s = file.read()
        print(s)

    # file = open("../text.txt", "r", encoding="utf-8")
    # try:
    #     s = file.read()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()

except FileNotFoundError:
    print("File not found")
except:
    print("Something went wrong")
