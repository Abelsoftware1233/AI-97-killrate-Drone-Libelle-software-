# AI-97-killrate-Drone-Libelle-software-
Repository for the AI software 97%killrate software 
# Libel Jacht AI (Dragonfly Predator AI)

## 🎯 Doel
Dit project is een proof-of-concept voor het ontwikkelen van een Kunstmatige Intelligentie (AI) die de extreem hoge jachtsuccesrate (tot 97%) van de libel nabootst. De AI is ontworpen om de bewegingen van een prooi in 3D-ruimte te voorspellen en een geoptimaliseerde onderscheppingsbaan voor drones te berekenen met behulp van Machine Learning en Guidance Navigation Laws (Geleide Navigatie).

## ⚙️ Architectuur
Het systeem bestaat uit drie hoofdcomponenten die de Libel's zenuwstelsel nabootsen:

1.  **`data_simulator.py`**: Simuleert de chaotische 3D-vlucht van een prooi (de *Perceptie*).
2.  **`prediction_model.py`**: Bevat een conceptueel **LSTM** (Long Short-Term Memory) model dat de toekomst van de prooi voorspelt (het *Libel Brein*).
3.  **`guidance_controller.py`**: Implementeert een Proportionele Navigatie (PN)-achtige wet om de beste onderscheppingsbaan te berekenen (de *Vluchtcontrole*).
4.  **`main.py`**: Coördineert de simulatie en brengt alle modules samen.

## 🛠️ Vereisten (Prerequisites)

U heeft de volgende Python-bibliotheken nodig. Deze kunnen worden geïnstalleerd met `pip`.

```bash
pip install numpy
# Voor het Prediction Model (hoewel conceptueel in deze fase)
# pip install tensorflow
