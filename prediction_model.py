# prediction_model.py
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from data_simulator import simuleer_prooi_beweging # Vereist import voor self-test

def bereid_data_voor_lstm(posities, lookback=10, voorspel_vooruit=5):
    """
    Maakt tijdreeks-datasets voor LSTM. 
    X = sequentie van 'lookback' posities (input)
    Y = 'voorspel_vooruit' toekomstige positie (target)
    
    Args:
        posities (np.array): 3D posities van de prooi over tijd.
        lookback (int): Hoeveel stappen geschiedenis te gebruiken.
        voorspel_vooruit (int): Hoeveel stappen in de toekomst te voorspellen.
    
    Returns:
        tuple: (X_data, Y_data)
    """
    X, Y = [], []
    for i in range(len(posities) - lookback - voorspel_vooruit):
        # Input: De geschiedenis
        X.append(posities[i:(i + lookback), :])
        
        # Target: De positie die we proberen te voorspellen
        Y.append(posities[i + lookback + voorspel_vooruit - 1, :])
        
    return np.array(X), np.array(Y)

def maak_en_train_model(X_train, Y_train, epochs=10):
    """
    Definieert en traint het LSTM-model voor 3D-positie voorspelling.
    """
    
    # Controleer de input shape: [samples, timesteps, features]
    n_timesteps = X_train.shape[1]
    n_features = X_train.shape[2]
    
    model = Sequential([
        # LSTM layer: 64 neuronen, input shape gedefinieerd door de data
        LSTM(units=64, input_shape=(n_timesteps, n_features)),
        # Dense layer: 3 output units (x, y, z)
        Dense(units=3) 
    ])
    
    model.compile(optimizer='adam', loss='mse')
    
    print(f"\n--- Starten Model Training ({epochs} epochs) ---")
    
    # Train het model
    model.fit(X_train, Y_train, epochs=epochs, batch_size=32, verbose=1)
    
    print("Model training voltooid.")
    return model

if __name__ == '__main__':
    # ZELF-TEST VAN DE AI-COMPONENT
    
    # 1. Genereer een grote dataset (5000 stappen)
    print("Genereren van 5000 stappen aan prooi-bewegingsdata...")
    posities, _ = simuleer_prooi_beweging(stappen=5000, dt=0.01)
    
    # 2. Bereid data voor (gebruik 10 stappen geschiedenis om 5 stappen vooruit te voorspellen)
    LOOKBACK = 10
    VOORSPEL_VOORUIT = 5
    X_train, Y_train = bereid_data_voor_lstm(posities, lookback=LOOKBACK, voorspel_vooruit=VOORSPEL_VOORUIT)
    
    print(f"Gemaakte Trainingsdata: X={X_train.shape} Y={Y_train.shape}")
    
    # 3. Maak en train het model
    ai_model = maak_en_train_model(X_train, Y_train, epochs=1) # Eén epoch voor snelle demo
    
    # 4. Test een voorspelling
    # Pak een willekeurige sequentie uit de data om te testen
    test_sequence = X_train[0:1] 
    voorspelling = ai_model.predict(test_sequence)
    
    print("\n--- Voorspelling Test ---")
    print(f"Geschiedenis van 10 stappen (laatste punt): {test_sequence[0, -1]}")
    print(f"Werkelijke Toekomstige Positie (Y): {Y_train[0]}")
    print(f"Voorspelde Toekomstige Positie (AI): {voorspelling[0]}")
    
