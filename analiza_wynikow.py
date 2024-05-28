import fnmatch
import math
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

d = 72E-9  # nm
print(d)
print(type(d))
source = os.getcwd()
print(source)
list_of_files = fnmatch.filter(os.listdir('.'), '*.txt')  # used files
print(list_of_files)
data = pd.read_fwf(source + '\\' + list_of_files[0], skiprows=1, header=None)
print(data)
data.columns = ['λ[nm]', 'TRANSMISSION']
print(data)
wavelengths = data['λ[nm]']
print(wavelengths)
print(data['TRANSMISSION'])

print(list_of_files[1:])
for file in list_of_files[1:]:
    temp = pd.read_fwf(source + '\\' + list_of_files[0], skiprows=1, header=None)
    temp.columns = ['λ[nm]', 'TRANSMISSION']
    data['TRANSMISSION'] += temp['TRANSMISSION']

data['TRANSMISSION'] = data['TRANSMISSION'] / len(list_of_files)
average_transmission = data['TRANSMISSION']
print(average_transmission)

plt.xlabel("wavelengths [nm]")
plt.ylabel("average transmission (0-1)")
plt.title('T(λ)')
plt.plot(wavelengths, average_transmission)
plt.show()

alpha = []  # container for alpha values
for i in range(len(average_transmission)):
    alpha.append((1 / d * math.log(1 / average_transmission[i])))

energies = 1240 / wavelengths
alpha_hv = alpha * energies ** 0.5

plt.plot(energies, alpha_hv)
plt.xlabel("energies [eV]")
plt.ylabel("SiN Tauc plot alfa^1/2")
plt.title('Checking the energy bandgap')
plt.xlim(3, 5)
plt.show()

# fitting the linear curve
condition = len(energies) == len(alpha_hv)
assert condition is True

energies_for_fit = [energies[x] for x in range(len(energies)) if 3.97 < energies[x] < 4.762]
alpha_hv_for_fit = [alpha_hv[x] for x in range(len(energies)) if 3.97 < energies[x] < 4.762]

coef = np.polyfit(energies_for_fit, alpha_hv_for_fit, 1)


a, b = coef[0].tolist(), coef[1].tolist()

energies_fit = [-b/a]
alpha_fv_fit = [0]

energies_fit += sorted(energies_for_fit)

for i in range(1,energies_fit.__len__()):
    alpha_fv_fit.append(a*energies_fit[i]+b)

print(energies_fit,alpha_fv_fit)

plt.plot(energies_for_fit, alpha_hv_for_fit)
plt.plot(energies_fit,alpha_fv_fit, color='green')
plt.title('Finding Eg in range (4 - 4.60 eV)')
plt.xlabel('energy (eV)')
plt.title('part of tauc plot')
plt.ylabel('SiN Tauc plot alfa^1/2')
plt.ylim(bottom = 0 )
plt.show()

print(f'Eg:{-coef[1] / coef[0]}')
