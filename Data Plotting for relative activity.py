import matplotlib.pyplot as plt
import numpy as np
import os

# Beispiel-Daten für drei Gruppen mit je drei Datensätzen
data = {
    '50µg': [0.520049034,		0.409764858,	    1.166688144],
    '10µg': [0.882486351,		0.744235182,		1.21238736],
    '1µg': [3.341701588,		4.231698506,		3.842104875]
}





labels = list(data.keys())
values = [np.mean(data[label]) for label in labels]
errors = [np.std(data[label]) for label in labels]
colors = ['blue', 'orange', 'green']

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
bars = plt.bar(np.arange(len(labels)), values, yerr=errors, color=colors, capsize=5)

# Achsenbeschriftungen und Titel
plt.xticks(np.arange(len(labels)), labels, fontsize=20)

# Achsenskalierung (Tick-Labels) anpassen
plt.tick_params(axis='y', labelsize=16)  # y-Achse
plt.tick_params(axis='x', labelsize=16)  # x-Achse (optional, falls du die Schriftgröße für die X-Achse anpassen möchtest)


# Pfad zum Speichern definieren
save_path = 'D:/Platereader/Balkendiagramm&Fehlerbars.png'

# Ordner erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Plot speichern
plt.savefig(save_path)

# Plot anzeigen
plt.show()