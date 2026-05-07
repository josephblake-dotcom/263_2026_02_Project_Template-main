# author: Nikolaos Komninos 
# date: 4/19/2026
# Purpose: 263 application to work with game DB
#          connect to SQL 
#          manage main menu
# Changes by Kris Pepper

import mysql.connector
import game_status_manager

# everyone in the project shares app.py, 
#  but everyone should have their own 2 files: 
#    module to manage their table
#    module to run their queries

# module to manage a table
from player_manager import (
    player_manager_menu 
)

#module to run queries
from player_stats import (
    player_stats_menu
)

# Establish connection to database (edit accordingly)
conn = mysql.connector.connect(
    host="compsci.adelphi.edu",
    port=3306,
    user="josephblake",
    password="M6cP31N8",
    database="josephblake",
)

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Maintain Player")
        print("2. Player Reports")
        print("3. Game Status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        match choice:
            case "1":
                player_manager_menu(conn)
            case "2":
                player_stats_menu(conn)
            case "3":
                game_status_manager.game_status_menu(conn)
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
