import matplotlib.pyplot as plt
import numpy as np
import os

# Beispiel-Daten, die dem hochgeladenen Diagramm ähneln
labels = [r'12mM MgSO$_4$', r'12mM MgSO$_4$', r'12mM MgCl$_2$']
values = [0.128292806, 0.122056471, 0.143413741]
colors = ['blue', 'orange', 'green']

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
bars = plt.bar(np.arange(len(labels)), values, color=colors)

# Achsenbeschriftungen und Titel
plt.ylabel(r'nmol$\cdot$min$^{-1}$$\cdot$$\mu$g$^{-1}$', fontsize=20)
plt.xticks(np.arange(len(labels)), labels, fontsize=20)

# Achsenskalierung (Tick-Labels) anpassen
plt.tick_params(axis='y', labelsize=16)  # y-Achse
plt.tick_params(axis='x', labelsize=16)  # x-Achse (optional, falls du die Schriftgröße für die X-Achse anpassen möchtest)


# Pfad zum Speichern definieren
save_path = 'D:\Platereader/Balkendiagramm.png'

# Ordner erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Plot speichern
plt.savefig(save_path)


# Plot anzeigen
plt.show()