import numpy as np
import matplotlib.pyplot as plt

with open('C:\\Users\\97254\\OneDrive\\Desktop\\Code\\TechnionCodeGit\\Bsc Winter Semseter 2026\\ChemEng-Ekronot-2H-Lab\\Lab_1\\temp_2D.txt', 'r') as file:
    temp_map = [[float(x) for x in line.split(' ')] for line in file]


def find_max_min_temp(temp_map):

    max_temp, min_temp = [temp_map[0][0]], [temp_map[0][0]]

    for i in range(len(temp_map)):
        for j in range(len(temp_map[0])):
            if temp_map[i][j] > max_temp[0]:
                max_temp[0] = temp_map[i][j]
            if temp_map[i][j] < min_temp[0]:
                min_temp[0] = temp_map[i][j]
    return f"{max_temp[0]} K, {min_temp[0]} K"

def create_heat_map(temp_map):
    Lx, Ly = len(temp_map[0]), len(temp_map)
    extent = 0, Lx, 0, Ly
    plt.imshow(temp_map, cmap=plt.cm.plasma, interpolation='bicubic', extent=extent, origin='lower')
    plt.title('Heat Convection Map')
    plt.colorbar(cmap='plasma', label='Temperature [K]')
    plt.xlabel('x [cm]')
    plt.ylabel('y [cm]')
    plt.show()

def central_difference(x_minus_1, x_plus_1, delta):
    return (x_plus_1 - x_minus_1) / (2 * delta)

def back_difference(x_minus_1, x, delta):
    return (x - x_minus_1) / delta

def forward_difference(x, x_plus_1, delta):
    return (x_plus_1 - x) / delta

def heat_flux_x(temp_map, delta, k):
    Lx, Ly = len(temp_map[0]), len(temp_map) #num of cols and rows
    qx = np.zeros((Lx, Ly)) #heat flux in x direction

    # Calculate qx

    for i in range(Lx):
        for j in range(Ly):
            if j == 0: #left side
                qx[i][j] = -k * forward_difference(temp_map[i][j], temp_map[i][j+1], delta)
            elif j == Ly - 1: #right side
                qx[i][j] = -k * back_difference(temp_map[i][j-1], temp_map[i][j], delta)
            else: #central difference
                qx[i][j] = -k * central_difference(temp_map[i][j-1], temp_map[i][j+1], delta)

    return qx

def heat_flux_y(temp_map, delta, k):
    Lx, Ly = len(temp_map[0]), len(temp_map) #num of cols and rows
    qy = np.zeros((Lx, Ly)) #heat flux in y direction

    # Calculate qy

    for i in range(Lx):
        for j in range(Ly):
            if i == 0: #top side
                qy[i][j] = -k * forward_difference(temp_map[i][j], temp_map[i+1][j], delta)
            elif i == Ly - 1: #bottom side
                qy[i][j] = -k * back_difference(temp_map[i-1][j], temp_map[i][j], delta)
            else: #central difference
                qy[i][j] = -k * central_difference(temp_map[i-1][j], temp_map[i+1][j], delta)

    return qy

def find_max_min_flux_x(temp_map, delta, k):
    qx = heat_flux_x(temp_map, delta, k)
    max_flux = np.max(qx)
    min_flux = np.min(qx)

    return max_flux, min_flux

def find_max_min_flux_y(temp_map, delta, k):
    qy = heat_flux_y(temp_map, delta, k)
    max_flux = np.max(qy)
    min_flux = np.min(qy)

    return max_flux, min_flux

def export_max_min_flux(temp_map, delta, k, filename):
    max_flux_x, min_flux_x = find_max_min_flux_x(temp_map, delta, k)
    max_flux_y, min_flux_y = find_max_min_flux_y(temp_map, delta, k)

    with open(filename, 'w') as file:
        file.write(f"Max and Min Heat Flux in X direction: {max_flux_x} W/cm^2, {min_flux_x} W/cm^2\n")
        file.write(f"Max and Min Heat Flux in Y direction: {max_flux_y} W/cm^2, {min_flux_y} W/cm^2\n")

print(f"Max and Min Temperatures:{find_max_min_temp(temp_map)}")

create_heat_map(temp_map)

export_max_min_flux(temp_map, 1, 500, 'heat_flux_output.txt')
