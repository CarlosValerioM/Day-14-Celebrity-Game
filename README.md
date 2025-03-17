# Day-14-Celebrity-Game  
A game to guess which celebrity has more Instagram followers. Difficulty: Easy  

## Author:  
Carlos Valerio (CarlosValerioM)  

## Date:  
2025/03/17

## License:  
MIT License  

## Dependencies:  
Requires `data.py` (contains the list of celebrities).  

## Description:  
`celebrityGame.py` is a Python game where the player must guess which of two randomly selected celebrities has more Instagram followers. The game continues until the player makes an incorrect guess.  

### Game Flow:  
1. The script selects two random celebrities from `data.py`.  
2. It displays their name, profession, and country.  
3. The player guesses which celebrity has more followers.  
4. If correct, the score increases and a new round begins.  
5. If incorrect, the game ends, and the final score is displayed.  

## Usage:  

1. Clone this repository:  
```bash
git clone https://github.com/CarlosValerioM/Day-14-Celebrity-Game.git
```
Navigate to the project directory:
```bash
cd Day-14-Celebrity-Game
```
Run the script:
```bash
python celebrityGame.py
```
Follow the on-screen instructions to play.
Example Output:
```bash
Cristiano Ronaldo is a Footballer from Portugal.  
Taylor Swift is a Singer from the USA.  
Who has more followers? Type A or B: a  
Correct! Your score is 1.  

Kylie Jenner is a Model from the USA.  
Lionel Messi is a Footballer from Argentina.  
Who has more followers? Type A or B: b  
Sorry! You lose! Your score is 1.
```
## How it works:
The script retrieves celebrity data from data.py.

It compares their follower counts to determine the correct answer.

The player keeps guessing until they make a mistake.

## License:
This project is licensed under the MIT License.
