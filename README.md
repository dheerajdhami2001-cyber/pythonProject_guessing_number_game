Higher or Lower: Flask Web Game
A fun, interactive number-guessing game built using the Flask web framework. The game generates a random number, and the player must guess it by navigating to different URLs. Each guess provides visual feedback through dynamic text colors and animated GIFs to tell the player if they are too high, too low, or correct!

demo.mp4


Key Features
Dynamic Routing: Uses Flask's <int:number> route converter to capture player guesses directly from the URL.

Visual Feedback: Features custom HTML styling with different colors (Red for too low, Blue for too high, Green for winning).

Giphy Integration: Displays fun, context-aware GIFs for every state of the game to improve user experience.

Randomized Logic: Every time the server restarts, a new secret number between 1 and 9 is generated.

Technologies Used
Python 3.x

Flask: A micro web framework for Python used to handle routing and server-side logic.

HTML/Inline CSS: Used for styling the game interface within the Python script.

Project Setup
1. Prerequisites
Python 3.x installed.

pip (Python package installer).

2. Installation
Clone the repository:

Bash

git clone https://github.com/dheerajdhami2001-cyber/higher-lower-flask.git
Navigate into the project directory:

Bash

cd higher-lower-flask
Install Flask:

Bash

pip install flask
How to Play
Run the script:

Bash

python main.py
Open your browser: Go to http://127.0.0.1:5000/. You will see the "Guess a number between 1 to 9" home screen.

Make a guess: To guess a number, add the number to the end of the URL in your browser's address bar.

Example: To guess the number 5, change the URL to http://127.0.0.1:5000/5 and hit Enter.

Follow the hints: The page will update to tell you if you need to go higher or lower. Keep changing the number in the URL until you find the winning number!

Optimization & Potential Improvements
HTML Templates: Currently, the HTML is written as strings inside the Python file. This could be moved to a templates/ folder using Flask's render_template for better code organization.

Reset Button: Adding a button on the "Win" screen that redirects back to the home page to start a new game.

Input Field: Instead of typing numbers into the URL bar, an HTML <form> could be added to the home page so users can type their guess into a box.

Acknowledgments
This project was inspired by and completed with the guidance of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.
