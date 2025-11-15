import numpy as np
import matplotlib.pyplot as plt

k = 5  # W/m·K
delta = 0.01  # m

with open('C:\\Users\\97254\\OneDrive\\Desktop\\Code\\TechnionCodeGit\\Bsc Winter Semseter 2026\\ChemEng-Ekronot-2H-Lab\\Lab_1\\temp_2D.txt', 'r') as file:
    temp_map = [[float(x) for x in line.split(' ')] for line in file]
    
def find_max_min_temp(temp_map):

    max_temp, min_temp = [temp_map[0][0]], [temp_map[0][0]] #begins with first element of temp_map

    for i in range(len(temp_map)):
        for j in range(len(temp_map[0])):
            if temp_map[i][j] > max_temp[0]: #checks if current element is greater than max_temp
                max_temp[0] = temp_map[i][j]
            if temp_map[i][j] < min_temp[0]: #checks if current element is less than min_temp
                min_temp[0] = temp_map[i][j]
    return f"{max_temp[0]} K, {min_temp[0]} K"

def create_heat_map(temp_map):
    Lx, Ly = len(temp_map[0])-1, len(temp_map)-1 #dimenstions of the map
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
    Lx, Ly = len(temp_map[0]), len(temp_map) #dimensions of the map
    qx = np.zeros((Lx, Ly)) #empty matrix for heat flux in x direction

    # Calculate q''_x
    #temp_map is read left to right

    for i in range(Lx):
        for j in range(Ly):
            if j == 0: #left side of the map
                qx[i][j] = -k * forward_difference(temp_map[i][j], temp_map[i][j+1], delta)
            elif j == Ly - 1: #right side of the map
                qx[i][j] = -k * back_difference(temp_map[i][j-1], temp_map[i][j], delta)
            else: #central difference for inner points of the map
                qx[i][j] = -k * central_difference(temp_map[i][j-1], temp_map[i][j+1], delta)

    return qx

def heat_flux_y(temp_map, delta, k):
    Lx, Ly = len(temp_map[0]), len(temp_map) #dimensions of the map
    qy = np.zeros((Lx, Ly)) #empty matrix for heat flux in y direction

    # Calculate q''_y
    # temp_map is read from top to bottom

    for i in range(Lx):
        for j in range(Ly):
            if i == 0: #top side of the map
                qy[i][j] = -k * forward_difference(temp_map[i][j], temp_map[i+1][j], delta)
            elif i == Ly - 1: #bottom side of the map
                qy[i][j] = -k * back_difference(temp_map[i-1][j], temp_map[i][j], delta)
            else: #central difference for inner points of the map
                qy[i][j] = -k * central_difference(temp_map[i-1][j], temp_map[i+1][j], delta)

    return qy

def find_max_min_flux_x(temp_map, delta, k):
    qx = heat_flux_x(temp_map, delta, k) #heat flux in x direction
    max_flux = np.max(qx) #finds max value in heat flux in x direction
    min_flux = np.min(qx) #finds min value in heat flux in x direction

    return max_flux, min_flux

def find_max_min_flux_y(temp_map, delta, k):
    qy = heat_flux_y(temp_map, delta, k) #heat flux in y direction
    max_flux = np.max(qy) #finds max value in heat flux in y direction
    min_flux = np.min(qy) #finds min value in heat flux in y direction

    return max_flux, min_flux

def export_max_min_flux(temp_map, delta, k):
    #calculates max and min heat flux in x and y directions
    max_flux_x, min_flux_x = find_max_min_flux_x(temp_map, delta, k)
    max_flux_y, min_flux_y = find_max_min_flux_y(temp_map, delta, k)
    
    #exports the results to a text file
    filepath = f"C:\\Users\\97254\\OneDrive\\Desktop\\Code\\TechnionCodeGit\\Bsc Winter Semseter 2026\\ChemEng-Ekronot-2H-Lab\\Lab_1\\max_and_min_heat_flux.txt"
    with open(filepath, 'w') as file:
        file.write(f"Max and Min Heat Flux in X direction: {max_flux_x} W/m^2, {min_flux_x} W/m^2\n")
        file.write(f"Max and Min Heat Flux in Y direction: {max_flux_y} W/m^2, {min_flux_y} W/m^2\n")

