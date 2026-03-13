# Observations

## Investigation 

- Human Computer Interaction

Ne connaissant pas grand chose au sujet, j'ai fait appel à l'intelligence Artificielle pour défricher un petit peu le sujet


:::::::{dropdown} Usage IA

::::::{tab-set}

:::::{tab-item} Prompt

- **Outil**: Perplexity
- **Date**: 10/03/2026
- **Iteration**: 1

Je cherche a définir une problématique de recherche dans le domaine de human computer interaction. Je souhaite étudier la possibilté d'adopter une posture de documentaliste / publisher pour les jeunes chercheurs grace a l'utilisation d'outils open-source tel que python, markdown, sphinx et github. Fais moi un état de l'art et génère moi plusieurs problématique de cherche qui explore des territoires inexplorés !

:::::

:::::{tab-item} Réponse complète

Voici d’abord un état de l’art synthétique, puis une série de problématiques de recherche formulées comme de vraies questions de thèse ou de projet.

## 1. État de l’art (HCI, jeunes chercheurs, posture éditoriale)

Dans l’Interaction Homme‑Machine, la problématique centrale est de concevoir des médiations entre les capacités humaines (perception, cognition, action, communication) et les systèmes informatiques, en s’appuyant sur des méthodes de conception, de prototypage et d’évaluation rigoureuses, souvent participatives et pluridisciplinaires. Les travaux récents insistent sur l’importance d’observer les interactions en situation plutôt que de se focaliser uniquement sur les interfaces, afin de dégager des propriétés interactionnelles plus générales. [books.openedition](https://books.openedition.org/editionscnrs/30758?lang=fr)

Parallèlement, les études sur les pratiques numériques des jeunes chercheurs montrent que cette génération s’inscrit dans un écosystème de communication scientifique en mutation profonde : plateformes numériques, réseaux sociaux académiques, open access, exigences de science ouverte et circulation rapide des résultats. Ces travaux décrivent des usages (Google Scholar, dépôts, réseaux sociaux) mais très peu la conception par les jeunes chercheurs eux‑mêmes d’« infrastructures éditoriales » open‑source dédiées à leur propre travail (sites, documentations, pipelines de publication). [books.openedition](https://books.openedition.org/editionsehess/28848?lang=en)

En sciences humaines et sociales, des recherches analysent les pratiques autour des documents numériques (conservation, diffusion, usages, transmission) et les enjeux de la numérisation et des plateformes d’édition scientifique. D’autres travaux sur les plateformes de science ouverte étudient l’usage, la navigation, l’appropriation et la diffusion des contenus, en mobilisant fouille de données, APIs et méthodes computationnelles pour comprendre l’influence de ces infrastructures sur les contenus et les publics. On voit émerger l’idée que les outils numériques (plateformes, scripts, APIs) deviennent eux‑mêmes des objets pour faire de la sociologie ou de l’étude des pratiques scientifiques, mais le rôle de « jeune chercheur‑éditeur/documentaliste » outillé par Python/Markdown/Sphinx/GitHub reste peu exploré. [lab.hypotheses](https://lab.hypotheses.org/3141)

Côté bibliothèques et science ouverte, de nombreux guides et dispositifs outillent les chercheurs pour mieux gérer leurs données, choisir des revues ouvertes, ou comprendre les enjeux de l’ouverture des publications. Cependant, ces ressources visent principalement à accompagner l’usage de services existants plutôt qu’à étudier la conception par les jeunes chercheurs de chaînes de production éditoriales open‑source intégrées à leurs pratiques de recherche. Cela ouvre un espace de recherche HCI sur les workflows « do‑it‑yourself » où le jeune chercheur devient co‑designer de son environnement documentaire et éditorial. [bibliotheques.univ-montp3](https://bibliotheques.univ-montp3.fr/boite-a-outils-recherche)

## 2. Axes conceptuels pour ta posture « documentaliste / publisher »

Ces constats permettent de structurer ton sujet autour de plusieurs axes HCI :

- **Jeune chercheur comme designer d’infrastructure** : passer de l’utilisateur de plateformes (journaux, HAL, OpenEdition) au concepteur de micro‑infrastructures (dépôt GitHub, site Sphinx, documentation versionnée, data‑paper auto‑généré).  
- **Chaîne de publication reproducible** : articuler Python (scripts d’analyse, notebooks), Markdown (contenus), Sphinx (génération de documentation, sites, API docs) et Git/GitHub (versionning, collaboration, CI) comme une chaîne éditoriale qui sert à la fois la production scientifique, la documentation de la recherche et la médiation vers d’autres publics.  
- **Posture de documentaliste numérique** : classification, métadonnées, conservation, circulation, mise en contexte des ressources (datasets, scripts, carnets de labo) dans un environnement contrôlé par le chercheur, en dialogue ou en tension avec les services institutionnels et commerciaux. [popups.uliege](https://popups.uliege.be/2030-1456/index.php?id=282&file=1&pid=262)
- **Expérience utilisateur (UX) de la documentation** : penser la documentation (Sphinx, README, tutoriels) comme une interface HCI à part entière pour les pairs, les étudiants et les non‑spécialistes : navigation, repérage, lisibilité, affordances, feedback, etc. [lri](https://www.lri.fr/~mbl/pdf/mbl-enjeux05.pdf)
- **Science ouverte et publics multiples** : analyser comment ces chaînes open‑source modifient l’accessibilité, la réutilisation et la visibilité des travaux, et comment elles reconfigurent les relations avec les plateformes de science ouverte existantes. [books.openedition](https://books.openedition.org/editionsehess/28848?lang=en)

Sur cette base, tu peux formuler des problématiques qui explorent des terrains encore peu investis et positionner ton travail à l’intersection HCI – études des pratiques scientifiques – documentation.

## 3. Problématiques de recherche (niveau thèse / projet)

Je te propose plusieurs familles de problématiques. Tu peux en combiner deux pour faire un projet original.

### A. Posture éditoriale et transformation des pratiques de recherche

1. Comment la conception et l’usage d’une chaîne éditoriale open‑source (Python + Markdown + Sphinx + GitHub) transforment‑ils la manière dont les jeunes chercheurs produisent, organisent et partagent leurs connaissances au quotidien (carnet de labo, préprints, code, données) ?  
2. En quoi l’adoption d’une posture de **documentaliste numérique** par les jeunes chercheurs reconfigure‑t‑elle leurs relations aux infrastructures institutionnelles de publication (revues, archives ouvertes, bibliothèques universitaires) et aux plateformes commerciales (réseaux sociaux académiques) ?  
3. Comment la mise en place de workflows éditoriaux reproducibles influence‑t‑elle la réflexivité des jeunes chercheurs sur leurs méthodes et leurs choix théoriques, par rapport à des pratiques de publication plus « classiques » (article PDF finalisé seulement) ?  

### B. HCI de la documentation scientifique conçue par les chercheurs

4. Quelles propriétés d’interaction (navigation, repérage, rétroaction, appropriation) caractérisent les sites et documentations de recherche créés avec Sphinx/GitHub par les jeunes chercheurs, et comment ces propriétés influencent‑elles l’expérience des utilisateurs (pairs, étudiants, non‑spécialistes) ?  
5. Comment concevoir, dans une perspective HCI, des gabarits et composants interactifs pour Sphinx ou Markdown qui soutiennent explicitement la compréhension des méthodes, la réutilisation des données et la reproductibilité des analyses ?  
6. Quelles tensions apparaissent entre les bonnes pratiques HCI (simplicité, charge cognitive réduite) et les exigences de traçabilité, de complétude et de transparence propres à la science ouverte dans des documentations pilotées par les jeunes chercheurs ?  

### C. Design participatif et co‑construction de chaînes éditoriales

7. Comment impliquer des jeunes chercheurs de disciplines variées dans des démarches de conception participative pour co‑designer des workflows éditoriaux open‑source adaptés à leurs contraintes, et quelles formes de médiation (ateliers, prototypes, guides) sont les plus efficaces ? [books.openedition](https://books.openedition.org/editionscnrs/30758?lang=fr)
8. Quels modèles de collaboration émergent lorsque des bibliothécaires/documentalistes, des ingénieurs HN (humanités numériques) et des jeunes chercheurs co‑construisent et maintiennent une infrastructure éditoriale basée sur GitHub, et comment ces modèles affectent‑ils la durabilité de l’infrastructure ?  
9. Comment évaluer, dans une perspective HCI, l’impact de ces chaînes éditoriales co‑conçues sur la charge de travail perçue, le sentiment d’autonomie et la capacité des jeunes chercheurs à se projeter dans des pratiques de science ouverte à long terme ?  

### D. Infrastructures, science ouverte et publics

10. En quoi les micro‑infrastructures éditoriales créées par les jeunes chercheurs (sites de projets, doc de code, carnets de labo ouverts) complètent‑elles ou concurrencent‑elles les grandes plateformes de publication scientifique en accès ouvert, du point de vue des usages et des publics visés ? [lab.hypotheses](https://lab.hypotheses.org/3141)
11. Comment les métadonnées, indexations et vocabulaires contrôlés définis « à la main » par des jeunes chercheurs‑documentalistes dans des dépôts GitHub/Sphinx influencent‑ils la trouvabilité et la réutilisation de leurs travaux par différents publics (académiques/non académiques) ?  
12. Quels scénarios d’« écologie des plateformes » peut‑on imaginer où les chaînes éditoriales open‑source individuelles s’articulent avec les dépôts institutionnels, les catalogues de bibliothèques et les archives ouvertes, et quelles implications cela a‑t‑il pour la conception des interfaces de ces différents systèmes ?  

### E. Méthodes d’observation des interactions avec les chaînes éditoriales

13. Comment développer une méthodologie HCI centrée sur l’observation des interactions avec des chaînes éditoriales reproductibles (consultation de doc, fork GitHub, exécution de notebooks) plutôt que seulement sur l’interface finale, afin de dégager une « physique des interactions » propres à la documentation scientifique ? [arxiv](https://arxiv.org/pdf/2510.06156.pdf)
14. Quelles combinaisons de méthodes (journaux de bord, logs, analyses de parcours, entretiens, tests utilisateurs) permettent le mieux de caractériser les usages réels des documentations Sphinx/GitHub créées par des jeunes chercheurs, et de relier ces usages à des choix de design concrets ?  
15. Comment les métriques classiques du web (pages vues, temps passé, rebonds) doivent‑elles être adaptées ou complétées pour évaluer la qualité interactionnelle de ressources documentaires scientifiques produites dans des workflows open‑source ?  

## 4. Comment choisir et resserrer ta problématique

Pour converger vers une problématique « territoire inexploré », tu peux :

- Choisir un cadre : par exemple, jeunes chercheurs en SHS à l’ère de la science ouverte (Fort lien avec les travaux sur plateformes et documents numériques). [popups.uliege](https://popups.uliege.be/2030-1456/index.php?id=282&file=1&pid=262)
- Fixer une infrastructure cible : Python + Markdown + Sphinx + GitHub comme chaîne éditoriale expérimentale.  
- Définir le point de vue HCI : expérience des usagers des docs, processus de conception participative, ou observation des interactions avec la chaîne plus que l’interface.  

Par exemple, une formulation consolidée pourrait être :  

> « Comment la co‑conception par des jeunes chercheurs de chaînes éditoriales open‑source basées sur Python, Markdown, Sphinx et GitHub transforme‑t‑elle leurs pratiques de documentation et de partage des résultats, et quelles propriétés d’interaction favorisent la compréhension et la réutilisation des travaux par différents publics ? »  

Si tu veux, tu peux me dire dans quel contexte disciplinaire et à quel niveau (M2, doctorat) tu te situes, et je t’aiderai à resserrer une problématique et à esquisser un plan de mémoire.

:::::


::::::

:::::::


```{note}

Reprendre le bon formattage du drop (penser à le citer dans les annexes), faire un tab item avec les différents niveaux d'explorations de l'IA et reprendre un a un ci dessous les différents éléments introduits.

```

## Biblio 

```{note}

Je met ici les liens que j'ai exploré, il faudra les lire et extraire les informations pertinentes

```

- [Interface Homme machine](https://books.openedition.org/editionscnrs/30758?lang=fr)

- [Les pratiques numériques des jeunes chercheurs](https://books.openedition.org/editionsehess/28848?lang=en)


### Projets

- [Harbinger Research Project]()
