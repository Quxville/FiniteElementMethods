from cmath import sqrt
import self as self
from mes1 import tableNode, Node, Alfa


def N1(ksi, eta):
    return 0.25 * (1 - ksi) * (1 - eta)


def N2(ksi, eta):
    return 0.25 * (1 + ksi) * (1 - eta)


def N3(ksi, eta):
    return 0.25 * (1 + ksi) * (1 + eta)


def N4(ksi, eta):
    return 0.25 * (1 - ksi) * (1 + eta)


tab_2points = {
    "PC11": [-1 / sqrt(3), -1],
    "PC12": [1 / sqrt(3), -1],
    "PC21": [1, -1 / sqrt(3)],
    "PC22": [1, 1 / sqrt(3)],
    "PC31": [-1 / sqrt(3), 1],
    "PC32": [1 / sqrt(3), 1],
    "PC41": [-1, -1 / sqrt(3)],
    "PC42": [-1, 1 / sqrt(3)]
}

tab_3points = {
    "PC11": [-sqrt(3.0/5.0), -1],
    "PC12": [0, -1],
    "PC13": [sqrt(3.0/5.0), -1],
    "PC21": [1, -sqrt(3.0/5.0)],
    "PC22": [1, 0],
    "PC23": [1, sqrt(3.0/5.0)],
    "PC31": [-sqrt(3.0/5.0), 1],
    "PC32": [0, 1],
    "PC33": [sqrt(3.0/5.0), 1],
    "PC41": [-1, -sqrt(3.0/5.0)],
    "PC42": [-1, 0],
    "PC43": [-1, sqrt(3.0/5.0)],
}


class Bok1:
    def __init__(self, ID_1, ID_2):
        self.ID_1 = ID_1
        self.ID_2 = ID_2

    points = 2
    if points == 2:
        point1_N_values = [N1(tab_2points["PC11"][0], tab_2points["PC11"][1]),
                           N2(tab_2points["PC11"][0], tab_2points["PC11"][1]),
                           N3(tab_2points["PC11"][0], tab_2points["PC11"][1]),
                           N4(tab_2points["PC11"][0], tab_2points["PC11"][1])]

        point2_N_values = [N1(tab_2points["PC12"][0], tab_2points["PC12"][1]),
                           N2(tab_2points["PC12"][0], tab_2points["PC12"][1]),
                           N3(tab_2points["PC12"][0], tab_2points["PC12"][1]),
                           N4(tab_2points["PC12"][0], tab_2points["PC12"][1])]
    elif points == 3:
        point1_N_values = [N1(tab_3points["PC11"][0], tab_3points["PC11"][1]),
                           N2(tab_3points["PC11"][0], tab_3points["PC11"][1]),
                           N3(tab_3points["PC11"][0], tab_3points["PC11"][1]),
                           N4(tab_3points["PC11"][0], tab_3points["PC11"][1])]

        point2_N_values = [N1(tab_3points["PC12"][0], tab_3points["PC12"][1]),
                           N2(tab_3points["PC12"][0], tab_3points["PC12"][1]),
                           N3(tab_3points["PC12"][0], tab_3points["PC12"][1]),
                           N4(tab_3points["PC12"][0], tab_3points["PC12"][1])]

        point3_N_values = [N1(tab_3points["PC13"][0], tab_3points["PC13"][1]),
                           N2(tab_3points["PC13"][0], tab_3points["PC13"][1]),
                           N3(tab_3points["PC13"][0], tab_3points["PC13"][1]),
                           N4(tab_3points["PC13"][0], tab_3points["PC13"][1])]

    def create_Hbc_1(self):

        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2
        tab_Hbc_1 = [[0 for x in range(4)] for y in range(4)]

        for i in range(4):
            for j in range(4):
                tab_Hbc_1[i][j] = Alfa * (
                        self.point1_N_values[i] * self.point1_N_values[j] + self.point2_N_values[i] *
                        self.point2_N_values[j]) * det_J

        return tab_Hbc_1

    def create_vP1(self, alfa, temp_ot):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2

        P_PC_1 = [0 for x in range(4)]
        P_PC_2 = [0 for x in range(4)]
        P1 = [0 for x in range(4)]
        for i in range(4):
            P1[i] = Alfa * (self.point1_N_values[i] * temp_ot + self.point2_N_values[i] * temp_ot) * det_J
            print(P1)

        return P1


class Bok2:
    def __init__(self, ID_1, ID_2):
        self.ID_1 = ID_1
        self.ID_2 = ID_2

    point2_N_values = [N1(tab_2points["PC21"][0], tab_2points["PC21"][1]),
                       N2(tab_2points["PC21"][0], tab_2points["PC21"][1]),
                       N3(tab_2points["PC21"][0], tab_2points["PC21"][1]),
                       N4(tab_2points["PC21"][0], tab_2points["PC21"][1])]

    point3_N_values = [N1(tab_2points["PC22"][0], tab_2points["PC22"][1]),
                       N2(tab_2points["PC22"][0], tab_2points["PC22"][1]),
                       N3(tab_2points["PC22"][0], tab_2points["PC22"][1]),
                       N4(tab_2points["PC22"][0], tab_2points["PC22"][1])]

    # det_J = (sqrt(pow(tableNode[self.ID_2 - 1].x - tableNode[self.ID_1 - 1].x, 2) + pow(
    #     tableNode[self.ID_2 - 1].y - tableNode[self.ID_1 - 1].y, 2))) / 2

    def create_Hbc_2(self):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2
        tab_Hbc_2 = [[0 for x in range(4)] for y in range(4)]

        for i in range(4):
            for j in range(4):
                tab_Hbc_2[i][j] = Alfa * (
                        self.point2_N_values[i] * self.point2_N_values[j] + self.point3_N_values[i] *
                        self.point3_N_values[j]) * det_J
        return tab_Hbc_2

    def create_vP2(self, alfa, temp_ot):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2

        P_PC_2 = [0 for x in range(4)]
        P_PC_3 = [0 for x in range(4)]
        P2 = [0 for x in range(4)]
        for i in range(4):
            # P_PC_2[i] = alfa * self.point2_N_values[i] * temp_ot * self.det_J
            # P_PC_3[i] = alfa * self.point3_N_values[i] * temp_ot * self.det_J
            #
            # P[i] = P_PC_2[i] + P_PC_3[i]
            P2[i] = alfa * (self.point2_N_values[i] * temp_ot + self.point3_N_values[i] * temp_ot) * det_J

        return P2


