# 263_2026_02_Project_Template

This repo contains a template for the CSC 263 Final Project that you may use to
get started.

In order to do the example exercise outlined by the comments in the template,
read the following section.

## Doing the Template Exercise

The repository is split into two different directories:

- `template/` contains the template to be used by the exercise
- `example/` contains the answers to the exercise

The queries to be completed for the exercise live in `example/queries.sql`

To get started, clone this repo to the compsci server.
If you are using VS code, open the 263_2026_02_Project_Template folder.
Finally, create a virtual environment, activate it, and install the
required libraries:

```bash
# Windows
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After setting up the environment, edit the database connection credentials in 
`template/app.py` to reflect your own (lines 18-24). You will only need to change
your username (match your compsci server username), and your database (match your
database name). Password will still be left blank.

Test your database connection by running `template/app.py`. If the connection does
not work, an error will be thrown. Otherwise, the connection was established and closed.

Once done, create the demo_players table in your database by running the example/queries.sql in your own database. 
Remember to first run :
   use yourdatabasename; # replace yourdatabasename with your own database, not your project's
Then run example/queries
 
It will create tables and stored procedures and insert this data:

INSERT INTO demo_players (ID, Name, Color, Wins, Losses, Gold) VALUES
('P001', 'James Anderson', 'Red', 15, 8, 450),
('P002', 'Emily Roberts', 'Blue', 12, 10, 380),
('P003', 'Michael Thompson', 'Green', 20, 5, 600),
('P004', 'Sarah Wilson', 'Yellow', 8, 15, 250),
('P005', 'David Martinez', 'Purple', 25, 3, 750),
('P006', 'Jessica Taylor', 'Orange', 18, 7, 520),
('P007', 'Christopher Davis', 'Black', 10, 12, 310),
('P008', 'Amanda White', 'Pink', 22, 4, 680),
('P009', 'Daniel Harris', 'Red', 14, 9, 420),
('P010', 'Jennifer Clark', 'Blue', 16, 6, 490),
('P011', 'Matthew Lewis', 'Green', 9, 14, 280),
('P012', 'Ashley Walker', 'Yellow', 28, 2, 850),
('P013', 'Andrew Hall', 'Purple', 11, 11, 340),
('P014', 'Stephanie Young', 'Orange', 19, 8, 560),
('P015', 'Joshua King', 'Black', 23, 5, 710),
('P016', 'Michelle Wright', 'Pink', 7, 16, 220),
('P017', 'Ryan Scott', 'Red', 17, 7, 500),
('P018', 'Kimberly Torres', 'Blue', 13, 10, 390),
('P019', 'Brandon Nguyen', 'Green', 21, 4, 640),
('P020', 'Laura Hill', 'Yellow', 6, 17, 190),
('P021', 'Justin Flores', 'Purple', 24, 6, 730),
('P022', 'Samantha Green', 'Orange', 5, 18, 160),
('P023', 'Kevin Adams', 'Black', 26, 3, 800),
('P024', 'Rachel Nelson', 'Pink', 12, 9, 370),
('P025', 'Brian Carter', 'Green', 30, 1, 900);


With the tables in place, you can now test the example. 
First change the database to your database in `example/app.py`, just as you did to `template/app.py`. 
Then run `example/app.py` to see how it works with the sample data. 

Now you are ready to use the template. 
One group member will copy the 5 files inside template into your own project folder, which you made by cloning your project repository. 
That group member will change app.py to use the project database and their own username, and then commit and push.
Then every other group member will pull down the updated repository and change the app.py to their own username.

Now each group member will start coding their own queries. 
Each group member will make a file similar to player_manager to manage their own table, and update app.py to import and use their new file.  
If you get stuck on a query, you may refer to the example query in `example/`.
