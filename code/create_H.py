from cmath import sqrt
from matrix_H import create_elements, Point_2P, Point_3P
from mes1 import tableElement, tableNode, Conductivity, Alfa, Density, SpecificHeat, SimulationStepTime, Tot
from create_Hbc import Bok1, Bok2, Bok3, Bok4
from create_Hbc_3 import Bok1_3, Bok2_3, Bok3_3, Bok4_3
import numpy as np


def N1(ksi, eta):
    return 0.25 * (1 - ksi) * (1 - eta)


def N2(ksi, eta):
    return 0.25 * (1 + ksi) * (1 - eta)


def N3(ksi, eta):
    return 0.25 * (1 + ksi) * (1 + eta)


def N4(ksi, eta):
    return 0.25 * (1 - ksi) * (1 + eta)


global_H_size = len(tableNode)
global_H = [[0 for x in range(global_H_size)] for y in range(global_H_size)]
global_C = [[0 for x in range(global_H_size)] for y in range(global_H_size)]
global_P = [0 for x in range(global_H_size)]


def agreagate_global_H(local_H, element):
    for i in range(4):
        for j in range(4):
            global_H[element.values[i] - 1][element.values[j] - 1] += local_H[i][j]


def agreagate_global_C(local_C, element):
    for i in range(4):
        for j in range(4):
            global_C[element.values[i] - 1][element.values[j] - 1] += local_C[i][j]


def agregate_global_P(local_P, element):
    for i in range(4):
        global_P[element.values[i] - 1] += local_P[i]


def print_H_GLobal(size, global_H):
    print("___________________________")
    for i in range(size):
        print(global_H[i])


# local_H_tab = [[[1 for x in range(len(tableElement))] for y in range(4)] for z in range(4)]
local_H_tab = []


