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
	- Gestion de la distanciation sociale et du confinement

Affichage graphique
	- Rendre la gestion des collisions entre personnes plus naturelle et corriger les bugs
		- Refaire entièrement le système de collision en utilisant une classe Hitbox
	- Plusieurs environnements dans lesquels les personnes se déplacent et se comportent de façon différente
	> Graphique temps réel représentant la distribution des états (sain/infecté/soigné/mort) de la population de la simulation en cours
		+ Gestion des statistiques de la simulation
		- Affichage des statistiques dans la fenêtre
		- Affichage du graphique

# Tâches accomplies 

(Dimanche 17)
Traitement logique de l'infection
	- Gestion de la mort/soin de façon déterministe lors de l'infection : calcul de la probabilité de mourir (en fonction de l'âge de la personne) puis déclenchement d'un timer (défini dans le JSON du virus) qui changera son état (à soigné ou mort) à son échéance
		- Changer la classe virus pour qu'elle gère la probabilité de mourrir selon l'age
		- Changer la fonction infection pour déterminer le dénouement d'une personne
		- Gérer les timer
	- Gestion des comorbidités sur la dangerosité du virus
	- Gestion des masques sur la propagation du virus
