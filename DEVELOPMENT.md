# 🔧 Development Guide for AI Learn

## Architecture Overview

### Frontend Architecture
- **Framework**: Streamlit
- **Approach**: Page-based navigation using radio buttons in sidebar
- **Styling**: Custom CSS with gradient effects and cards

### Backend Architecture
- **Database**: SQLite3 with 11 interconnected tables
- **Authentication**: bcrypt for password hashing
- **Session Management**: Streamlit session state

### Data Flow
```
User Input → Streamlit App → Database Layer → Data Processing → Display
```

---

## File Organization

### Core Application Files
- `app.py`: Main entry point and navigation
- `requirements.txt`: Python dependencies
- `.streamlit/config.toml`: Streamlit configuration

### Source Modules (`src/`)
- `db.py`: Database initialization, queries, and CRUD operations
- `auth.py`: Authentication, registration, and password management
- `courses.py`: Course content and curriculum data

### Page Modules (`pages/`)
- `home.py`: Landing page, login, and registration
- `courses.py`: Course listing and lesson content
- `exercises.py`: Interactive coding exercises
- `quiz.py`: Quizzes and assessments
- `forum.py`: Community discussions
- `profile.py`: User profile and settings
- `certifications.py`: Certificate management

---

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP,
    last_login TIMESTAMP
)
```

### Courses & Learning Tables
```sql
CREATE TABLE courses (id, title, description, level, duration_hours, created_at)
CREATE TABLE lessons (id, course_id, title, content, order_num, created_at)
CREATE TABLE exercises (id, lesson_id, title, description, starter_code, solution_code, difficulty, created_at)
CREATE TABLE user_progress (id, user_id, course_id, lesson_id, exercise_id, completed, completed_at, score)
CREATE TABLE quizzes (id, course_id, title, description, passing_score, created_at)
CREATE TABLE quiz_questions (id, quiz_id, question_text, question_type, options, correct_answer, explanation, order_num)
CREATE TABLE quiz_attempts (id, user_id, quiz_id, score, passed, attempted_at, answers)
```

### Community & Achievements
```sql
CREATE TABLE forum_posts (id, user_id, course_id, title, content, created_at, updated_at, views)
CREATE TABLE forum_replies (id, post_id, user_id, content, created_at, updated_at, helpful_count)
CREATE TABLE certifications (id, user_id, course_id, issued_at, certificate_code)
```

---

## Adding New Features

### 1. Add a New Course

**File**: `src/courses.py`

```python
"new_course_key": {
    "title": "Course Title",
    "description": "Course description",
    "level": "Beginner",  # or Intermediate/Advanced
    "duration_hours": 20,
    "lessons": [
        {
            "title": "Lesson Title",
            "content": "Markdown content here",
            "exercises": [
                {
                    "title": "Exercise Title",
                    "description": "What to do",
                    "starter_code": "# Your code here",
                    "solution_code": "# Solution",
                    "difficulty": "Easy"  # or Medium/Hard
                }
            ]
        }
    ]
}
```

### 2. Add a New Page

**File**: `pages/newpage.py`

```python
import streamlit as st

def show_newpage(user):
    """Display new page content"""
    st.title("📌 New Page Title")
    
    # Your content here
    st.markdown("### Hello World")
    st.write("Your content goes here")
```

**Update**: `app.py` - Add to navigation radio button and import

```python
from pages import newpage

# In the navigation section:
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📚 Courses", "📌 New Page"],  # Add this
    label_visibility="collapsed"
)

# In the routing section:
elif page == "📌 New Page":
    newpage.show_newpage(user)
```

### 3. Add a New Database Table

**File**: `src/db.py`

```python
def init_db():
    # ... existing code ...
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS new_table (
        id INTEGER PRIMARY KEY,
        column1 TEXT NOT NULL,
        column2 INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()

# Add helper functions:
def add_to_new_table(column1, column2):
    """Add record to new_table"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO new_table (column1, column2) VALUES (?, ?)",
        (column1, column2)
    )
    conn.commit()
    conn.close()
```

---

## Session State Management

### Current User Session
```python
# Set user in session after login
st.session_state.user = user_object  # Contains: id, username, email

# Check if user is logged in
if is_logged_in():
    user = st.session_state.user
    # Use user data

# Logout
logout_user()  # Clears st.session_state.user
```

### Storing Course State
```python
# Selected course
st.session_state.selected_course = course_key
st.session_state.selected_lesson = lesson_index
```

---

## Authentication Flow

```
User Registration
    ↓
Hash Password (bcrypt)
    ↓
Store in Database
    ↓
User Login
    ↓
Verify Password
    ↓
Update Last Login
    ↓
Store in Session State
    ↓
Redirect to Dashboard
```

---

## Styling and Customization

### Color Scheme (in `.streamlit/config.toml`)
```
Primary Color: #667eea (Purple)
Secondary Color: #764ba2 (Dark Purple)
Background: #ffffff (White)
Secondary Background: #f0f2f6 (Light Gray)
Text: #262730 (Dark Gray)
```

### Custom CSS (in `app.py`)
```python
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)
```

---

## Common Development Tasks

### Testing
```bash
# Run the app
streamlit run app.py

# Test specific page
# Navigate in sidebar to test each feature
```

### Database Debugging
```python
# Check database contents
from src.db import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
```

### Adding Sample Data
```python
from src.db import get_connection

def add_sample_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Add courses
    cursor.execute(
        "INSERT INTO courses (title, level) VALUES (?, ?)",
        ("Python Basics", "Beginner")
    )
    conn.commit()
    conn.close()
```

---

## Performance Optimization Tips

1. **Cache Database Queries**
```python
@st.cache_data
def get_courses():
    return get_all_courses()
```

2. **Lazy Load Content**
```python
# Only load lesson content when requested
lesson = get_lesson(course_key, lesson_idx)
if lesson:
    st.markdown(lesson['content'])
```

3. **Optimize Images**
- Use webp format when possible
- Compress images to under 100KB

---

## Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Deploy to Streamlit Cloud
1. Push to GitHub
2. Go to share.streamlit.io
3. Connect GitHub repository
4. Deploy with one click

### Self-Hosted Options
- Docker container
- AWS EC2
- Heroku
- DigitalOcean App Platform

---

## Troubleshooting

### Issue: Database locked
**Solution**: Close all connections and restart app

### Issue: Session state not persisting
**Solution**: Use `st.session_state` correctly, avoid direct variables

### Issue: Slow page load
**Solution**: Use `@st.cache_data` for expensive operations

### Issue: CSS not applying
**Solution**: Use `unsafe_allow_html=True` in st.markdown()

---

## Contributing Guidelines

1. **Code Style**: Follow PEP 8
2. **Comments**: Add docstrings to all functions
3. **Testing**: Test new features locally first
4. **Commits**: Use clear, descriptive commit messages
5. **Documentation**: Update README and DEVELOPMENT.md

---

## Future Enhancement Ideas

- [ ] Real code execution sandbox (Replit API)
- [ ] Video lesson integration (YouTube API)
- [ ] AI-powered learning recommendations
- [ ] Peer code review system
- [ ] Livestream tutoring sessions
- [ ] Certificate verification API
- [ ] Mobile responsive design
- [ ] Dark mode theme
- [ ] Multi-language support
- [ ] Gamification (badges, leaderboards)

---

## Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Python SQLite3](https://docs.python.org/3/library/sqlite3.html)
- [bcrypt Documentation](https://github.com/pyca/bcrypt)
- [Markdown Guide](https://www.markdownguide.org)

---

Happy coding! 🚀
