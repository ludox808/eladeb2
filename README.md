# ELADEB-R Patient CLI

Ce dépôt contient un petit script Python (`patient_app.py`) simulant une auto‑évaluation inspirée de l'ELADEB-R.

## Exécution

1. Installez Python 3.
2. Lancez le script depuis un terminal :

```bash
python3 patient_app.py
```

Le programme vous posera des questions pour évaluer vos difficultés et vos besoins d'aide, puis affichera un récapitulatif.

## Version web

Une version web minimale est proposée dans `patient_web.py`. Elle nécessite
`Flask`. Installez-la (si besoin) puis lancez le serveur :

```bash
pip install flask
python3 patient_web.py
```

Ouvrez ensuite votre navigateur sur `http://localhost:5000` pour remplir le
formulaire d'auto‑évaluation.
