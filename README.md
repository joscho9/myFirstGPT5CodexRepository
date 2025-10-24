# myFirstGPT5CodexRepository

Dieses Repository enthält ein Skript zur Erstellung eines medizinisch motivierten synthetischen Datensatzes, der den Zusammenhang des systolischen Blutdrucks mit Alter, BMI und weiteren Einflussgrößen mit nichtlinearen Komponenten modelliert.

## Datensatz erzeugen

```bash
python data/generate_medical_dataset.py -o data/medical_dataset.csv
```

Standardmäßig werden 50 Zeilen mit den folgenden Variablen generiert:

- `age` – Alter in Jahren
- `bmi` – Body-Mass-Index
- `sodium_intake_g` – tägliche Natriumaufnahme in Gramm
- `exercise_minutes_per_week` – Minuten körperlicher Aktivität pro Woche
- `stress_score` – subjektiver Stresslevel (1–10)
- `systolic_blood_pressure` – resultierender systolischer Blutdruck in mmHg

Die Blutdruckwerte entstehen aus einer nichtlinearen Kombination der Faktoren inklusive sinusförmiger und logarithmischer Komponenten sowie zufälligem Rauschen.
