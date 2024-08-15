import matplotlib.pyplot as plt
import numpy as np
import os

# Beispiel-Daten für drei Gruppen mit je drei Datensätzen
data = {
    '50µg': [0.075602925, 0.15541231, 0.069624064],
    '10µg': [0.128292806, 0.282267517, 0.072351241],
    '5µg': [0.145376532, 0.379271934, 0.05967667],
    '1µg': [0.485804989, 1.604964478, 0.229284026]
}





labels = list(data.keys())
values = [np.mean(data[label]) for label in labels]
errors = [np.std(data[label]) for label in labels]
colors = ['blue', 'orange', 'red', 'green']

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
bars = plt.bar(np.arange(len(labels)), values, yerr=errors, color=colors, capsize=5)

# Achsenbeschriftungen und Titel
plt.ylabel(r'nmol$\cdot$min$^{-1}$$\cdot$$\mu$g$^{-1}$', fontsize=20)
plt.xticks(np.arange(len(labels)), labels)


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