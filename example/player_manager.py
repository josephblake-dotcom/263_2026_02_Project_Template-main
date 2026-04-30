# author: Nikolaos Komninos 
# date: 4/19/2026
# Purpose: present a menu to manage a table 
#     add/update/delete/list the table
# Changes by Kris Pepper

def player_manager_menu(conn):
    print("\n--- Maintain Player ---")
    print("1. Add Player")
    print("2. Change Player")
    print("3. Delete Player")
    print("4. List Players")
    print("5. Update Player Score (Stored Procedure)")  
    print("6. Change Player in a more complex and flexible way")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            add_player(conn)
        case "2":
            change_player(conn)
        case "3":
            delete_player(conn)
        case "4":
            list_players(conn)
        case "5":
            update_player_score(conn)
        case "6":
            change_player_complex(conn)
        case _:
            print("Invalid choice. Please try again.")

def add_player(conn):
    """Add a new player to the database.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Add Player ---")
    player_id = input("Enter Player ID: ")
    name = input("Enter Name: ")
    color = input("Enter Color: ")
    wins = input("Enter Wins: ")
    losses = input("Enter Losses: ")
    gold = input("Enter Gold: ")

    cur.execute(
        "INSERT INTO demo_players (ID, Name, Color, Wins, Losses, Gold) VALUES (%s, %s, %s, %s, %s, %s)",
        (player_id, name, color, wins, losses, gold),
    )
    conn.commit()
    print ('rows inserted: ', cur.rowcount)
    if cur.rowcount == 1:
        print(f"Player {name} added successfully!")
    else:
        print('An error occurred adding the player') 
    cur.close()


def change_player_complex(conn):
    """Update player information in the database.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Change Player ---")
    player_id = input("Enter Player ID to change: ")

    cur.execute("SELECT * FROM demo_players WHERE ID = %s", (player_id,))
    player = cur.fetchone()

    if not player:
        print("Player not found!")
        cur.close()
        return

    print(f"Current player data: {player}")
    print("\nWhich field would you like to change?")
    print("1. Name")
    print("2. Color")
    print("3. Wins")
    print("4. Losses")
    print("5. Gold")

    field_choice = input("Enter your choice (1-5): ")

    field_map = {
        "1": "Name",
        "2": "Color",
        "3": "Wins",
        "4": "Losses",
        "5": "Gold",
    }

    if field_choice not in field_map:
        print("Invalid choice!")
        cur.close()
        return

    field_name = field_map[field_choice]
    new_value = input(f"Enter new {field_name} (current: {player[field_name]}): ")

    cur.execute(
        f"UPDATE demo_players SET {field_name} = %s WHERE ID = %s",
        (new_value, player_id),
    )
    conn.commit()
    print ('rows updated: ', cur.rowcount)
    if cur.rowcount == 1:
        print(f"Player {field_name} updated successfully!")
    else:
        print('An error occurred updating the player') 
    cur.close()

def change_player(conn):
    """Update player information in the database as simply as possible.
       Args:
        conn: Active MySQL database connection
    """
    # Create a cursor 
    cur = conn.cursor(dictionary=True)
    #Prompt user for Player ID to change
    player_id = input("Enter Player ID to be changed: ")
    new_value = input("Enter color to change: ")
    # Execute an SQL UPDATE query to modify only that field
    cur.execute(
        f"UPDATE demo_players SET color = %s WHERE ID = %s",
        (new_value, player_id),
    )
    # Commit the transaction
    conn.commit()
    # Check for success and Print success message
    print ('rows updated: ', cur.rowcount)
    if cur.rowcount == 1:
        print(f"Player color updated successfully!")
    else:
        print('An error occurred updating the player') 
    # Close the transaction
    cur.close()

def delete_player(conn):
    """Delete a player from the database.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Delete Player ---")
    player_id = input("Enter Player ID to delete: ")

    cur.execute("DELETE FROM demo_players WHERE ID = %s", (player_id,))
    conn.commit()
    print ('rows updated: ', cur.rowcount)
    if cur.rowcount == 1:
        print(f"Player {player_id} deleted!")
    else:
        print('An error occurred updating the player') 
    cur.close()


def list_players(conn):
    """List all players in the database.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- List Players ---")
    cur.execute("SELECT * FROM demo_players")
    players = cur.fetchall()

    if not players:
        print("No players found.")
        cur.close()
        return

    print(
        f"\n{'ID':<15} {'Name':<20} {'Color':<15} {'Wins':<8} {'Losses':<8} {'Gold':<8}"
    )
    print("-" * 80)
    for player in players:
        print(
            f"{player['ID']:<15} {player['Name']:<20} {player['Color']:<15} {player['Wins']:<8} {player['Losses']:<8} {player['Gold']:<8}"
        )

    cur.close()


def update_player_score(conn):
    """Update a player's wins using the UpdatePlayerScore stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Update Player Score (Stored Procedure) ---")
    player_id = input("Enter Player ID: ")
    new_wins = input("Enter new number of wins: ")

    cur.callproc("UpdatePlayerScore", (player_id, new_wins))
    conn.commit()
    print(f"Player score updated to {new_wins} wins!")
    cur.close()
