def save_game_txt(PlayerName, game_state, filename = "PlayersData.txt"):
    
    # 'a' to append data
    with open(filename, 'a') as file:  
        file.write(f"Player: {PlayerName}\n")
        for key, value in game_state.items():
            file.write(f"{key}: {value}\n")
        # Blank line to separate data
        file.write("\n")


def load_game_txt(PlayerName, password, filename = "PlayersData.txt"):
    game_state = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        player_found = False
        for line in lines:

            if line.startswith("Player:"):

                # (": ")[1] = player's name
                CurrentPlayer = line.split(": ")[1].strip()
                if CurrentPlayer == PlayerName:
                    # True = data found // False = ignore
                    player_found = True
                else:
                    player_found = False

            elif player_found:
                # Empty line to indicate the end of a player data
                if line.strip() == "":
                    break  
                key, value = line.strip().split(': ')
                game_state[key] = value

    if game_state.get('password') == password:
        return game_state
    else:
        print("Incorrect name or password.")
        return None


def start_game():
    while True:
        choice = input("Enter 'L' to load game, 'N' for new game, or 'X' to quit: ")
        
        if choice == 'X':
            print("Goodbye!")
            return

        if choice == 'L':
            # Limit to 5 attempts only
            attempts = 5
            while attempts > 0:

                PlayerName = input("Enter your name (or 'X' to quit): ")
                if PlayerName == 'X':
                    print("Goodbye!")
                    return
                
                password = input("Enter password (or 'X' to quit): ")
                if password == 'X':
                    print("Goodbye!")
                    return
                
                # Load game with correct name and password
                game_state = load_game_txt(PlayerName, password)
                if game_state:
                    print(f"Welcome back, {PlayerName}!")
                    return
                
                # Load game with incorrect name or password or both
                else:
                    attempts -= 1
                    print(f"You have {attempts} attempts left.")
                    if attempts == 0:
                        print("Maximum attempts reached.")
                        print("Goodbye!")
                        break
                    
        elif choice == 'N':
            PlayerName = input("Enter your name (or 'X' to quit): ")
            if PlayerName == 'X':
                print("Goodbye!")
                break
            
            password = input("Create a new password (or 'X' to quit): ")
            if password == 'X':
                print("Goodbye!")
                break

            # Starter pack
            game_state = {
                'password': password,
                'my pet': '0',
            }

            save_game_txt(PlayerName, game_state)
            print(f"Welcome, {PlayerName}!")
            break

        else:
            print("Invalid choice. Please enter 'L', 'N', or 'X'.")

start_game()
