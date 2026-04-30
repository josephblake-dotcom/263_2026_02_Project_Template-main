# author: Nikolaos Komninos 
# date: 4/19/2026
# Purpose: present a menu to list queries 
# Changes by Kris Pepper

def player_stats_menu(conn):
    print("\n--- Player Reports ---")
    print("1. Player Statistics (Stored Procedure)")
    print("2. Players Grouped by Wins (GROUP BY)")
    print("3. Players with Gold Above Average (Sub-query)")
    print("4. High-Winning Players (HAVING)")
    print("5. All Players with Stats (LEFT OUTER JOIN)")

    subchoice = input("Enter your choice (1-5): ").strip()

    match subchoice:
        case "1":
            query_player_stats(conn)
        case "2":
            query_players_by_wins(conn)
        case "3":
            query_players_by_gold(conn)
        case "4":
            query_top_players(conn)
        case "5":
            query_all_players_with_stats(conn)
        case _:
            print("Invalid choice. Please try again.")
def query_player_stats(conn):
    """Query player statistics using GetPlayerStats stored procedure.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Player Statistics ---")

    cur.callproc("GetPlayerStats")
    
    for result in cur.stored_results():
        raw_stats = result.fetchone()
        # if the stats came through as a tuple instead of a dict, 
        #   turn them into a dict
        # Debug: Check if it's still a tuple 
        print(f"DEBUG: Type is {type(raw_stats)}, Value: {raw_stats}")

        if raw_stats:
            # If it's a tuple, map it to the column names manually
            if isinstance(raw_stats, tuple):
                column_names = [i[0] for i in result.description]
                stats = dict(zip(column_names, raw_stats))
            else:
                stats = raw_stats
        
        print(f"\nTotal Players: {stats['TotalPlayers']}")
        print(f"Total Wins: {stats['TotalWins']}")
        print(f"Total Losses: {stats['TotalLosses']}")
        print(f"Average Gold: {stats['AverageGold']:.2f}")
        print(f"Max Wins by a Player: {stats['MaxWins']}")

    cur.close()


def query_players_by_wins(conn):
    """Query players grouped by wins using GROUP BY.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Players Grouped by Wins ---")

    cur.execute("""
        SELECT ID, Name, Wins, Losses, (Wins + Losses) as TotalGames, Color
        FROM demo_players
        GROUP BY Wins, ID, Name
        ORDER BY Wins DESC
    """)

    print(
        f"{'ID':<15} {'Name':<20} {'Color':<15} {'Wins':<8} {'Losses':<8} {'Total Games':<12}"
    )
    print("-" * 95)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Color']:<15} {row['Wins']:<8} {row['Losses']:<8} {row['TotalGames']:<12}"
        )

    cur.close()


def query_players_by_gold(conn):
    """Query players with gold above average using a sub-query.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- Players with Gold Above Average ---")

    cur.execute("""
        SELECT ID, Name, Gold, (SELECT AVG(Gold) FROM demo_players) as AvgGold
        FROM demo_players
        WHERE Gold > (SELECT AVG(Gold) FROM demo_players)
        ORDER BY Gold DESC
    """)

    print(f"{'ID':<15} {'Name':<20} {'Gold':<8} {'Avg Gold':<10}")
    print("-" * 60)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Gold']:<8} {row['AvgGold']:<10.2f}"
        )

    cur.close()


def query_top_players(conn):
    """Query players using HAVING clause.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- High-Winning Players (HAVING) ---")

    cur.execute("""
        SELECT ID, Name, Wins, Losses, Gold, (Wins + Losses) as TotalGames
        FROM demo_players
        GROUP BY ID, Name, Wins, Losses, Gold
        HAVING Wins > 20
        ORDER BY Wins DESC
    """)

    print(
        f"{'ID':<15} {'Name':<20} {'Wins':<8} {'Losses':<8} {'Gold':<8} {'Total Games':<12}"
    )
    print("-" * 95)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Wins']:<8} {row['Losses']:<8} {row['Gold']:<8} {row['TotalGames']:<12}"
        )

    cur.close()


def query_all_players_with_stats(conn):
    """Query all players with statistics using LEFT OUTER JOIN.

    Args:
        conn: Active MySQL database connection
    """
    cur = conn.cursor(dictionary=True)
    print("\n--- All Players with Stats (LEFT OUTER JOIN) ---")

    cur.execute("""
        SELECT p.ID, p.Name, p.Color, p.Wins, p.Losses, p.Gold,
               s.AvgWins as OverallAvgWins
        FROM demo_players p
        LEFT OUTER JOIN (
            SELECT AVG(Wins) as AvgWins
            FROM demo_players
        ) s ON 1=1
        ORDER BY p.Name
    """)

    print(
        f"{'ID':<15} {'Name':<20} {'Color':<15} {'Wins':<8} {'Losses':<8} {'Gold':<8} {'Avg Wins':<10}"
    )
    print("-" * 95)
    for row in cur.fetchall():
        print(
            f"{row['ID']:<15} {row['Name']:<20} {row['Color']:<15} {row['Wins']:<8} {row['Losses']:<8} {row['Gold']:<8} {row['OverallAvgWins']:<10.2f}"
        )

    cur.close()
