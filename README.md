# Cricket Simulation

The methodology used in the provided code is to create classes to represent different entities in a cricket match, such as players, teams, field, umpire, commentator, and the match itself. Each class has its own set of properties and methods to simulate the behavior and interactions between these entities.Here's a more detailed explanation of the methodology used in the code:

<h4>Player Class:</h4>The Player class represents a cricket player and contains attributes such as name, bowling ability, batting ability, fielding ability, running ability, and experience. These attributes are used to determine the probabilities of different events occurring during the match.

<h4>Team Class:</h4>The Team class represents a cricket team and contains a list of players. It also has methods to select a captain, choose the next player to bat, and select a bowler. The batting_order list is used to keep track of the batting order of the players.

<h4>Field Class:</h4>The Field class represents the cricket field and contains attributes such as size, fan ratio, pitch conditions, and home advantage. These attributes can affect the probabilities of different events during the match.

<h4>Umpire Class:</h4>The Umpire class represents the umpire and keeps track of the score, wickets, and overs. It has a predict_outcome() method that uses the player's abilities to predict the outcome of a ball, such as a boundary, getting out, or scoring runs.

<h4>Commentator Class:</h4>The Commentator class provides commentary for each ball and over. It uses the match statistics to give a description of the ongoing game events.

<h4>Match Class:</h4>The Match class represents an individual cricket match. It takes objects of the Team, Field, Umpire, and Commentator classes as parameters. It has methods to start the match, change innings, simulate a ball, and end the match. The simulate_ball() method selects a batsman and a bowler, predicts the outcome using the umpire's predict_outcome() method, updates the score and wickets, and provides commentary.
<br>
<br>

<h3>To run the code:</h3>
1) Set up a Python environment: Install Python on your system if you haven't already.<br>
2) Create a new Python file: Open a text editor or an IDE and create a new Python file, for example, cricket.py.<br>
3) Write the complete code into the cricket.py file.<br>
4) Save the file: Save the cricket.py file.<br>
5) Run the code: Open a terminal or command prompt, navigate to the directory where the cricket.py file is saved and run the python python.py command<br>
6) Observe the output: The code will simulate a cricket match and display the commentary and match statistics in the terminal or command prompt.<br>
