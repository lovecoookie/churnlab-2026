# churnlab-2026

Projet de prédiction du churn pour le cours Machine Learning Operations (ESILV).

## Question métier et cible

Un opérateur télécom veut identifier les clients susceptibles de quitter son service. La colonne cible est `Churn` (`Yes` ou `No`). On prédit une catégorie : c'est une classification.

## Environnement

Python 3.11 (3.12 accepté). Les dépendances exactes sont fixées dans `uv.lock`.

```sh
uv sync --locked
uv run python -c "import churnlab; print(churnlab.__version__)"
```

Attendu : `0.1.0`.

## Données

- Source : IBM Telco Customer Churn, [fichier épinglé à un commit](https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/1fd6fd70906479be1712e64cfc0ea89f58466629/data/Telco-Customer-Churn.csv)
- SHA-256 : `16320c9c1ec72448db59aa0a26a0b95401046bef5d02fd3aeb906448e3055e91`
- Le CSV brut n'est pas dans Git. Pour l'obtenir et vérifier son hash : `uv run python scripts/download_data.py`
- Inspection : `uv run python scripts/inspect_telco.py` (7 043 lignes, 21 colonnes, 1 869 `Yes` et 5 174 `No`)

## Organisation du projet

| Dossier | Rôle |
|---|---|
| `src/churnlab/` | Code importable du projet |
| `scripts/` | Commandes exécutables (téléchargement, inspection, enregistrement de l'environnement) |
| `data/raw/` | Données d'origine non modifiées et métadonnées de source |
| `evidence/tp01/` | Preuves et réponses du TP01 |

## Limites

Ce jeu de données est un instantané des clients à un moment donné. Ce n'est pas un journal d'événements daté, ni une expérience où des clients auraient reçu un traitement de rétention tiré au hasard. On ne peut donc pas en déduire l'effet d'une action commerciale, ni reconstituer l'historique d'un client.

Le hash identifie les octets du fichier, mais ne prouve pas la qualité des labels. Recréer l'environnement ne garantit pas à lui seul des résultats d'entraînement identiques.