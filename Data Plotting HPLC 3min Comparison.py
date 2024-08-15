import numpy as np
import matplotlib.pyplot as plt
import os

# Daten definieren
x = np.array([15 , 30 , 45 , 60 , 90 , 120 , 180])



# Gruppe Cocktail 3min
y1_1 = np.array([96.58332593,	42.33955113,	38.20252615,	27.52925831,	20.67690651,	20.99585422,	18.59654745,])
y1_2 = np.array([40.02913545,	39.17971131,	36.38412476,	30.95829129,	28.14725087,	27.5969866,	26.56254476,])
y1_3 = np.array([66.44684989,	45.78331129,	44.18031776,	30.60706612,	23.9501984,	22.90502355,	22.55336446,])

# Gruppe MgATP 3min
y2_1 = np.array([20.39496233,	28.18366888,	26.22432154,	19.61884995,	17.03475551,	16.2373444,	15.39464343,	])
y2_2 = np.array([28.20891473,	23.70722871,	25.36941849,	20.05484136,	17.06504635,	16.45494278,	15.19072663,])
y2_3 = np.array([23.20751363,	22.65328133,	22.57449589,	20.55328604,	20.49113598,	19.4338584,	18.8178054,])

# Gruppe Doppelt 3min
y3_1 = np.array([22.417819,	22.75222581,	22.77601305,	22.03221995,	22.13854108,	21.90136398,	22.54321175,	])
y3_2 = np.array([26.63599768,	26.05638884,	24.33364875,	24.26294575,	22.81425562,	20.96329968,	16.33478845,])
y3_3 = np.array([35.86364421,	32.00393666,	25.97546516,	22.05669729,	17.93871779,	17.47873525,	15.73304963,])







# Mittelwert und Standardabweichung berechnen
y1_mean = np.mean([y1_1, y1_2, y1_3], axis=0)
y1_std = np.std([y1_1, y1_2, y1_3], axis=0)

y2_mean = np.mean([y2_1, y2_2, y2_3], axis=0)
y2_std = np.std([y2_1, y2_2, y2_3], axis=0)

y3_mean = np.mean([y3_1, y3_2, y3_3], axis=0)
y3_std = np.std([y3_1, y3_2, y3_3], axis=0)

# Plot erstellen
plt.figure(figsize=(10, 8))

# Farben für die Punkte festlegen
color1 = 'red'
color2 = 'green'
color3 = 'blue'

# Plot für Gruppe AMP
plt.errorbar(x, y1_mean, yerr=y1_std, fmt='o', ecolor=color1, capsize=5, label='Cocktail', color=color1)
plt.plot(x, y1_mean, linestyle='-', marker='o', color=color1,linewidth=5)

# Plot für Gruppe ADP
plt.errorbar(x, y2_mean, yerr=y2_std, fmt='o', ecolor=color2, capsize=5, label='MgATP', color=color2)
plt.plot(x, y2_mean, linestyle='-', marker='o', color=color2,linewidth=5)

# Plot für Gruppe ATP
plt.errorbar(x, y3_mean, yerr=y3_std, fmt='o', ecolor=color3, capsize=5, label='3.0', color=color3)
plt.plot(x, y3_mean, linestyle='-', marker='o', color=color3,linewidth=5)
# Plot-Details hinzufügen
plt.xlabel('Time [sec]', fontsize = 20)
plt.ylabel('Amount [nmol]', fontsize = 20)
plt.legend(fontsize = 16)
plt.grid(True)


# Achsenskalierung (Tick-Labels) anpassen
plt.tick_params(axis='y', labelsize=16)  # y-Achse
plt.tick_params(axis='x', labelsize=16)  # x-Achse (optional, falls du die Schriftgröße für die X-Achse anpassen möchtest)


# Pfad zum Speichern definieren
save_path = 'D:\HPLC\Geplottete Daten und Graphen/plot_mit_fehlerindikatoren.png'

# Ordner erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Plot speichern
plt.savefig(save_path)


# Plot anzeigen
plt.show()

