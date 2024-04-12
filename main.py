from player_manager import PlayerManager
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    pm = PlayerManager()
    print("Player Manager")
    print()
    print("Command Menu\nview - View players\nadd  - Add a player\ndel  - Delete a player\nexit - Exit program")
    while True:
        print()
        user_input = str(input("Command: "))
        if user_input == "view":
            players = pm.get_players()
            print("Name            Wins    Losses      Ties     Games")
            print('-' * 50)
            for player in players:
                print(f"{player[1]:15} {player[2]:4} {player[3]:9} {player[4]:9} {player[5]:9}")
        elif user_input == 'add':
            while True:
                name = input('Name: ')
                if pm.player_exists(name):
                    print(f"A player with the name {name} already exists. Please enter a different name.")
                else:
                    break
            wins = get_positive_integer('Wins: ')
            losses = get_positive_integer('Losses: ')
            ties = get_positive_integer('Ties: ')
            pm.add_player(name, wins, losses, ties)
            print(f'{name} was added to database.')
        elif user_input == 'del':
            name = input('Name: ')
            if pm.player_exists(name):
                pm.delete_player(name)
                print(f'{name} was deleted from database.')
            else:
                print(f'No player found with the name {name}.')
        elif user_input == 'update':
            name = input('Name: ')
            if pm.player_exists(name):
                wins = get_positive_integer('New Wins: ')
                losses = get_positive_integer('New Losses: ')
                ties = get_positive_integer('New Ties: ')
                pm.update_player(name, wins, losses, ties)
                print(f'{name} was updated.')
            else:
                print(f'No player found with the name {name}.')

        elif user_input == "exit":
            break
        else:
            print("Please enter a valid command: They are case sensitive.")

    print("Bye!")
main()