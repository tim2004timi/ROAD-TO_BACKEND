def foo(lst):
    for i in lst:
        s = i.replace("/", ".")
        s = s.split(".")

        if s[4] == "24":
            mask = "255.255.255.0"
        elif s[4] == "30":
            mask = "255.255.255.252"
        elif s[4] == "16":
            mask = "255.255.0.0"

        s[1] = str(int(s[1]) + 11)

        print(f"ip route {'.'.join(s[:4])} {mask} {interface}")


third_networks = \
"""10.11.11.0/30
30.30.22.0/30
30.30.33.0/30
182.200.1.0/30
182.200.2.0/30
182.200.3.0/30
169.185.1.0/30
169.185.2.0/30
169.185.3.0/30
172.160.1.0/30
172.160.2.0/30
172.160.3.0/30"""

second_networks = \
    """10.10.10.0/30
    30.30.2.0/30
    30.30.3.0/30
    18.20.1.0/30
    18.20.2.0/30
    18.20.3.0/30
    16.18.1.0/30
    16.18.2.0/30
    16.18.3.0/30
    17.16.1.0/30
    17.16.2.0/30
    17.16.3.0/30"""

first_networks = \
    """10.20.0.0/30
    10.19.0.0/30
    10.16.0.0/30
    10.17.0.0/30
    10.0.0.0/16"""

third_networks = third_networks.split()
second_networks = second_networks.split()
first_networks = first_networks.split()

j = int(input("j: "))
next_network = second_networks[j - 1]
pc_network = third_networks[j - 1]

second_networks.remove(next_network)
third_networks.remove(pc_network)

next_network = next_network.replace("/", ".")
next_network = next_network.split(".")
next_network[1] = str(int(next_network[1]) + 11)
next_network[3] = str(int(next_network[3]) + 2)

interface = ".".join(next_network[:4])

print("ena")
print("conf t")
foo(third_networks)
foo(second_networks)
foo(first_networks)
print("exit")
print("wr\n\n\n")