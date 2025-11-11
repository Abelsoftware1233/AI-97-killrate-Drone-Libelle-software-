# main.py
import numpy as np
import time

# Importeren van de modules
# Merk op: In een echt project moeten 'prediction_model.py' en 'data_simulator.py'
# ook bestaan om dit te laten werken.
from data_simulator import simuleer_prooi_beweging
from prediction_model import bereid_data_voor_lstm, maak_en_train_model 
from guidance_controller import bereken_onderscheppingsversnelling

# --- SIMULATIE PARAMETERS ---
TIJD_STAPPEN_TOTAAL = 100 
DT = 0.01  # Tijdstap in seconden

def run_jacht_simulatie():
    """Voert één gesimuleerde jachtsequentie uit."""
    
    print("--- 🧠 Starten van Libel Jacht-AI Simulatie ---")
    
    # 1. Initiele Data Voorbereiding & Training (Eenmalig)
    print("\n[STAP 1/4] Genereren van trainingsdata...")
    historische_posities, _ = simuleer_prooi_beweging(stappen=5000)
    
    # In een echt project zou u hier het model trainen.
    # X_train, Y_train = bereid_data_voor_lstm(historische_posities)
    # model = maak_en_train_model(X_train, Y_train) 
    # print("Model klaar voor voorspelling.")
    
    # 2. De Jacht Start
    drone_positie = np.array([5.0, 5.0, 2.0])  # Startpositie van de drone (Jager)
    drone_snelheid = np.array([0.0, 0.0, 0.0])
    
    # Genereer de prooi-baan voor de huidige run
    prooi_posities_run, prooi_snelheden_run = simuleer_prooi_beweging(stappen=TIJD_STAPPEN_TOTAAL, dt=DT)

    print("\n[STAP 2/4] Jacht gestart. Drone Positie:", drone_positie)
    
    for t in range(TIJD_STAPPEN_TOTAAL):
        prooi_huidige_pos = prooi_posities_run[t]
        
        # --- KERN VAN DE AI: VOORSPELLING ---
        # In een echte implementatie zou u de laatste 5 metingen van de prooi gebruiken om 
        # de toekomstige positie te voorspellen. Hier gebruiken we voor de demo de ECHTE 
        # toekomstige positie van de prooi (t+5 stappen) als perfecte voorspelling.
        
        voorspelde_prooi_pos = prooi_posities_run[min(t + 5, TIJD_STAPPEN_TOTAAL - 1)] 
        
        # --- BEREKENING VAN DE ONDERSCHEPPING ---
        versnelling_commando = bereken_onderscheppingsversnelling(
            drone_positie, 
            voorspelde_prooi_pos, 
            drone_snelheid
        )
        
        # --- UPDATE DRONE FYSICA ---
        drone_snelheid += versnelling_commando * DT
        drone_positie += drone_snelheid * DT
        
        # --- CONTROLE OP VANGST ---
        afstand = np.linalg.norm(drone_positie - prooi_huidige_pos)
        
        if afstand < 0.1: # Vangstraal van 10 cm
            print(f"\n[STAP 4/4] 🎯 SUCCES! Prooi gevangen op tijdstap {t} ({t*DT:.2f}s).")
            print(f"Laatste Afstand: {afstand:.3f}m")
            return
        
        if t % 10 == 0:
            print(f"Tijd: {t*DT:.2f}s | Afstand tot Prooi: {afstand:.3f}m | Commando: {versnelling_commando}")

    print("\n[STAP 4/4] ❌ MISLUKT. Prooi ontsnapt.")
    print(f"Laatste Afstand: {afstand:.3f}m")


if __name__ == '__main__':
    run_jacht_simulatie()
  
