import matplotlib.pyplot as plt
import numpy as np

# Generazione di dati casuali per il grafico a dispersione
np.random.seed(0)  # Imposta il seme per la riproducibilità dei risultati
x = np.random.rand(50)  # Genera 50 valori casuali per l'asse x
y = np.random.rand(50)  # Genera 50 valori casuali per l'asse y
colors = np.random.rand(50)  # Genera 50 valori casuali per i colori dei punti
sizes = 1000 * np.random.rand(50)  # Genera 50 valori casuali per le dimensioni dei punti

# Creazione del grafico a dispersione
plt.figure(figsize=(10, 6))  # Crea una nuova figura con dimensioni personalizzate
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
# Crea il grafico a dispersione con:
# - x: valori per l'asse x
# - y: valori per l'asse y
# - c: colori dei punti (usando la mappa di colori 'viridis')
# - s: dimensioni dei punti
# - alpha: trasparenza dei punti

# Aggiunta di una barra dei colori
plt.colorbar(label='Valori dei colori')  # Aggiunge una barra dei colori con un'etichetta

# Impostazione delle etichette degli assi e del titolo
plt.xlabel('Asse X')  # Imposta l'etichetta dell'asse x
plt.ylabel('Asse Y')  # Imposta l'etichetta dell'asse y
plt.title('Grafico a Dispersione con Colori e Dimensioni Variabili')  # Imposta il titolo del grafico

# Aggiunta di una griglia
plt.grid(True, linestyle='--', alpha=0.5)  # Aggiunge una griglia al grafico

# Visualizzazione del grafico
plt.show()  # Mostra il grafico creato