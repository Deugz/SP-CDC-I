---
title: 4.A Documentation
myst:
  html_meta:
    "description lang=fr": |
      Documentation du projet 4.A
html_theme.sidebar_secondary.remove: true
---

```{toctree}
:maxdepth: 4
:hidden:

content/I-Presentations/Presentations-main
```

```{toctree}
:maxdepth: 4
:hidden:

content/II-Analyse/Analyse-main
```

```{toctree}
:maxdepth: 4
:hidden:

content/III-Identitee/Identitee-main
```

```{toctree}
:maxdepth: 4
:hidden:

content/IV-Conception/Conception-main
```

```{toctree}
:maxdepth: 4
:hidden:

content/V-Dev/Dev-main
```

```{toctree}
:maxdepth: 4
:hidden:

content/VI-Marketing/Marketing-main
```

```{toctree}
:maxdepth: 4
:hidden:

content/VII-Com/Com-main
```

<br>

```{image} _static/title/journal-de-prod.svg
:width: 100%

```

***

<br>
<br>

# Projet 4.A 

<br>
<br>

<p class="p-dial"><em>"Un ensemble de solutions numériques open sources et gratuites, permettant à tout <strong>Artisan de la connaissance</strong>, d'écrire et de partager le <strong>récit vivant de ses apprentissages</strong> !"</em></p>

## Abstract

::::{grid} 3

:::{grid-item}
:columns: 5

<br>
<br>

