# Multi Ordi

```{note}

Insérer des captures d'écran de ce que la réponse du terminal pour chaque étape avec des explications approfondies

```

## Process

L'hébergement sur Github permet le travail sur plusieurs ordinateurs (en local), à partir de la meme version hébergé en ligne.

### Récupérer les changements

```PowerShell

git fetch origin

```

Cette commande récupère les nouveaux commits depuis GitHub sans les fusionner.

Il est ensuite possible de voir les différences :


```PowerShell

git log HEAD..origin/main --oneline

```

Si des commits apparaissent, c’est que ton ordi A n’a pas encore intégré les changements.

### Fusionner les changements

```PowerShell

git pull origin main

```

pull = fetch + merge

```{note}

Expliquer les différentes commandes ci-dessus

```

Après ça, ta branche locale sera à jour avec les changements de l’ordi B.
