import random

class Player:
    def __init__(self, name):
        """
        Initialize a new Player instance.
        
        :param name: String representing the player's name.
        """
        self.name = name
        self.position = 0

class RedPlayer(Player):
    def walk(self):
        """
        Simulate the RedPlayer walking by advancing their position by a random amount between 1 and 10.
        """
        self.position += random.randrange(1, 11)

class BluePlayer(Player):
    def walk(self):
        """
        Simulate the BluePlayer walking by advancing their position by a random amount between 4 and 8.
        """
        self.position += random.randrange(4, 9)

def play_game():
    """
    Simulate a game where Blue and Red players move randomly until one reaches a position over 100.
    
    :return: Tuple containing the name of the winning player and the number of turns taken.
    """
    players = [BluePlayer(f"BluePlayer{i}") for i in range(1, 4)] + [RedPlayer(f"RedPlayer{i}") for i in range(1, 4)]
    
    turns = 0
    while True:
        for player in players:
            player.walk()
        turns += 1
        
        for player in players:
            if player.position > 100:
                return (player.name, turns)

if __name__ == "__main__":
    winner, turns = play_game()
    print(f"{winner} won the game in {turns} turns!")
