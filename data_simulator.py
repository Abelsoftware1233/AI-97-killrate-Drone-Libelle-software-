# data_simulator.py
import numpy as np
import random

def simuleer_prooi_beweging(stappen=100, dt=0.01):
    """
    Genereert een reeks 3D-posities (x, y, z) en snelheden voor de prooi.
    De beweging omvat willekeurige versnellingen om een realistische vlucht na te bootsen.
    """
    posities = np.zeros((stappen, 3))
    snelheden = np.zeros((stappen, 3))
    
    # Initiele positie
    posities[0] = [0.1, 0.1, 1.0] 
    
    for i in range(1, stappen):
        # Voeg ruis/willekeurige versnelling toe om de vlucht realistischer te maken
        versnelling = np.array([
            random.uniform(-0.5, 0.5), 
            random.uniform(-0.5, 0.5), 
            random.uniform(-0.5, 0.5)
        ])
        
        # Snelheid en positie update met Euler integratie
        snelheden[i] = snelheden[i-1] + versnelling * dt
        posities[i] = posities[i-1] + snelheden[i] * dt
        
    return posities, snelheden

if __name__ == '__main__':
    posities, snelheden = simuleer_prooi_beweging(stappen=200)
    print("--- Prooi Beweging Simulatie Data ---")
    print(f"Eerste 5 posities:\n{posities[:5]}")
    print(f"Vorm van de data: {posities.shape}")
  
