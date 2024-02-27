# AiCore_Projects
This repo contains several different projects.

<!-- TABLE OF CONTENTS -->
<details> 
  <summary>Table of Contents</summary> 
  <ol> 
    <li> <a href="#Hangman">Hangman</a> 
      <ul> 
        <li><a href="#installation">Installation</a></li> 
        <li><a href="#usage">Usage</a></li> 
        <li><a href="#customization">Customization</a></li> 
      </ul> 
    </li> 
    <li> 
      <a href="#Rock-Paper-Scissors">Rock Paper Scissors</a>
        <ul> 
          <li><a href="#installation">Installation</a></li> 
          <li><a href="#usage">Usage</a></li> 
          <li><a href="#customization">Customization</a></li> 
      </ul> 
    </li> 
  </ol> 
</details> 

## Hangman
A simple game of hangman. 
The game allows a player to guess letters in order to find a randomly chosen word from a list of words. 
Players have a limited number of lives (5), and each incorrect guess results in the loss of a life. The objective of the game is to guess the word before running out of lives.


#### Installation
Import random package:
`import random`

#### Usage
To play the Hangman game, follow these steps:
- Clone the repository to your local machine.
- Open a terminal
- Run the following command to start the game:
`python milestone_5.py`
- The game will prompt you to make a guess by entering a single alphabetical character.
- Continue making guesses until you either guess the word or run out of lives.
- If you guess the word correctly, you win the game. If you run out of lives, you lose the game.

#### Customization
You can customize the game by modifying the word list in the play_game function. Simply replace the words in the word_list parameter with your own words. 
The game will randomly select a word from the list for each round.

## Rock Paper Scissors
A game of rock paper scissors between the user and the computer.
The game can be played with a simple manual user entry or by using a webcam and an image model for user input.
The game allows a player to choose from rock, paper or scissors.
The computer chooses from the same options at random.


#### Installation
The following steps are for Mac M1 chip users.  
First, create a virtual environment by running the following commands:  
`conda create -n tensorflow-env python=3.9`  
`conda activate tensorflow-env`  
`conda install pip`  
`python -m pip install tensorflow`  
`python -m pip install tensorflow-metal`  

More details on the installation of tensorflow and tensorflow-metal can be found at this link: https://developer.apple.com/metal/tensorflow-plugin/  
The link contains some helpful code to test that the installation is working correctly.  

Once you get tensorflow for Mac, you will install opencv for Mac by running the following commands:

`conda install -c conda-forge opencv`  
`pip install ipykernel`

Run the following file to check that the mode works as expected: https://aicore-files.s3.amazonaws.com/Foundations/Python_Programming/RPS-Template.py  

Import cv2 package: `import cv2`  
Import load_model from keras package: `from keras.models import load_model`  
Import numpy package: `import numpy as np`  
Import time package: `import time`  
Import random package: `import random`  

#### Usage
To play the manual baseed Rock Paper Scissors game, follow these steps:
- Clone the repository to your local machine.
- Open a terminal
- Run the following command to start the game:
`python manual_rps.py`
- The game will prompt you to make a choice by entering a rock, paper or scissors.
- The computer will make the same choice ay random.
- If you beat the computer you win the game.

To play the computer vision based Rock Paper Scissors game, follow these steps:
- Clone the repository to your local machine.
- Open a terminal
- Run the following command to start the game:
`python camera_rps.py`
- The game will prompt you to make a choice by making a gesture towards your webcam in 5 seconds. The keras model will interpret this into rock, paper or scissors.
- The computer will make the same choice ay random.
- If you beat the computer you get a point, if the computer beats you it gets a point.
- The first person to win 3 points, wins the game!

#### Customization
You can customize the game: 
- modify the timer setting in the get_prediction function.
- Alter the final score needed to win the game
- Visit this link and train a new image model if necessary: https://teachablemachine.withgoogle.com/

