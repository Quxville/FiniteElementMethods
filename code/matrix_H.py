from cmath import sqrt

def N1(ksi, eta):
    return 0.25 * (1 - ksi) * (1 - eta)


def N2(ksi, eta):
    return 0.25 * (1 + ksi) * (1 - eta)


def N3(ksi, eta):
    return 0.25 * (1 + ksi) * (1 + eta)


def N4(ksi, eta):
    return 0.25 * (1 - ksi) * (1 + eta)


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


Point_2P = [
    {"ksi": -(1 / sqrt(3)), "eta": -(1 / sqrt(3))},
    {"ksi": 1 / sqrt(3), "eta": -(1 / sqrt(3))},
    {"ksi": -(1 / sqrt(3)), "eta": 1 / sqrt(3)},
    {"ksi": 1 / sqrt(3), "eta": 1 / sqrt(3)}
]

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

dn_dKsi_differential = [dN1_dKsi, dN2_dKsi, dN3_dKsi, dN4_dKsi]
dn_dEta_differential = [dN1_dEta, dN2_dEta, dN3_dEta, dN4_dEta]


def create_elements(points):
    tab_Ksi = [[0 for x in range(pow(points, 2))] for y in range(4)]
    tab_Eta = [[0 for x in range(pow(points, 2))] for y in range(4)]

    if points == 2:
        for i in range(4):
            for j in range(4):
                tab_Ksi[i][j] = round(dn_dKsi_differential[i](Point_2P[j]["eta"]).real, 4)
                tab_Eta[i][j] = round(dn_dEta_differential[i](Point_2P[j]["ksi"]).real, 4)

    if points == 3:
        for i in range(4):
            for j in range(9):
                tab_Ksi[i][j] = round(dn_dKsi_differential[i](Point_3P[j]["eta"]).real, 4)
                tab_Eta[i][j] = round(dn_dEta_differential[i](Point_3P[j]["ksi"]).real, 4)
    element = {"tab_Ksi": tab_Ksi, "tab_Eta": tab_Eta}
    return element



# create_elements(3)