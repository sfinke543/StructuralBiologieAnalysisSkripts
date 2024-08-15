import numpy as np
import matplotlib.pyplot as plt
import os

# Daten definieren
x = np.array([1, 2, 5, 10, 30, 60, 120, 180])

# Gruppe ATP Cocktail
y1_1 =  np.array([0.267771161,	0.316516711,	0.292881079,	0.307712817,	2.712012296,	5.205134908,	6.973248501,	7.254601917])
y1_2 = np.array([0.604493959,	0.560929323,	0.613308309,	0.565399234,	2.2098819,	    4.91525468,	    7.237532609,	7.822792884])
y1_3 = np.array([2.072741911,	2.732965982,	3.965312449,	5.00125994,	    6.985183946,	8.064586285,	8.776907031,	8.983181635])



# Gruppe ATP MgATP
y2_1 = np.array([0.531229252,	0.713643421,	1.284119009,	1.875271201,	3.708436368,	4.561985372,	5.716952724,	5.408748477	])
y2_2 = np.array([1.387345187,	1.571745984,	2.514285416,	3.325582003,	4.930520339,	6.07469717,	6.623596945,	6.71015114	])
y2_3 = np.array([2.072741911,	2.732965982,	3.965312449,	5.00125994,	6.985183946,	8.064586285,	8.776907031,	8.983181635	])





# Gruppe ATP 2.0
y4_1 = np.array([0.532536243,	0.513694655,	0.530408461,	0.517265356,	0.540247492,	0.538956184,	0.570569691,	0.572143309])
y4_2 = np.array([0.966661264,	0.842256599,	0.876850046,	0.989434282,	1.108276392,	1.403698263,	1.894745372,	2.391752362])
y4_3 = np.array([0.670753193,	0.549354608,	0.553463788,	0.579509512,	0.5929297,	0.538971868,	0.736599418,	0.863597154])



# Gruppe ATP 3.0
y5_1 = np.array([0.535955332,	0.518561891,	0.527616727,	0.51869259,	0.510082131,	0.51239812,	0.514159944,	0.52629928])
y5_2 = np.array([0.56808118,	0.55749455,	0.558069626,	0.535767126,	0.532342808,	0.560118988,	0.583503678,	0.676869913])
y5_3 = np.array([0.564933945,	0.571474129,	0.540189984,	0.529681774,	0.534930651,	0.725615462,	0.717005003,	0.80486619])





# Mittelwert und Standardabweichung berechnen
y1_mean = np.mean([y1_1, y1_2, y1_3], axis=0)
y1_std = np.std([y1_1, y1_2, y1_3], axis=0)

y2_mean = np.mean([y2_1, y2_2, y2_3], axis=0)
y2_std = np.std([y2_1, y2_2, y2_3], axis=0)


y4_mean = np.mean([y4_1, y4_2, y4_3], axis=0)
y4_std = np.std([y4_1, y4_2, y4_3], axis=0)

y5_mean = np.mean([y5_1, y5_2, y5_3], axis=0)
y5_std = np.std([y5_1, y5_2, y5_3], axis=0)

# Plot erstellen
plt.figure(figsize=(10, 8))

# Farben für die Punkte festlegen
color1 = 'red'
color2 = 'green'
color3 = 'blue'
color5 = 'black'

# Plot für Gruppe ATP Cocktail
plt.errorbar(x, y1_mean, yerr=y1_std, fmt='o', ecolor=color1,  capsize=5, label='Cocktail', color=color1)
plt.plot(x, y1_mean, linestyle='-', marker='o', color=color1, linewidth=5)

# Plot für Gruppe ATP MgATP
plt.errorbar(x, y2_mean, yerr=y2_std, fmt='o', ecolor=color2, capsize=5, label='MgATP', color=color2)
plt.plot(x, y2_mean, linestyle='-', marker='o', color=color2, linewidth=5)



# Plot für Gruppe ATP 2.0
plt.errorbar(x, y4_mean, yerr=y4_std, fmt='o', ecolor=color3, capsize=5, label='2.0', color=color3)
plt.plot(x, y4_mean, linestyle='-', marker='o', color=color3, linewidth=5)

# Plot für Gruppe ATP 3.0
plt.errorbar(x, y5_mean, yerr=y5_std, fmt='o', ecolor=color5, capsize=5, label='3.0', color=color5)
plt.plot(x, y5_mean, linestyle='-', marker='o', color=color5, linewidth=5)





# Plot-Details hinzufügen
plt.xlabel('Time [min]', fontsize = 20)
plt.ylabel('Amount [nmol]', fontsize = 20)
plt.legend(fontsize = 16)
plt.grid(True)

# Achsenskalierung (Tick-Labels) anpassen
plt.tick_params(axis='y', labelsize=16)  # y-Achse
plt.tick_params(axis='x', labelsize=16)  # x-Achse (optional, falls du die Schriftgröße für die X-Achse anpassen möchtest)


# Pfad zum Speichern definieren
save_path = 'D:/HPLC/Geplottete Daten und Graphen/plot_mit_fehlerindikatoren.png'

# Ordner erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Plot speichern
plt.savefig(save_path)

# Plot anzeigen
plt.show()