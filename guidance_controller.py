# guidance_controller.py
import numpy as np

def bereken_onderscheppingsversnelling(pos_drone, pos_prooi_voorspeld, snelheid_drone, N=4.0):
    """
    Berekent de vereiste versnelling (in m/s^2) om de prooi te onderscheppen.
    Gebaseerd op het principe van Proportionele Navigatie (PN).
    
    Args:
        pos_drone (np.array): Huidige 3D-positie van de drone.
        pos_prooi_voorspeld (np.array): 3D-positie van de prooi in de nabije toekomst.
        snelheid_drone (np.array): Huidige 3D-snelheid van de drone.
        N (float): Navigatie Constante (typisch 3-5).
        
    Returns:
        np.array: Het 3D-versnellingscommando.
    """
    
    # 1. Zichtlijn Vector (Line-of-Sight)
    R_vec = pos_prooi_voorspeld - pos_drone
    R_mag = np.linalg.norm(R_vec)  
    R_unit = R_vec / R_mag        
    
    # 2. Vereenvoudigde sturing in de richting van het voorspelde punt
    # Dit zorgt voor sturing naar het onderscheppingspunt.
    
    # De versnelling moet de drone's snelheid aanpassen (sturen) naar de richting van het doel.
    # Dit is een vereenvoudigde 'Steer-to-Intercept' methode.
    
    gewenste_snelheid_richting = R_unit * np.linalg.norm(snelheid_drone) 
    
    # Het commando is het verschil tussen de gewenste en de huidige snelheid, geschaald met N
    versnelling_commando = (gewenste_snelheid_richting - snelheid_drone) * N 
    
    return versnelling_commando

if __name__ == '__main__':
    # Voorbeeld run
    drone_p = np.array([0.5, 0.5, 1.5]) # Drone positie
    prooi_p_next = np.array([2.0, 1.0, 1.2]) # Voorspelde prooi positie
    drone_v = np.array([3.0, 0.0, 0.0]) # Drone snelheid
    
    acc = bereken_onderscheppingsversnelling(drone_p, prooi_p_next, drone_v)
    
    print("--- Guidance Controller Test ---")
    print(f"Huidige Drone Positie: {drone_p}")
    print(f"Voorspelde Prooi Positie: {prooi_p_next}")
    print(f"Vereist Versnellings Commando: {acc}")
  
