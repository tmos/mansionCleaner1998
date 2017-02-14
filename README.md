# Mansion Cleaner 1998
Clean your mansion, seamlessly.

![mansionCleaner1998](https://github.com/tmos/mansionCleaner1998/blob/master/assets/mansion_cleaner.png)

## Introduction

Mansion Cleaner 1998 is a script that emulate the behavior of a cleaner robot in a big mansion. It uses Artificial Intelligence to be the most effective possible.

The python code is organised in 3 classes :

1. Game.py : the global controller ;
2. Mansion.py : the mansion ;
3. Robot.py : the robot.


* 😎 : Hal, the cleaner robot
* 💩 : A piece of dust
* 💍 : A jewel ring
* 🍪 : Both a ring and some dust

## Installation 

MC1998 uses Python 3.5. Here is the installation process :

Requirements :
* Python 3.5.x
* Pip
* UNIX terminal

Check if you have Virtualenv installed :

`bash$ python -m venv`

If it doesn't work, you have to install Virtualenv :

`$ pip install --user virtualenv`

Once installed, go inside the project folder, and :

`$ source bin/activate`

Now, you just have to install the dependencies :

`$ pip install -r requirements.txt`

And launch the Mansion Cleaner :

`$ python mansion_cleaner_1998.py`

## The agent

### Exploration and planification
To explore and plan his actions, the agent starts with scanning his environnement. Those elements are now his new targets. For each target, the robot then looks for the best path. It uses the A star algorithm. For each iteration, the robot get the best path that have the highest number of items (jewels or dust). To do so, we have played with the weight of each item (empty, dust, ring, dust and ring).

Once the agent have the path list to each target, he will define wich one is the most pertinent at the moment. Basicaly, it will be the one that have the biggest amount of items on its way, the shortest A star score, and that respect the movement limitations of the robot (check out the performance measurements section).

### Mental state
L’état mental de l’agent est implémenté dans la fonction live() de Robot.py. Cette fonction est simplement une boucle infinie qui exécute les capteurs et effecteurs de l’agent selon des critères définis. À chaque itération, le fonctionnement de la boucle est le suivant :

1. Le robot vérifie qu’il lui reste des actions prévues (la quantité d’actions prévues est limitée par la mesure de performance, cf le titre suivant).
2. S’il lui reste des actions prévues, il exécute la première de la pile
3. Si la liste d’actions est vide :
   1. Il vérifie que de nouvelles cibles sont apparues, auquel cas :
      1. Il calcule le meilleur chemin à parcourir
      2. puis réalise le premier mouvement de ce chemin

### Performance measurements
Pour améliorer la performance de l’agent, un mesure de performance. En fonction de l’action effectuée par le robot, un bonus/malus permettra de mettre à jour sa performance. Ainsi :

* À chaque scan de l’environnement, la performance diminue de 2 points ;
* À chaque déplacement, la performance diminue d’1 point ;
* À chaque bonne action[2], la performance augmente de 10 points ;
* À chaque mauvaise action[3], la performance diminue de 100 points.

La mesure de performance ainsi calculée permet d’influer sur le nombre de mouvements possibles au prochain tour. Le nombre de mouvement est obtenu par la formule `performance/10`
