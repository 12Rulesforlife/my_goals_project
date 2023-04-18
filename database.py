import sqlite3

DATABASE_NAME = "goals.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def close_db_connection(conn):
    conn.close()


def create_tables():
    conn = get_db_connection()
    conn.execute("""CREATE TABLE IF NOT EXISTS main_goals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    category TEXT,
                    deadline TEXT
                )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS subgoals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    main_goal_id INTEGER,
                    deadline TEXT,
                    FOREIGN KEY (main_goal_id) REFERENCES main_goals (id)
                )""")

    conn.execute("""CREATE TABLE IF NOT EXISTS achievements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT
                )""")

    conn.commit()
    close_db_connection(conn)

# Main goals-related functions

def get_goals():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM main_goals")
    goals = cursor.fetchall()
    close_db_connection(conn)
    return goals

def add_goal(title, description, category, deadline):
    conn = get_db_connection()
    conn.execute("INSERT INTO main_goals (title, description, category, deadline) VALUES (?, ?, ?, ?)",
                 (title, description, category, deadline))
    conn.commit()
    close_db_connection(conn)

def update_goal(goal_id, title, description, category, deadline):
    conn = get_db_connection()
    conn.execute("UPDATE main_goals SET title=?, description=?, category=?, deadline=? WHERE id=?",
                 (title, description, category, deadline, goal_id))
    conn.commit()
    close_db_connection(conn)

def delete_goal(goal_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM main_goals WHERE id=?", (goal_id,))
    conn.commit()
    close_db_connection(conn)

# Subgoals-related functions

def get_subgoals():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM subgoals")
    subgoals = cursor.fetchall()
    close_db_connection(conn)
    return subgoals

def add_subgoal(title, description, main_goal_id, deadline):
    conn = get_db_connection()
    conn.execute("INSERT INTO subgoals (title, description, main_goal_id, deadline) VALUES (?, ?, ?, ?)",
                 (title, description, main_goal_id, deadline))
    conn.commit()
    close_db_connection(conn)

def update_subgoal(subgoal_id, title, description, deadline):
    conn = get_db_connection()
    conn.execute("UPDATE subgoals SET title=?, description=?, deadline=? WHERE id=?",
                 (title, description, deadline, subgoal_id))
    conn.commit()
    close_db_connection(conn)

def delete_subgoal(subgoal_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM subgoals WHERE id=?", (subgoal_id,))
    conn.commit()
    close_db_connection(conn)

import sqlite3

DATABASE_NAME = "goals.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def close_db_connection(conn):
    conn.close()



def get_achievements():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM achievements")
    achievements = cursor.fetchall()
    close_db_connection(conn)
    return achievements

def add_achievement(title, description):
    conn = get_db_connection()
    conn.execute("INSERT INTO achievements (title, description) VALUES (?, ?)",
                 (title, description))
    conn.commit()
    close_db_connection(conn)

def update_achievement(achievement_id, title, description):
    conn = get_db_connection()
    conn.execute("UPDATE achievements SET title=?, description=? WHERE id=?",
                 (title, description, achievement_id))
    conn.commit()
    close_db_connection(conn)

def delete_achievement(achievement_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM achievements WHERE id=?", (achievement_id,))
    conn.commit()
    close_db_connection(conn)

create_tables()
