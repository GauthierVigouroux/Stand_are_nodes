# Stand_are_nodes

Visualisation de l'éco-système normatif autour des cartes de navigations sous forme de nuage de points.

## TODO List

1. Création du docker Python avec son Dockerfile (ou compose)
    + ~Setup environnement de travail~
        + Faire un lien symbolique entre mon docker et mon système pour ne pas avoir à recompiler
        + ~Merge la branche proxyon et master~
2. ~Développement du script PARSE_HTML~
    + ~Utiliser une projet déjà existant pour gagner du temps de dev~
    + ~On est dans le cadre du WebScrapping, il existe plusieurs framework python~
        + ~Création d'une branch pour l'utilisation de scrappy.~
        + ~Utilisation de HTML_PARSE (fork)~
3. Test base de données
4. Rajout docker neo4j
5. PROCESS : Entrée = ~Liste ISO 19100 (nom norme, URL)~ //Un .json surement
    -> Scrapping.py
        - ~Mise sous forme de dictionnaire de la liste~
            - ~Parcours du dictionnaire~
            - ~Récupération de l'HTML/Rendu JavaScript~
            - ~Scrapping de la liste des normes avec lien correspondant (ou non suivant si présent ou non dans le papier)~
                - ~Avec une forme normalisé des noms pour éviter les doublons~
        - ~Renvoi du dictionnaire.~
    -> FeedNodes.py
        - fonction init:
            - Parcours du dictionnaire :
                -Si norme non présente dans la bdd = Création du Nodes
        - fonction link:
            - Parcours du dictionnaire :
                - Si pas de relation présente = Création de la relation (Voir pour rewrite, plus simple)
                - Prévoir un message d'erreur donnant la liaison qui n'a pas pu être crée
