# Handleiding: Opzetten en Uitvoeren van het Libel Jacht AI Project

Dit document bevat de stappen om de Libel Jacht AI-simulatie te installeren en uit te voeren met behulp van de Python-scripts in uw repository (data_simulator.py, prediction_model.py, guidance_controller.py en main.py).

---

## STAP 1: Project Voorbereiden (Installatie)

1.  **Python Controle:** Zorg ervoor dat Python 3.x is geïnstalleerd op uw systeem.
2.  **Bestandsstructuur:** Bevestig dat alle vier de Python-bestanden (inclusief main.py) in dezelfde map staan.
3.  **Vereisten Installeren:** Open uw terminal (op Windows, Mac of Linux), navigeer naar uw projectmap en installeer de benodigde bibliotheek.

    ```bash
    pip install numpy
    # OPTIONEEL: Voor toekomstige ML-training
    # pip install tensorflow
    ```

---

## STAP 2: De Simulatie Uitvoeren

1.  **Start het Hoofd-Script:** Voer het main.py bestand uit vanuit uw terminal. Dit script coördineert de data-generatie, voorspellingsoproep en vluchtcontrole-berekening.

    ```bash
    python main.py
    ```

2.  **Analyseer de Output:** De terminal toont de voortgang van de jachtsequentie. Let op de volgende informatie in de output:
    * **Tijd:** De gesimuleerde tijd in seconden.
    * **Afstand tot Prooi:** De afstand (in meters) tussen de drone en de prooi.
    * **Commando:** Het 3D-versnellingscommando (acceleratie in m/s²) dat naar de drone zou worden gestuurd.

---

## STAP 3: Resultaten Interpreteren

De simulatie eindigt met één van de twee resultaten:

### A. Succesvolle Vangst:
Dit betekent dat de drone's Guidance Controller erin geslaagd is om binnen de gedefinieerde vangstraal (0.1m) van de prooi te komen, dankzij de voorspelling.

### B. Mislukte Vangst:
Dit geeft aan dat de prooi te snel of te onvoorspelbaar was, of dat de **Navigatie Constante (N)** in guidance_controller.py aangepast moet worden.

---

## STAP 4: Optimalisatie en Aanpassing

Om de nauwkeurigheid en snelheid van de jacht te testen, kunt u de volgende parameters in de scripts aanpassen:

| Bestand | Parameter om aan te passen | Doel van de aanpassing |
| :--- | :--- | :--- |
| **`data_simulator.py`** | **`random.uniform`** bereik | Maakt de prooibeweging meer of minder chaotisch (moeilijkheidsgraad). |
| **`guidance_controller.py`** | **`N` (Navigatie Constante)** | Regelt hoe agressief de drone stuurt. Hoger = agressiever sturen. |
| **`main.py`** | **`TIJD_STAPPEN_TOTAAL`** | De totale lengte van de simulatie. |
| **`main.py`** | **`voorspelde_prooi_pos`** lijn | Verander de perfecte voorspelling (t+5) naar een minder nauwkeurige voorspelling om de invloed van AI-fouten te testen. |
