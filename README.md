# AiCore_Projects
This repo contains several different projects.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Hangman">Hangman</a>
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
