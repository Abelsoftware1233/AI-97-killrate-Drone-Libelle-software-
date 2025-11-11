# main.py
import numpy as np
import time

# Importeren van de modules (vereist dat deze bestanden in dezelfde map staan)
# In deze simulatie gebruiken we de data_simulator om zowel training als de 
# "perfecte" voorspelling (voor demonstratie) te genereren.
from data_simulator import simuleer_prooi_beweging
from guidance_controller import bereken_onderscheppingsversnelling

# Let op: De prediction_model module wordt in de main.py niet direct voor runtime 
# voorspelling gebruikt, omdat dit een complexe integratie van data I/O is. 
# We simuleren hier een perfecte voorspelling voor een werkende jachtloop.

# --- SIMULATIE PARAMETERS ---
TIJD_STAPPEN_TOTAAL = 500  # Aantal simulatiestappen
DT = 0.01                 # Tijdstap in seconden

def run_jacht_simulatie():
    """Voert één gesimuleerde jachtsequentie uit."""
    
    print("--- 🧠 Starten van Libel Jacht-AI Simulatie ---")
    
    # 1. Initialisatie
    drone_positie = np.array([5.0, 5.0, 2.0])  # Startpositie van de drone
    drone_snelheid = np.array([0.0, 0.0, 0.0])
    
    # Genereer de prooi-baan voor de huidige run (de 'echte' beweging)
    prooi_posities_run, _ = simuleer_prooi_beweging(stappen=TIJD_STAPPEN_TOTAAL, dt=DT)

    print(f"\n[INFO] Jacht gestart. Drone Positie: {drone_positie}")
    
    for t in range(TIJD_STAPPEN_TOTAAL):
        prooi_huidige_pos = prooi_posities_run[t]
        
        # --- KERN VAN DE AI: VOORSPELLING ---
        # Voor deze simulatielus: We simuleren een perfecte voorspelling door
        # de positie 5 stappen (5*0.01s) in de toekomst te gebruiken.
        VOORSPELLING_STAPPEN = 5
        voorspeld_index = min(t + VOORSPELLING_STAPPEN, TIJD_STAPPEN_TOTAAL - 1)
        voorspelde_prooi_pos = prooi_posities_run[voorspeld_index] 
        
        # --- BEREKENING VAN DE ONDERSCHEPPING (Guidance Controller) ---
        versnelling_commando = bereken_onderscheppingsversnelling(
            pos_drone=drone_positie, 
            pos_prooi_voorspeld=voorspelde_prooi_pos, 
            snelheid_drone=drone_snelheid
        )
        
        # --- UPDATE DRONE FYSICA ---
        drone_snelheid += versnelling_commando * DT
        drone_positie += drone_snelheid * DT
        
        # --- CONTROLE OP VANGST ---
        afstand = np.linalg.norm(drone_positie - prooi_huidige_pos)
        
        if afstand < 0.2: # Vangstraal van 20 cm
            print(f"\n[RESULTAAT] 🎯 SUCCES! Prooi gevangen op tijdstap {t} ({t*DT:.2f}s).")
            print(f"Laatste Afstand: {afstand:.3f}m")
            return
        
        if t % 50 == 0:
            print(f"Tijd: {t*DT:.2f}s | Afstand tot
            
