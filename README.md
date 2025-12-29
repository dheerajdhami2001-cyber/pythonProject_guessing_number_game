# Higher-Lower Web Game

A web-based "Guess the Number" game built with Python and the Flask framework. This application generates a random number between 1 and 9 and challenges the user to guess it by modifying the URL. It provides immediate visual feedback with fun GIFs and colored text to indicate if the guess is too high, too low, or correct.

## Demo

![Higher Lower Game Demo](demo.gif)

## Key Features

-   **Random Number Generation:** A new target number (1-9) is generated every time the server starts.
-   **Dynamic Routing:** Uses Flask's variable rules (`<int:number>`) to capture the user's guess directly from the URL bar.
-   **Visual Feedback:** Displays different GIFs and styled HTML messages based on the game logic (Too High, Too Low, or Correct).
-   **Debug Mode:** Runs with debug mode enabled for easier development and testing.

## Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/higher-lower-flask.git
    ```
    *(Note: Please replace `higher-lower-flask` with your actual repository name if it is different.)*

2.  **Navigate into the project directory:**
    ```bash
    cd higher-lower-flask
    ```

3.  **Install Flask:**
    You need to install the Flask framework to run the web server.
    ```bash
    pip install flask
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## How to Play

1.  Once the script is running, you will see a message in your terminal like `Running on http://127.0.0.1:5000`.
2.  Open your web browser and go to `http://127.0.0.1:5000/`. You will see the prompt to guess a number.
3.  **To make a guess, add a forward slash and a number to the end of the URL.**
    *   *Example:* To guess the number **5**, type: `http://127.0.0.1:5000/5`
4.  The page will reload and tell you if your guess was too high, too low, or correct!

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)** by Dr. Angela Yu.
