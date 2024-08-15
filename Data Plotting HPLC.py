import numpy as np
import matplotlib.pyplot as plt
import os

# Daten definieren
x = np.array([1,2,5,10,30,60,120,180])





# Gruppe 1 AMP
y1_1 = np.array([0.285279618,	0.279094935,	0.266317787,	0.279361561,	0.272549522,	0.28437518,	0.28463135,	0.284427459])
y1_2 = np.array([0.288139315,	0.570632427,	0.588857114,	0.565686772,	0.570067807,	0.559371389,	0.552674366,	0.697332169])
y1_3 = np.array([0.331745774,	0.317405465,	0.301449715,	0.303922542,	0.300780535,	0.312726436,	0.330914528,	0.329189299])

# Gruppe 2 ADP
y2_1 = np.array([0.535955332,	0.518561891,	0.527616727,	0.51869259,	0.510082131,	0.51239812,	0.514159944,	0.52629928])
y2_2 = np.array([0.56808118,	0.55749455,	0.558069626,	0.535767126,	0.532342808,	0.560118988,	0.583503678,	0.676869913])
y2_3 = np.array([0.564933945,	0.571474129,	0.540189984,	0.529681774,	0.534930651,	0.725615462,	0.717005003,	0.80486619])

# Gruppe 3 ATP
y3_1 = np.array([17.14110801,	15.07507881,	14.92025262,	15.32845738,	14.50746815,	15.1405068,	15.24043936,	15.23232033])
y3_2 = np.array([19.74686191,	16.8225158,	16.79180673,	16.72913388,	16.72626373,	17.08084003,	15.33199149,	16.86398925])
y3_3 = np.array([18.16565854,	16.88792811,	15.4704071,	15.52908056,	15.75985341,	15.96061251,	16.18758986,	19.09118095])







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
plt.errorbar(x, y1_mean, yerr=y1_std, fmt='o', ecolor=color1, capsize=5, label='AMP', color=color1)
plt.plot(x, y1_mean, linestyle='-', marker='o', color=color1, linewidth=5)

# Plot für Gruppe ADP
plt.errorbar(x, y2_mean, yerr=y2_std, fmt='o', ecolor=color2, capsize=5, label='ADP', color=color2)
plt.plot(x, y2_mean, linestyle='-', marker='o', color=color2, linewidth=5)

# Plot für Gruppe ATP
plt.errorbar(x, y3_mean, yerr=y3_std, fmt='o', ecolor=color3, capsize=5, label='ATP', color=color3)
plt.plot(x, y3_mean, linestyle='-', marker='o', color=color3, linewidth=5)

# Plot-Details hinzufügen
plt.xlabel('Time [min]', fontsize = 20)
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

