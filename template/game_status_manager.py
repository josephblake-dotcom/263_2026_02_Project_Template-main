# author: Joseph Blake
# date: 4/29/2026
# purpose: menu to view and manage game status reports

def game_status_menu(conn):
    print("\n--- Game Status Menu ---")
    print("1. View Game Status")
    print("2. View Current Winner")
    print("3. View Active Players")
    print("4. View Game Progress Summary")
    print("5. Update Player Score")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        view_game_status(conn)
    elif choice == "2":
        view_current_winner(conn)
    elif choice == "3":
        view_active_players(conn)
    elif choice == "4":
        view_game_progress(conn)
    elif choice == "5":
        update_player_score_sp(conn)
    elif choice == "6":
        print("Returning to main menu.")
    else:
        print("Invalid choice. Please try again.")


def view_game_status(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT Player_No, Player_Name, Current_Score, Turns_Left,
        CASE
            WHEN Current_Score >= 100 THEN 'Winner'
            WHEN Turns_Left <= 0 THEN 'Lost'
            ELSE 'In Progress'
        END AS Game_Status
        FROM players;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Current Game Status ---")
    for row in rows:
        print(row)

    cur.close()


def view_current_winner(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT Player_No, Player_Name, Current_Score
        FROM players
        WHERE Current_Score = (
            SELECT MAX(Current_Score)
            FROM players
        );
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Current Winner / Highest Score ---")
    for row in rows:
        print(row)

    cur.close()


def view_active_players(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT Player_No, Player_Name, Current_Score, Turns_Left
        FROM players
        WHERE Current_Score < 100
        AND Turns_Left > 0;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Active Players ---")
    for row in rows:
        print(row)

    cur.close()


def view_game_progress(conn):
    cur = conn.cursor(dictionary=True)

    query = """
        SELECT Game_No,
               COUNT(*) AS Total_Players,
               AVG(Current_Score) AS Average_Score,
               AVG(Turns_Left) AS Average_Turns_Left
        FROM players
        GROUP BY Game_No
        HAVING AVG(Current_Score) >= 0;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- Game Progress Summary ---")
    for row in rows:
        print(row)

    cur.close()

def update_player_score_sp(conn):
    cur = conn.cursor(dictionary=True)

    player_id = input("Enter Player No: ")
    new_score = input("Enter new score: ")
    output = 0

    cur.callproc("updateSPplayers", (player_id, new_score, output))

    conn.commit()

    print("Score updated using stored procedure.")

    cur.close()