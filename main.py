import matplotlib.pyplot as plt

def calculate_dispersion(wavelength):
    S0 = 0.11
    U0 = 1320
    disp = (S0/4)*wavelength*(1-(U0/wavelength)**4)
    return disp

wavelengths = []
wavelengths = [i for i in range(850,1850,10)]

dispersion = []

for i in wavelengths:
    dispersion.append(calculate_dispersion(i))

plt.plot( wavelengths,dispersion)
plt.ylabel("Dispersion (ps · nm^-1 km^-1)")
plt.xlabel("Wavelength (nm)")
plt.grid(True)
plt.show()

print(calculate_dispersion(1285),"\n",calculate_dispersion(1375)+ calculate_dispersion(1285))
print(calculate_dispersion(1375))