class Bok3:
    def __init__(self, ID_1, ID_2):
        self.ID_1 = ID_1
        self.ID_2 = ID_2

    point3_N_values = [N1(tab_2points["PC31"][0], tab_2points["PC31"][1]),
                       N2(tab_2points["PC31"][0], tab_2points["PC31"][1]),
                       N3(tab_2points["PC31"][0], tab_2points["PC31"][1]),
                       N4(tab_2points["PC31"][0], tab_2points["PC31"][1])]

    point4_N_values = [N1(tab_2points["PC32"][0], tab_2points["PC32"][1]),
                       N2(tab_2points["PC32"][0], tab_2points["PC32"][1]),
                       N3(tab_2points["PC32"][0], tab_2points["PC32"][1]),
                       N4(tab_2points["PC32"][0], tab_2points["PC32"][1])]

    # det_J = (sqrt(pow(tableNode[self.ID_2 - 1].x - tableNode[self.ID_1 - 1].x, 2) + pow(
    #     tableNode[self.ID_2 - 1].y - tableNode[self.ID_1 - 1].y, 2))) / 2

    def create_Hbc_3(self):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2

        tab_Hbc_3 = [[0 for x in range(4)] for y in range(4)]

        for i in range(4):
            for j in range(4):
                tab_Hbc_3[i][j] = Alfa * (
                        self.point3_N_values[i] * self.point3_N_values[j] + self.point4_N_values[i] *
                        self.point4_N_values[j]) * det_J

        return tab_Hbc_3

    def create_vP3(self, alfa, temp_ot):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2
        P_PC_3 = [0 for x in range(4)]
        P_PC_4 = [0 for x in range(4)]
        P3 = [0 for x in range(4)]
        for i in range(4):
            # P_PC_3[i] = alfa * self.point3_N_values[i] * temp_ot * self.det_J
            # P_PC_4[i] = alfa * self.point4_N_values[i] * temp_ot * self.det_J
            #
            # P[i] = P_PC_3[i] + P_PC_4[i]
            P3[i] = alfa * (self.point3_N_values[i] * temp_ot + self.point4_N_values[i] * temp_ot) * det_J

        return P3


class Bok4:
    def __init__(self, ID_1, ID_2):
        self.ID_1 = ID_1
        self.ID_2 = ID_2


    point4_N_values = [N1(tab_2points["PC41"][0], tab_2points["PC41"][1]),
                       N2(tab_2points["PC41"][0], tab_2points["PC41"][1]),
                       N3(tab_2points["PC41"][0], tab_2points["PC41"][1]),
                       N4(tab_2points["PC41"][0], tab_2points["PC41"][1])]

    point1_N_values = [N1(tab_2points["PC42"][0], tab_2points["PC42"][1]),
                       N2(tab_2points["PC42"][0], tab_2points["PC42"][1]),
                       N3(tab_2points["PC42"][0], tab_2points["PC42"][1]),
                       N4(tab_2points["PC42"][0], tab_2points["PC42"][1])]

    # det_J = (sqrt(pow(tableNode[self.ID_2 - 1].x - tableNode[self.ID_1 - 1].x, 2) + pow(
    #     tableNode[self.ID_2 - 1].y - tableNode[self.ID_1 - 1].y, 2))) / 2

    def create_Hbc_4(self):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2

        tab_Hbc_4 = [[0 for x in range(4)] for y in range(4)]

        for i in range(4):
            for j in range(4):
                tab_Hbc_4[i][j] = Alfa * (
                        self.point4_N_values[i] * self.point4_N_values[j] + self.point1_N_values[i] *
                        self.point1_N_values[j]) * det_J

        return tab_Hbc_4

    def create_vP4(self, alfa, temp_ot):
        det_J = (sqrt(pow(self.ID_2.x - self.ID_1.x, 2) + pow(self.ID_2.y - self.ID_1.y, 2))) / 2

        P_PC_4 = [0 for x in range(4)]
        P_PC_1 = [0 for x in range(4)]
        P4 = [0 for x in range(4)]

        for i in range(4):
            # P_PC_4[i] = alfa * self.point4_N_values[i] * temp_ot * self.det_J
            # P_PC_1[i] = alfa * self.point1_N_values[i] * temp_ot * self.det_J
            #
            # P[i] = P_PC_4[i] + P_PC_1[i]
            P4[i] = alfa * (self.point4_N_values[i] * temp_ot + self.point1_N_values[i] * temp_ot) * det_J

        return P4
