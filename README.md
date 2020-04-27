## Organisation
[Trello](https://trello.com/b/DPv9ow8F/ppro0403)

## Commandes git
### Mettre à jour le contenu du dépôt local avec celui du dépôt distant
> git pull

### Envoyer sur le dépôt distant les modifications (Toujours mettre à jour son dépôt local avant d'envoyer)  
> git add .  
> git commit -m "message décrivant le contenu des modifications"  
> git push

# Simulation de la propagation d’un virus

## Sujet
L’idée est de se baser sur les simulations publiées par le Washington Post pendant l’épidémie du COVID-19. Le projet doit permettre de produire plusieurs scénarios qui montrent la propagation du virus en fonction de divers critères : la mobilité des individus, la durée des contacts, le rassemblement dans des lieux précis (magasin d’alimentation ou bureaux de vote).

## Plan de travail
Dans un premier temps, peut-être que certain(e)s n'ont pas encore travaillé sur Python et sur la bibliothèque graphique (on part sur Pygame ?). Si c'est le cas, il faut déjà récupérer toute la documentation nécessaire (liens vers la documentation, tutoriels, etc.).

Dans un deuxième temps, il faut être capable de réaliser le même type d'interface que celui proposé dans l'article (des petits ronds qui se déplacent). Une fois que l'interface sera faite, nous pourrons adapter la simulation. Comment ? A vous de réfléchir là-dessus.

Dans un troisième temps, il faut réfléchir aux simulations que l'on souhaite faire. L'objectif est de partir sur des critères et il est nécessaire qu'ils puissent être configurables (par exemple avant de lancer la simulation). Je donne quelques exemples, mais il y a plein de possibilités : est-ce qu'un individu est infecté dès qu'il est touché ? Ou bien y'a-t-il une probabilité ? Le contact ou un rayon autour de l'individu ? Comment se déplacent les individus ? Peut-on limiter certains à une zone et d'autres non ? Peut-on obliger les individus à aller à un endroit régulièrement ? etc. Je vous rappelle qu'il y a un deuxième groupe qui travaille sur le même sujet. Soyez inventifs !

## Ressources 


[Article Washington Post](https://www.washingtonpost.com/graphics/2020/world/corona-simulator/?fbclid=IwAR2fR0DmKt411g-nQkPCfiriesyZcGDR6ovSnXiA4qRm4nx6XcGHlRHGieY)

[Video Simulation de l'évolution du COVID-19](https://www.youtube.com/watch?v=hrLrEfP2Wjo&fbclid=IwAR1tauuZLSBlKuAiWRztkthoEDdMkmZjWyJeH1aR0bIbxp3HRPBA25wW4b8)

[Logiciel de simulation de propagation d'un virus](https://github.com/angeluriot/Disease_propagation?fbclid=IwAR1JoR2a45tnGa-Nbj9WESWnBDD5pP1XYJIYFQ68PyFz8HqEdZGxO0XqTPs)

[Taux d’actes médicaux SOS Médecins pour suspicion de Covid-19](https://www.data.gouv.fr/fr/datasets/taux-dactes-medicaux-sos-medecins-pour-suspicion-de-covid-19-pour-10-000-actes-medicaux/)

[Taux d'hospitalisation parmi les passages aux urgences pour suspicion de Covid-19](https://www.data.gouv.fr/fr/datasets/taux-dhospitalisation-parmi-les-passages-aux-urgences-pour-suspicion-de-covid-19/)

[Taux de passage aux urgences pour suspicion de Covid-19](https://www.data.gouv.fr/fr/datasets/taux-de-passages-aux-urgences-pour-suspicion-de-covid-19/)