def create_H(points, element, tableNode, kon, spec_Heat, density):
    global k
    element_4 = create_elements(points)

    tab_jacobian = [[0 for x in range(4)] for y in range(pow(points, 2))]
    tab_element_value = [element.value1, element.value2, element.value3, element.value4]

    for i in range(pow(points, 2)):
        dX_dKsi = 0
        dY_dKsi = 0
        dX_dEta = 0
        dY_dEta = 0
        for j in range(4):
            dX_dKsi += tableNode[tab_element_value[j] - 1].x * element_4["tab_Ksi"][j][i]
            dY_dKsi += tableNode[tab_element_value[j] - 1].y * element_4["tab_Ksi"][j][i]
            dX_dEta += tableNode[tab_element_value[j] - 1].x * element_4["tab_Eta"][j][i]
            dY_dEta += tableNode[tab_element_value[j] - 1].y * element_4["tab_Eta"][j][i]
            tab_jacobian[i][0] = round(dY_dKsi.real, 4)
            tab_jacobian[i][1] = round(dX_dKsi.real, 4)
            tab_jacobian[i][2] = round(dY_dEta.real, 4)
            tab_jacobian[i][3] = round(dX_dEta.real, 4)
        print(tab_jacobian[i])

    tab_detJ = [0 for x in range(pow(points, 2))]
    for i in range(pow(points, 2)):
        tab_detJ[i] = tab_jacobian[i][0] * tab_jacobian[i][3] - tab_jacobian[i][1] * tab_jacobian[i][2]

    tab_jacobian_reversed = [0 for x in range(pow(points, 2))]
    for j in range(pow(points, 2)):
        tab_jacobian_reversed[j] = 1 / tab_detJ[j]

    tab_dN_dX = [[[0 for x in range(pow(points, 2))] for y in range(4)] for z in range(pow(points, 2))]
    tab_dN_dY = [[[0 for x in range(pow(points, 2))] for y in range(4)] for z in range(pow(points, 2))]

    for i in range(pow(points, 2)):
        for j in range(4):
            for k in range(pow(points, 2)):
                tab_dN_dX[i][j][k] = tab_jacobian_reversed[i] * tab_jacobian[i][3] * element_4["tab_Ksi"][j][k] + tab_jacobian_reversed[i] * (-tab_jacobian[i][1])* element_4["tab_Eta"][j][k]
        # column = tab_dN_dX[i][1]
        # tab_dN_dX[i][1] = tab_dN_dX[i][3]
        # tab_dN_dX[i][3] = column
    # print(tab_dN_dX[0])

    for i in range(pow(points, 2)):
        for j in range(4):
            for k in range(pow(points, 2)):
                tab_dN_dY[i][j][k] = tab_jacobian_reversed[i] *tab_jacobian[i][0] * element_4["tab_Eta"][j][k] + tab_jacobian_reversed[i] *(-tab_jacobian[i][2]) * element_4["tab_Ksi"][j][k]
        # column = tab_dN_dY[i][1]
        # tab_dN_dY[i][1] = tab_dN_dY[i][3]
        # tab_dN_dY[i][3] = column
    # print(tab_dN_dY[0])

    tab_H_dX = [[[0 for x in range(pow(points, 2))] for y in range(4)] for z in range(pow(points, 2))]
    tab_H_dY = [[[0 for x in range(pow(points, 2))] for y in range(4)] for z in range(pow(points, 2))]
    for i in range(pow(points, 2)):
        for j in range(4):
            for k in range(4):
                tab_H_dX[i][j][k] = tab_dN_dX[i][j][i] * tab_dN_dX[i][k][i]

    for i in range(pow(points, 2)):
        for j in range(4):
            for k in range(4):
                tab_H_dY[i][j][k] = tab_dN_dY[i][j][i] * tab_dN_dY[i][k][i]
    # print(tab_H_dX)
    # print(tab_H_dY)

    tab_H = [[[0 for x in range(4)] for y in range(4)] for z in range(pow(points, 2))]
    tab_C = [[[0 for x in range(4)] for y in range(4)] for z in range(pow(points, 2))]

    if points == 2:
        for i in range(pow(points, 2)):
            N_functions_value = [
                N1(Point_2P[i]["ksi"], Point_2P[i]["eta"]),
                N2(Point_2P[i]["ksi"], Point_2P[i]["eta"]),
                N3(Point_2P[i]["ksi"], Point_2P[i]["eta"]),
                N4(Point_2P[i]["ksi"], Point_2P[i]["eta"])
            ]

            for j in range(4):
                for k in range(4):
                    tab_H[i][j][k] = kon * (tab_H_dX[i][j][k] + tab_H_dY[i][j][k]) * tab_detJ[i]
                    tab_C[i][j][k] = spec_Heat * density * N_functions_value[j] * N_functions_value[k] * tab_detJ[i]

    if points == 3:
        for i in range(pow(points, 2)):
            N_functions_value = [
                N1(Point_3P[i]["ksi"], Point_3P[i]["eta"]),
                N2(Point_3P[i]["ksi"], Point_3P[i]["eta"]),
                N3(Point_3P[i]["ksi"], Point_3P[i]["eta"]),
                N4(Point_3P[i]["ksi"], Point_3P[i]["eta"])
            ]

            for j in range(4):
                for k in range(4):
                    tab_H[i][j][k] = kon * (tab_H_dX[i][j][k] + tab_H_dY[i][j][k]) * tab_detJ[i]
                    tab_C[i][j][k] = spec_Heat * density * N_functions_value[j] * N_functions_value[k] * tab_detJ[i]

    wages_2_points = [1, 1, 1, 1]
    wages_3_points = [5 / 9, 8 / 9, 5 / 9]
    tab_wages_3 = [0 for x in range(9)]
    # for i in range(9):
    #     for j in range(3):
    #         for k in range(3):
    #             tab_wages_3[i] = (wages_3_points[k] * wages_3_points[j])
    if points == 2:
        for i in range(pow(points, 2)):
            for j in range(pow(points, 2)):
                tab_H[i][j][k] *= (wages_2_points[i] * wages_2_points[j])
    if points == 3:
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    tab_wages_3[i] *= (wages_3_points[k] * wages_3_points[j])


    HBC = [[0 for x in range(pow(points, 2))] for y in range(4)]
    HBC_1 = [[0 for x in range(pow(points, 2))] for y in range(4)]
    HBC_2 = [[0 for x in range(pow(points, 2))] for y in range(4)]
    HBC_3 = [[0 for x in range(pow(points, 2))] for y in range(4)]
    HBC_4 = [[0 for x in range(pow(points, 2))] for y in range(4)]
    for i in range(4):
        for j in range(4):
            HBC[i][j] = 0

    for i in range(4):
        for j in range(4):
            HBC_1[i][j] = 0
            HBC_2[i][j] = 0
            HBC_3[i][j] = 0
            HBC_4[i][j] = 0


    P = [0 for x in range(4)]
    P1 = [0 for x in range(4)]
    P2 = [0 for x in range(4)]
    P3 = [0 for x in range(4)]
    P4 = [0 for x in range(4)]

    if points == 2:
        if tableNode[tab_element_value[0] - 1].BC == 1:
            if tableNode[tab_element_value[1] - 1].BC == 1:
                bok1 = Bok1(tableNode[tab_element_value[0] - 1], tableNode[tab_element_value[1] - 1])
                HBC_1 = bok1.create_Hbc_1()
                P1 = bok1.create_vP1(Alfa, Tot)

        if tableNode[tab_element_value[1] - 1].BC == 1:
            if tableNode[tab_element_value[2] - 1].BC == 1:
                bok2 = Bok2(tableNode[tab_element_value[1] - 1], tableNode[tab_element_value[2] - 1])
                HBC_2 = bok2.create_Hbc_2()
                P2 = bok2.create_vP2(Alfa, Tot)

        if tableNode[tab_element_value[2] - 1].BC == 1:
            if tableNode[tab_element_value[3] - 1].BC == 1:
                bok3 = Bok3(tableNode[tab_element_value[2] - 1], tableNode[tab_element_value[3] - 1])
                HBC_3 = bok3.create_Hbc_3()
                P3 = bok3.create_vP3(Alfa, Tot)

        if tableNode[tab_element_value[3] - 1].BC == 1:
            if tableNode[tab_element_value[0] - 1].BC == 1:
                bok4 = Bok4(tableNode[tab_element_value[3] - 1], tableNode[tab_element_value[0] - 1])
                HBC_4 = bok4.create_Hbc_4()
                P4 = bok4.create_vP4(Alfa, Tot)

    if points == 3:
        if tableNode[tab_element_value[0] - 1].BC == 1:
            if tableNode[tab_element_value[1] - 1].BC == 1:
                bok1_3 = Bok1_3(tableNode[tab_element_value[0] - 1], tableNode[tab_element_value[1] - 1])
                HBC_1 = bok1_3.create_Hbc_1()
                P1 = bok1_3.create_vP1(Alfa, Tot)
            if tableNode[tab_element_value[1] - 1].BC == 1:
                if tableNode[tab_element_value[2] - 1].BC == 1:
                    bok2_3 = Bok2_3(tableNode[tab_element_value[1] - 1], tableNode[tab_element_value[2] - 1])
                    HBC_2 = bok2_3.create_Hbc_2()
                    P2 = bok2_3.create_vP2(Alfa, Tot)

            if tableNode[tab_element_value[2] - 1].BC == 1:
                if tableNode[tab_element_value[3] - 1].BC == 1:
                    bok3_3 = Bok3_3(tableNode[tab_element_value[2] - 1], tableNode[tab_element_value[3] - 1])
                    HBC_3 = bok3_3.create_Hbc_3()
                    P3 = bok3_3.create_vP3(Alfa, Tot)

            if tableNode[tab_element_value[3] - 1].BC == 1:
                if tableNode[tab_element_value[0] - 1].BC == 1:
                    bok4_3 = Bok4_3(tableNode[tab_element_value[3] - 1], tableNode[tab_element_value[0] - 1])
                    HBC_4 = bok4_3.create_Hbc_4()
                    P4 = bok4_3.create_vP4(Alfa, Tot)

    for i in range(4):
        P[i] = P1[i] + P2[i] + P3[i] + P4[i]

    agregate_global_P(P, element)

    for i in range(4):
        for j in range(4):
            HBC[i][j] = HBC_1[i][j] + HBC_2[i][j] + HBC_3[i][j] + HBC_4[i][j]



    H = [[0 for x in range(pow(points, 2))] for y in range(4)]
    C = [[0 for x in range(pow(points, 2))] for y in range(4)]

    for i in range(4):
        for j in range(4):
            H[i][j] = tab_H[0][i][j] + tab_H[1][i][j] + tab_H[2][i][j] + tab_H[3][i][j] + HBC[i][j]
            C[i][j] = tab_C[0][i][j] + tab_C[1][i][j] + tab_C[2][i][j] + tab_C[3][i][j]

    print("____________")
    print(P)
    print("____________")
    # print(tab_element_value)
    # -----------AGREGATION----------------
    agreagate_global_H(H, element)
    agreagate_global_C(C, element)
    # local_H_tab.append(H)


