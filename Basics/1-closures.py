def say_name(name):  # замыкание (say_goodbye -> say_name -> global f ->)

    def say_goodbye():
        print("goodbye", name)

    return say_goodbye


f = say_name("Tim")
f2 = say_name("Python")
f()  # goodbye Tim
f2()  # godbye Python


# ------------------------------------------------------------

def counter(start=1):
    def step():
        nonlocal start

        print(start)
        start += 1

    return step


c1 = counter()
c2 = counter(10)
c1()
c1()
c2()
c2()
c1()

