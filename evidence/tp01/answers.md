# TP01 - Réponses

## Partie A

**A1.** Le CSV, le modèle et le code n'ont pas le même rôle. Le CSV est la donnée brute de départ : on ne la modifie jamais pour savoir toujours ce qu'on a reçu. Le code explique comment on traite les données et comment on entraîne : on le versionne avec Git et on le fait relire. Le modèle est le résultat produit par le code sur les données : il peut être régénéré et il change à chaque entraînement, donc on ne le traite pas comme du code. Si on mélange les trois, on ne sait plus quelle donnée et quel code ont donné quel modèle.

**A2.** `Churn` est ce que le modèle doit prédire. Si on le met dans les entrées, on lui donne la réponse : c'est une fuite de la cible. Le modèle aurait de très bons scores en test mais ne servirait à rien en vrai, car on ne connaît pas `Churn` au moment où on veut savoir si un client va partir.

## Partie B2

1. Dans `pyproject.toml`, la contrainte Python est `requires-python = ">=3.11,<3.13"`, et une dépendance directe est `numpy~=1.26.0`.
2. Dans `uv.lock`, `numpy` est fixé à la version exacte `1.26.4`, qui respecte la contrainte précédente.
3. Avec `uv tree`, on voit que `pandas` utilise `python-dateutil`, qui utilise `six`. `six` est une dépendance transitive : je ne l'ai pas demandée moi-même.
4. `pyproject.toml` dit ce que le projet demande (des contraintes de versions). `uv.lock` garde les versions exactes choisies, pour que tout le monde installe la même chose. `.venv/` est l'installation réelle sur mon ordinateur : on peut la recréer à partir des deux autres, donc on ne la met pas dans Git.

## Partie C3

1. C'est une classification parce que `Churn` ne vaut que `Yes` ou `No` : on prédit une catégorie, pas un nombre.
2. Environ 73,5 % des clients ne partent pas. Un modèle qui répond toujours `No` aurait donc déjà environ 73 % d'accuracy sans repérer un seul client qui part. L'accuracy seule ne suffit pas, il faudra regarder aussi le rappel, la précision ou le F1.
3. Pandas lit une colonne comme du texte (`object`) dès qu'une valeur n'est pas convertible en nombre. Dans `TotalCharges`, 11 valeurs sont des blancs, donc toute la colonne est lue comme du texte.
4. Une valeur blanche est une chaîne de caractères, pas un `NaN`, donc `isna()` ne la détecte pas. Il faut enlever les espaces puis comparer à une chaîne vide, comme dans le script.
5. Le hash SHA-256 : si deux personnes ont le même hash, elles ont exactement le même fichier. Le nom du fichier ne prouve rien.

## Partie D2

## Partie D2

| Élément | Preuve produite dans TP01 | Limite restante |
|---|---|---|
| Code | Commit Git | Les modifications non commitées ne sont pas identifiées par ce commit |
| Versions de paquets | `pyproject.toml`, `uv.lock` | La plateforme et l'interpréteur peuvent changer l'installation |
| Environnement installé | Enregistrements avant/après (`environment-before.json`, `environment.json`) | Ne capture pas tous les détails de l'OS ni du matériel |
| Données sources | URL source et SHA-256 | N'établit pas la qualité des labels ni l'absence de fuite |
| Modèle entraîné | Non produit dans TP01 | Il faudra des preuves d'entraînement, de configuration et d'artefacts |

Constat après recréation de `.venv` : les versions de Python et des paquets (churnlab, pandas, numpy, scikit-learn) ainsi que le hash des données sont identiques avant et après.

## Partie E

- URL de la pull request : https://github.com/lovecoookie/churnlab-2026/pull/1
- Hash du commit : 37a5ace (commit du README), fusionné dans main par 49587af
- Relecture : réalisée par moi-même, TP fait seule

## Partie F

Avec `git restore README.md` (F1), la modification non indexée est annulée : ma phrase disparaît du fichier. Avec `git restore --staged README.md` (F2), je retire seulement le fichier de l'index, c'est-à-dire de ce qui était prévu pour le prochain commit, mais ma modification reste dans le fichier. F1 supprime le changement, F2 garde le changement et annule juste le `git add`.

## Limites de reproductibilité

Ce TP permet de recréer les versions de paquets et d'identifier les données grâce au hash. Il ne garantit pas des résultats identiques pour un futur entraînement : il manque encore les graines aléatoires, la configuration d'entraînement, la découpe des données, les artefacts du modèle, et les différences possibles de système ou de matériel.