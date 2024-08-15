import pandas as pd
import matplotlib.pyplot as plt
import os

# Funktion zum Einlesen und Plotten der Daten
def plot_excel_data(file_path, save_folder, start_value, end_value):
    # Lesen der Excel-Datei
    df = pd.read_excel(file_path)
    
    # Annehmen, dass die erste Spalte 'X' und die zweite Spalte 'Y' heißt
    x = df.iloc[:, 0]  # Erste Spalte
    y = df.iloc[:, 1]  # Zweite Spalte

    # Filtern der Daten basierend auf dem Start- und Endwert der x-Achse
    filtered_df = df[(df.iloc[:, 0] >= start_value) & (df.iloc[:, 0] <= end_value)]
    x_filtered = filtered_df.iloc[:, 0]
    y_filtered = filtered_df.iloc[:, 1]

    # Erstellen des Diagramms
    plt.figure(figsize=(10, 6))
    plt.plot(x_filtered, y_filtered, linestyle='-', color='b', linewidth=5)  # Linie ohne Punkte
    plt.xlabel('mL', fontsize=20)
    plt.ylabel('mAU', fontsize=20)
    plt.grid(True)


    # Achsenskalierung (Tick-Labels) anpassen
    plt.tick_params(axis='y', labelsize=16)  # y-Achse
    plt.tick_params(axis='x', labelsize=16)  # x-Achse (optional, falls du die Schriftgröße für die X-Achse anpassen möchtest)


   

    # Überprüfen, ob der Ordner existiert, und erstellen, falls nicht
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Speichern des Diagramms im gewählten Ordner
    save_path = os.path.join(save_folder, '2024-06-28-ÄktaPure-Run2.png')
    plt.savefig(save_path)
    plt.show()

    print(f"Diagramm gespeichert in: {save_path}")

# Beispielaufruf der Funktion
file_path = 'D:\\Äkta\\Pure Test.xlsx'  # Pfad zu Ihrer Excel-Datei
save_folder = 'D:\\Äkta\\Akta Pure\\Plots'  # Pfad zum Speicherordner
start_value = 5  # Startwert für die x-Achse
end_value = 15  # Endwert für die x-Achse

plot_excel_data(file_path, save_folder, start_value, end_value)