>À l’heure où les grandes plateformes numériques structurent les conditions de création, de publication et de diffusion des connaissances, le projet 4.A propose une alternative scientifique, créative et gratuite de la **construction du savoir**, fondée sur la maîtrise des outils open-source suivant : Python, Markdown, Sphinx et GitHub. Il introduit le concept de *récit vivant d’apprentissage* comme outil méthodologique pour nourrir et développer la [pensée complexe](https://fr.wikipedia.org/wiki/Pens%C3%A9e_complexe#:~:text=La%20pens%C3%A9e%20complexe%20est%20un,'une%20%C3%A0%20l'autre.) à l'échelle individuelle et collective. 

:::

:::{grid-item}
:columns: 7

<div class="lottie-container">

<script
  src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.3/dist/dotlottie-wc.js"
  type="module"
></script>
<dotlottie-wc id="lottie-adjust" src="https://lottie.host/42426f9c-6360-4be9-928f-9a2ce2261974/cFz9k2UlDH.lottie" style="width: 200%; left: -44%;" autoplay loop></dotlottie-wc>

</div>

:::

::::



### La Pensée Complexe ?

<br>
<br>

::::::{tab-set}

:::::{tab-item} Mes Opinions

<div class="index-tab" id="indexTab">

<button class="btn-complexity" id="btn-complexity-toggleBtn">Changer l’image</button>

<script>
const button = document.getElementById("btn-complexity-toggleBtn");
const container = document.getElementById("indexTab");

let state = 0; // 0 = image par défaut

button.addEventListener("click", () => {
  
  // Reset des classes
  container.classList.remove("alt-bg-1", "alt-bg-2");

  // Avance d’un état
  state++;

  if (state === 1) {
    container.classList.add("alt-bg-1");
  } 
  else if (state === 2) {
    container.classList.add("alt-bg-2");
  } 
  else {
    state = 0; // Retour à l’image initiale
  }

});
</script>


<br>
<br>
<br>
<br>

::::{grid} 
:gutter: 3

:::{grid-item}

:::


:::{grid-item-card}
:link: https://deugz.github.io/SP-CDC-I/build/html/content/I-Presentations/1-Me/2-Opinions/1-Numerique/Numerique.html
:class-header: bg-light
:link-alt: clickable cards
:columns: 2
**Numérique**
^^^

```{image} _static/svg/Index-page/numerique-symbol-green.svg
:width: 100%
:align: center


```

:::

:::{grid-item}


:::

::::


::::{grid} 5

:::{grid-item}
:columns: 

:::


:::{grid-item-card}
:link: https://deugz.github.io/SP-CDC-I/build/html/content/I-Presentations/1-Me/2-Opinions/4-Democratie/Democratie.html
:class-header: bg-light
:link-alt: clickable cards
:columns: 2
**Démocratie**
^^^

```{image} _static/svg/Index-page/societe-symbol-green.svg
:width: 100%
:align: center


```

:::

:::{grid-item}
:columns: 3


:::

:::{grid-item-card}
:link: https://deugz.github.io/SP-CDC-I/build/html/content/I-Presentations/1-Me/2-Opinions/2-Education/Education.html
:class-header: bg-light
:link-alt: clickable cards
:columns: 2
**Education**
^^^

```{image} _static/svg/Index-page/education-symbol-green.svg
:width: 100%
:align: center

```

:::

:::{grid-item}
:columns: 

:::

::::

::::{grid}
:gutter: 3


:::{grid-item}


:::

:::{grid-item-card}
:link: https://deugz.github.io/SP-CDC-I/build/html/content/I-Presentations/1-Me/2-Opinions/3-Science/Science.html
:class-header: bg-light
:link-alt: clickable cards
:columns: 2
**Science**
^^^

```{image} _static/svg/Index-page/science-symbol-green.svg
:width: 100%
:align: center


```

:::

:::{grid-item}


:::

::::

<br>
<br>
<br>
<br>
<br>

</div>

:::::

:::::{tab-item} Valeurs

```{note}

A faire, une fois que le format général est mis en place 


```

:::::

:::::{tab-item} Besoins

```{note}

A faire, une fois que le format général est mis en place 


```

:::::

:::::{tab-item} Offre

```{note}

A faire, une fois que le format général est mis en place 


```

:::::

:::::{tab-item} Vision

```{note}

A faire, une fois que le format général est mis en place 


```

:::::

::::::


### Plusieurs Niveaux d'Explorations


```{note}

Format flashcard avec des informations sur les différents niveaux
- niveau 1
- niveau 2
- niveau 3

p-emphase pour introduire le niveau 4 dans le sommaire ci-dessous

```

#### 4. le Temps


## Sommaire

```{note}

Explication rapide de comment intéragir avec la figure

- créer un bouton floatant en ccs qui ouvre un tooltip au survol ?

```

<iframe 
    src="_static/Python-Processing/Arbo-site/output/Arborescence-site.html"
    width="100%" 
    height="900"
    frameborder="0">
</iframe>

<br>

(dropdown-reflexion-Elan-1)=
:::::{dropdown} 💪 Comment j'ai fait ça ? (pas en une fois je te rassure)
:class-container: dropdown-arrow



- tab processing python

```{note}

explication interaction excel-python

- Lien vers GDP

```


:::::



### Documentation Numérique Itérative

```{note}

Intégrer vidéo gource de première grosse itération (version alpha -> beta)

```


#### Petite Parenthèse UI / UX

```{note}

Explication des différents éléments, liens vers les listes et explication du passage de diplome CDUI

```




### Quelle(s) récit(s) ?

```{note}

Bulle vidéo avec ma tête ?

- explication des différentes méthode de communication (newsletter production - site wordpress w/ blog)

- Agent IA nourrie de la documentation ?

- [Wikicommute](https://wikicommute.vercel.app/?ref=medianes.org)
    - Inclure et faire lien dans benchmark technologique

```


#### Les Bonnes Pages

## Introduction

Quand je commence l’écriture de ce journal, en décembre 2025, je le fais avec l’idée de raconter une histoire singulière, mon histoire, qui prend racine dans un parcours éducatif riche, divers et semé d'embûches. Cette histoire est la source de mon projet, un projet complexe, multidimensionnel, que je n’ai pu discuter de manière holistique qu'à de très rares occasions, avec un nombre très limité de personnes. C’est donc avec un immense plaisir et en même temps un peu d’appréhension que j’écris ces premières lignes. J’ai l’intention de le faire avec une grande liberté (qui me caractérise) et l’envie de partager ce qui m’anime.

### Sections