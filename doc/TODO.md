# Tâches à réaliser

Interface utilisateur
	> Menu permettant de paramétrer la simulation :
		> Sélection des paramètres de la simulation (population, virus, environnement,...)
		- Création personnalisée d'un virus qui sera stocké dans un fichier custom.JSON
	- Affichage des infos de la personne suite à un clic via une pop-up et remplaçant le graphique (top-right corner)

Ressources pour la simulation
	- Choix de 3 virus pour les templates et recueil de données epidémiologiques
	- 3 fichiers JSON caractérisant les virus

Traitement logique des personnes
	- Plusieurs comportements différents lié à l'environnement qui influencent le déroulement de l'épidémie (fou furieux,parano,normal,...)

Traitement logique de l'infection
	- Gestion de la distanciation sociale et du confinement

Traitement logique de la simulation
	> Classe simulation permettant d'initialiser la simu depuis le menu puis de l'arrêter avec un retour menu

Affichage graphique
	- Plusieurs environnements dans lesquels les personnes se déplacent et se comportent de façon différente
	> Graphique temps réel représentant la distribution des états (sain/infecté/soigné/mort) de la population de la simulation en cours
		+ Gestion des statistiques de la simulation
		+ Affichage des statistiques dans la fenêtre
		> Affichage du graphique (top-right corner)
	- Affichage détaillé des stats de la simulation une fois celle-ci arrêtée (affichage de transition avant le retour menu)

# Tâches accomplies 

(Lundi 18)
Affichage graphique
	- Rendre la gestion des collisions entre personnes plus naturelle et corriger les bugs
		- Refaire entièrement le système de collision en utilisant une classe Hitbox

(Dimanche 17)
Traitement logique de l'infection
	- Gestion de la mort/soin de façon déterministe lors de l'infection : calcul de la probabilité de mourir (en fonction de l'âge de la personne) puis déclenchement d'un timer (défini dans le JSON du virus) qui changera son état (à soigné ou mort) à son échéance
		- Changer la classe virus pour qu'elle gère la probabilité de mourrir selon l'age
		- Changer la fonction infection pour déterminer le dénouement d'une personne
		- Gérer les timer
	- Gestion des comorbidités sur la dangerosité du virus
	- Gestion des masques sur la propagation du virus
