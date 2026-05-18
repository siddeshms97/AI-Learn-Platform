import sqlite3
import os
from datetime import datetime
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "data" / "ailearn.db"

def get_connection():
    """Get database connection"""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with all required tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    )
    """)
    
    # Courses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        level TEXT,
        duration_hours INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Lessons table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY,
        course_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT,
        order_num INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    
    # Exercises table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        lesson_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        starter_code TEXT,
        solution_code TEXT,
        difficulty TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (lesson_id) REFERENCES lessons(id)
    )
    """)
    
    # User Progress table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        lesson_id INTEGER,
        exercise_id INTEGER,
        completed BOOLEAN DEFAULT 0,
        completed_at TIMESTAMP,
        score REAL,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id),
        FOREIGN KEY (lesson_id) REFERENCES lessons(id),
        FOREIGN KEY (exercise_id) REFERENCES exercises(id)
    )
    """)
    
    # Quizzes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY,
        course_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        passing_score REAL DEFAULT 70,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    
    # Quiz Questions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_questions (
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER NOT NULL,
        question_text TEXT NOT NULL,
        question_type TEXT,
        options TEXT,
        correct_answer TEXT,
        explanation TEXT,
        order_num INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
    )
    """)
    
    # Quiz Attempts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_attempts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        quiz_id INTEGER NOT NULL,
        score REAL,
        passed BOOLEAN,
        attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        answers TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
    )
    """)
    
    # Forum Posts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS forum_posts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        course_id INTEGER,
        title TEXT NOT NULL,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP,
        views INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    
    # Forum Replies table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS forum_replies (
        id INTEGER PRIMARY KEY,
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP,
        helpful_count INTEGER DEFAULT 0,
        FOREIGN KEY (post_id) REFERENCES forum_posts(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)
    
    # Certifications table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS certifications (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        certificate_code TEXT UNIQUE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    
    conn.commit()
    conn.close()

def add_user(username, email, password_hash):
    """Add a new user"""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user(username):
    """Get user by username"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_login(user_id):
    """Update last login timestamp"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?",
        (user_id,)
    )
    conn.commit()
    conn.close()

def get_user_progress(user_id, course_id):
    """Get user progress for a course"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT * FROM user_progress 
           WHERE user_id = ? AND course_id = ?""",
        (user_id, course_id)
    )
    progress = cursor.fetchall()
    conn.close()
    return progress
