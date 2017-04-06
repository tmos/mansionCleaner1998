# Mansion Cleaner 1998
Clean your mansion, seamlessly.

<img src="https://github.com/tmos/mansionCleaner1998/blob/master/assets/mansion.gif" height="400">

## Introduction

Mansion Cleaner 1998 is a script that emulate the behavior of a cleaner robot in a big mansion. It uses Artificial Intelligence to be the most effective possible.

The python code is organised in 3 classes:

1. `Game.py`: the global controller
2. `Mansion.py`: the mansion
3. `Robot.py`: the robot

* 😎 : Hal, the cleaner robot
* 💩 : A piece of dust
* 💍 : A jewel ring
* 🍪 : Both a ring and some dust

## Installation 

MC1998 uses Python 3.5. Here is the installation process:

Requirements:
* Python 3.5.x
* Pip
* UNIX terminal

Check if you have Virtualenv installed:

`bash$ python -m venv`

If it doesn't work, you have to install Virtualenv:

`$ pip install --user virtualenv`

Once installed, go inside the project folder, and:

`$ source bin/activate`

Now, you just have to install the dependencies:

`$ pip install -r requirements.txt`

And launch the Mansion Cleaner:

`$ python mansion_cleaner_1998.py`

## The agent

### Exploration and planification
To explore and plan his actions, the agent starts with scanning his environnement. Those elements are now his new targets. For each target, the robot then looks for the best path. It uses the A star algorithm. For each iteration, the robot get the best path that have the highest number of items (jewels or dust). To do so, we have played with the weight of each item (empty, dust, ring, dust and ring).

Once the agent have the path list to each target, he will define wich one is the most pertinent at the moment. Basicaly, it will be the one that have the biggest amount of items on its way, the shortest A star score, and that respect the movement limitations of the robot (check out the performance measurements section).

### Mental state
The agent's mental state is implemented into the `live()` function of `Robot.py`. This function is simply an infinite loop which executes the agent's sensors and effectors, according to the defined criteria. At each iteration, the loop works as follows:

1. The robot checks that there are still scheduled actions (the quantity of scheduled actions is limited by the perform measure, see the following title) ;
2. If there are still scheduled actions, the robot executes the first action of the pile ;
3. If the actions list is empty:
   1. The robot checks that new targets appeared, in which case:
      1. It calculates the best path to travel ;
      2. Then it performs the first move of this path.

### Performance measurements
In order to optimize the agent's performance, a measure is considered. Depending on the action performed by the robot, a bonus/malus will affect its performance. Then:

* At each environment scan, the performance decreases of 2 points ;
* At each move, the performance decreases of 1 point ;
* At each good action[2], the performance increases of 10 points ;
* At each bad action[3], the performance decreases of 100 points.

Thanks to the performance measure, we can act on the number of possible move allowed on the next turn. The number of moves is obtained with the formula `performance/10`
