from players import play_game as players_play_game, BluePlayer, RedPlayer

def play_game():
    """
    Simulate a marathon where Blue and Red players move randomly until one reaches a position over 1000.
    
    :return: Tuple containing the name of the winning player and the number of turns taken.
    """
    players = [BluePlayer(f"BluePlayer{i}") for i in range(1, 4)] + [RedPlayer(f"RedPlayer{i}") for i in range(1, 4)]
    
    turns = 0
    while True:
        for player in players:
            player.walk()
        turns += 1
        
        for player in players:
            if player.position > 1000:
                return (player.name, turns)

if __name__ == "__main__":
    winner, turns = play_game()
    print(f"{winner} won the marathon in {turns} turns!")
    
    imported_winner, imported_turns = players_play_game()
    print(f"{imported_winner} won the game in {imported_turns} turns!")