# for i in range(len(global_H)):
#     print(global_H[i])

for element in range(len(tableElement)):
    create_H(3, tableElement[element - 1], tableNode, Conductivity, SpecificHeat, Density)

# deklaracja tablocy H i C
global_H_and_C = [[0 for x in range(global_H_size)] for y in range(global_H_size)]
global_H_and_C_copy = [[0 for x in range(global_H_size)] for y in range(global_H_size)]

# in range nodes number
for i in range(16):
    for j in range(16):
        global_H_and_C[i][j] += global_H[i][j] + global_C[i][j] / SimulationStepTime # 50 - step time

for i in range(16):
    for j in range(16):
        global_H_and_C_copy[i][j] = global_H_and_C[i][j]

# 16 - nodes number
global_P_copy = [0 for x in range(16)]

temp_vector = [100 for x in range(16)]
for i in range(16):
    global_P_copy[i] = global_P[i]

print("___________________")
print(global_P)
print("___________________")
print_H_GLobal(16, global_H)
print_H_GLobal(16,global_C)
print_H_GLobal(16,global_H_and_C)

# in range SimulationTime / Simulation step time
for i in range(10):
    print("Iteration: ", i)
    for j in range(16):
        for k in range(16):
            global_P[j] += global_C[j][k] / SimulationStepTime * temp_vector[k]

    # print("____")
    # print(global_P)

    temp_vector = np.linalg.solve(global_H_and_C, global_P)

    min = np.min(temp_vector)
    max = np.max(temp_vector)

    print("Max temperature: ", max)
    print("Min temperature: ", min)
    print(temp_vector)
    for j in range(16):
        global_P[j] = global_P_copy[j]

    for j in range(16):
        for k in range(16):
            global_H_and_C[j][k] = global_H_and_C_copy[j][k]
