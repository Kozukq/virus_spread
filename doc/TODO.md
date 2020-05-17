# Tâches à réaliser

Interface utilisateur
	- Menu permettant de paramétrer la simulation
	- Affichage des infos de la personne suite à un clic via une pop-up

Ressources pour la simulation
	- Choix de 3 virus pour les templates et recueil de données epidémiologiques
	- 3 fichiers JSON caractérisant les virus

Traitement logique des personnes
	- Plusieurs comportements différents lié à l'environnement qui influencent le déroulement de l'épidémie (fou furieux,parano,normal,...)

Traitement logique de l'infection
	- Gestion de la mort/soin de façon déterministe lors de l'infection : calcul de la probabilité de mourir (en fonction de l'âge de la personne) puis déclenchement d'un timer (défini dans le JSON du virus) qui changera son état (à soigné ou mort) à son échéance
	- Gestion des masques et protections sur la propagation du virus
	- Gestion de la distanciation sociale et du confinement

Affichage graphique
	- Rendre la gestion des collisions entre personnes plus naturelle et corriger les bugs
	- Plusieurs environnements dans lesquels les personnes se déplacent et se comportent de façon différente
	- Graphique temps réel représentant la distribution des états (sain/infecté/soigné/mort) de la population de la simulation en cours

# Tâches accomplies