def create_heat_flux_map(qx, qy):
    Lx, Ly = len(qx[0])-1, len(qx)-1 #dimenstions of the map
    extent = 0, Lx, 0, Ly

    fig, ax = plt.subplots(1, 2, figsize=(12, 4)) #creates 2 subplots side by side
    
    #first subplot - heat flux in x direction
    im1 = ax[0].imshow(qx, cmap=plt.cm.plasma, interpolation='bicubic', extent=extent, origin='lower')
    ax[0].set_title('Heat Flux in X Direction')
    ax[0].set_xlabel('x [cm]')
    ax[0].set_ylabel('y [cm]')
    fig.colorbar(im1, ax=ax[0], label=r'Heat Flux $[W/m^2]$')

    #second subplot - heat flux in y direction
    im2 = ax[1].imshow(qy, cmap=plt.cm.plasma, interpolation='bicubic', extent=extent, origin='lower')
    ax[1].set_title('Heat Flux in Y Direction')
    ax[1].set_xlabel('x [cm]')
    ax[1].set_ylabel('y [cm]')
    fig.colorbar(im2, ax=ax[1], label=r'Heat Flux $[W/m^2]$')

    plt.tight_layout() 
    plt.show()

def find_temp_and_flux_at_y(y, temp_map, delta, k):
    temp_y = [temp_map[y][i] for i in range(len(temp_map[0]))] #finds temperature at given y

    qy = heat_flux_y(temp_map, delta, k) #heat flux in y direction
    qy_y = qy[y] #finds heat flux perpendicular to given y
    return temp_y, qy_y

def graph_temp_and_flux_at_y(y, temp_map, delta, k):
    temp_y, qy_y = find_temp_and_flux_at_y(y, temp_map, delta, k)

    fig, ax = plt.subplots(2, 1, figsize=(8, 4)) #creates 2 subplots
    
    ax[0].plot(range(len(temp_map[0])), temp_y) #plots line graph of temp at given y
    ax[0].set_title(rf"Temperature as a Function of x on y={y:.1f}cm")
    ax[0].set_xlabel('x [cm]')
    ax[0].set_ylabel('T [K]')

    ax[1].plot(range(len(qy_y)), qy_y) #plots line graph of heat flux perpendicular to given y
    ax[1].set_title(rf"$q''_y$ as a Function of x on y={y:.1f}cm")
    ax[1].set_xlabel('x [cm]')
    ax[1].set_ylabel(r"$q''_y$ $[W/m^2]$")

    plt.tight_layout()
    plt.show()

def export_temp_and_flux_at_y(y, temp_map, delta, k):
    temp_y, qy_y = find_temp_and_flux_at_y(y, temp_map, delta, k)
        
    filepath1 = f"C:\\Users\\97254\\OneDrive\\Desktop\\Code\\TechnionCodeGit\\Bsc Winter Semseter 2026\\ChemEng-Ekronot-2H-Lab\\Lab_1\\Temperature_at_y_{y}.txt"
    filepath2 = f"C:\\Users\\97254\\OneDrive\\Desktop\\Code\\TechnionCodeGit\\Bsc Winter Semseter 2026\\ChemEng-Ekronot-2H-Lab\\Lab_1\\Heat_Flux_at_y_{y}.txt"
    
    with open(filepath1, 'w') as file: #file for temperature @ given y
        file.write("x [cm], T [K]\n")
        for i in range(len(temp_map[0])):
            file.write(f"{i}, {temp_y[i]}\n")

    with open(filepath2, 'w') as file: #file for heat flux @ given y
        file.write("x [cm], q''_y [W/m^2]\n")
        for i in range(len(qy_y)):
            file.write(f"{i}, {qy_y[i]}\n")

def heat_power_at_y(y, temp_map, delta, k):
    qy_y = find_temp_and_flux_at_y(y, temp_map, delta, k)[1] #heat flux perpendicular to given y
    total_heat_power = 0
    for i in range(len(qy_y)):
        total_heat_power += qy_y[i] * delta  #integrates heat flux over the length in x direction

    print(total_heat_power)


print("Max and Min Temperatures:", find_max_min_temp(temp_map))
create_heat_map(temp_map)
create_heat_flux_map(heat_flux_x(temp_map, delta, k), heat_flux_y(temp_map, delta, k))
export_max_min_flux(temp_map, delta, k)
graph_temp_and_flux_at_y(4, temp_map, delta, k)
export_temp_and_flux_at_y(4, temp_map, delta, k)

heat_power_at_y(4, temp_map, delta, k)