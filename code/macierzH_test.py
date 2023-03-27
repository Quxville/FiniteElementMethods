from element import Element
from node import Node
from point import Point
from math import sqrt

# PC for two points:
Point_2P = [
    {"ksi": -(1 / sqrt(3)), "eta": -(1 / sqrt(3))},
    {"ksi": 1 / sqrt(3), "eta": -(1 / sqrt(3))},
    {"ksi": -(1 / sqrt(3)), "eta": 1 / sqrt(3)},
    {"ksi": 1 / sqrt(3), "eta": 1 / sqrt(3)}
]

# PC for three points:
Point_3P = [
    {"ksi": -(sqrt(3 / 5)), "eta": -(sqrt(3 / 5))},
    {"ksi": 0, "eta": -(sqrt(3 / 5))},
    {"ksi": (sqrt(3 / 5)), "eta": -(sqrt(3 / 5))},
    {"ksi": -(sqrt(3 / 5)), "eta": 0},
    {"ksi": 0, "eta": 0},
    {"ksi": (sqrt(3 / 5)), "eta": 0},
    {"ksi": -(sqrt(3 / 5)), "eta": (sqrt(3 / 5))},
    {"ksi": 0, "eta": (sqrt(3 / 5))},
    {"ksi": (sqrt(3 / 5)), "eta": (sqrt(3 / 5))}
]

# PC for four points:
Point_4P = [
    {"ksi": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 - (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": -(sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
    {"ksi": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5)))), "eta": (sqrt(3 / 7 + (2 / 7 * sqrt(6 / 5))))},
]

wages_2P = [1, 1, 1, 1]

wages_3P = [8 / 9, 5 / 9, 8 / 9, 5 / 9, 8 / 9, 5 / 9, 8 / 9, 5 / 9, 8 / 9]

wages_4P = [(18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36, (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36,
            (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36, (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36,
            (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36, (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36,
            (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36, (18 + sqrt(30)) / 36, (18 - sqrt(30)) / 36]


def dN1_dEta(ksi):
    return -0.25 * (1 - ksi)


def dN1_dKsi(eta):
    return -0.25 * (1 - eta)


def dN2_dEta(ksi):
    return 0.25 * (1 - ksi)


def dN2_dKsi(eta):
    return -0.25 * (1 + eta)


def dN3_dEta(ksi):
    return 0.25 * (1 + ksi)


def dN3_dKsi(eta):
    return 0.25 * (1 + eta)


def dN4_dEta(ksi):
    return -0.25 * (1 + ksi)


def dN4_dKsi(eta):
    return 0.25 * (1 - eta)


dn_dKsi = [dN1_dKsi, dN2_dKsi, dN3_dKsi, dN4_dKsi]
dn_dEta = [dN1_dEta, dN2_dEta, dN3_dEta, dN4_dEta]

PIERWIASTEK1_3 = sqrt(1 / 3)
PIERWIASTEK3_5 = sqrt(3 / 5)
PIERWIASTEK_for_4P_plus = sqrt((3.0 / 7.0) + ((2.0 / 7.0) * sqrt((6.0 / 5.0))))
PIERWIASTEK_for_4P_minus = sqrt((3.0 / 7.0) - ((2.0 / 7.0) * sqrt((6.0 / 5.0))))


# ///////////////////////////////////////////// POINT_2
tabPC2_Eta = [-PIERWIASTEK1_3, -PIERWIASTEK1_3, PIERWIASTEK1_3, PIERWIASTEK1_3]
tabPC2_Ksi = [-PIERWIASTEK1_3, PIERWIASTEK1_3, -PIERWIASTEK1_3, PIERWIASTEK1_3]

tabKsi_N2 = [[0 for x in range(4)] for y in range(4)]
tabEta_N2 = [[0 for x in range(4)] for y in range(4)]

for i in range(4):
    tabKsi_N2[i][0] = dN1_dKsi(tabPC2_Ksi[i])
    tabKsi_N2[i][1] = dN2_dKsi(tabPC2_Ksi[i])
    tabKsi_N2[i][2] = dN3_dKsi(tabPC2_Ksi[i])
    tabKsi_N2[i][3] = dN4_dKsi(tabPC2_Ksi[i])

    tabEta_N2[i][0] = dN1_dEta(tabPC2_Eta[i])
    tabEta_N2[i][1] = dN2_dEta(tabPC2_Eta[i])
    tabEta_N2[i][2] = dN3_dEta(tabPC2_Eta[i])
    tabEta_N2[i][3] = dN3_dEta(tabPC2_Eta[i])
#
# print("Tab Ksi(point 2): ")
# for j in range(4):
#     print(tabKsi_N2[j])
#
# print("\nTab Eta(point2): ")
# for k in range(4):
#     print(tabEta_N2[k])
# print(tabKsi_N2)

# //////////////////////////////////////////////POINT_3
tabPC3_Eta = [-PIERWIASTEK3_5, -PIERWIASTEK3_5, -PIERWIASTEK1_3, 0, 0, 0, PIERWIASTEK3_5, PIERWIASTEK3_5, PIERWIASTEK3_5]
tabPC3_Ksi = [-PIERWIASTEK3_5, 0, PIERWIASTEK3_5, -PIERWIASTEK3_5, 0, PIERWIASTEK3_5, -PIERWIASTEK3_5, 0, PIERWIASTEK3_5]


tabKsi_N3 = [[0 for x in range(9)] for y in range(4)]
tabEta_N3 = [[0 for x in range(9)] for y in range(4)]


for i in range(9):
    tabKsi_N3[i][0] = dN1_dKsi(tabPC3_Ksi[i])
    tabKsi_N3[i][1] = dN2_dKsi(tabPC3_Ksi[i])
    tabKsi_N3[i][2] = dN3_dKsi(tabPC3_Ksi[i])
    tabKsi_N3[i][3] = dN4_dKsi(tabPC3_Ksi[i])

    tabEta_N3[i][0] = dN1_dEta(tabPC3_Eta[i])
    tabEta_N3[i][1] = dN2_dEta(tabPC3_Eta[i])
    tabEta_N3[i][2] = dN3_dEta(tabPC3_Eta[i])
    tabEta_N3[i][3] = dN3_dEta(tabPC3_Eta[i])

# print(tabKsi_N3[i])

p1 = Point(0, 0)
p2 = Point(0.025, 0)
p3 = Point(0.025, 0.025)
p4 = Point(0, 0.025)

point_list = [p1, p2, p3, p4]
# print(point_list)


def calculate_H():
    array_points = []
    point = int(input("Choose point: "))
    size = point * point
    if size == 4:
        array_points = Point_2P
        wages = wages_2P
    if size == 9:
        array_points = Point_3P
        wages = wages_3P
    if size == 16:
        array_points = Point_4P
        wages = wages_4P

    array_dN_Ksi = [4][size]
    for i in range(4):
        for j in range(size.lengh):
            array_dN_Ksi[i][j] = dn_dKsi[i]()




# calculate_H()


