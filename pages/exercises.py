import streamlit as st

def show_exercises(user):
    """Display exercises page"""
    st.markdown("""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>💪 Practice Exercises</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Strengthen your skills with hands-on coding challenges</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        course_filter = st.selectbox("Filter by course", ["All", "Python Fundamentals", "ML Basics", "Deep Learning"])
    with col2:
        difficulty_filter = st.selectbox("Filter by difficulty", ["All", "Easy", "Medium", "Hard"])
    
    st.divider()
    
    # Sample exercises
    exercises = [
        {
            "title": "Print Your Name",
            "course": "Python Fundamentals",
            "difficulty": "Easy",
            "description": "Write a program that prints your name",
            "completed": True
        },
        {
            "title": "Grade Calculator",
            "course": "Python Fundamentals",
            "difficulty": "Easy",
            "description": "Create an if/else statement that assigns grades based on scores",
            "completed": False
        },
        {
            "title": "Fibonacci Generator",
            "course": "Python Fundamentals",
            "difficulty": "Medium",
            "description": "Generate Fibonacci sequence up to n numbers",
            "completed": False
        },
        {
            "title": "Linear Regression from Scratch",
            "course": "ML Basics",
            "difficulty": "Hard",
            "description": "Implement linear regression without using sklearn",
            "completed": False
        }
    ]
    
    for exercise in exercises:
        if course_filter != "All" and exercise["course"] != course_filter:
            continue
        if difficulty_filter != "All" and exercise["difficulty"] != difficulty_filter:
            continue
        
        difficulty_color = {
            "Easy": "🟢",
            "Medium": "🟡",
            "Hard": "🔴"
        }
        
        difficulty_badge_class = {
            "Easy": "badge-success",
            "Medium": "badge-warning",
            "Hard": "badge-danger"
        }
        
        status_icon = "✅" if exercise.get("completed") else "⭕"
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            <div class='card' style='border-left: 4px solid #667eea;'>
                <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;'>
                    <h3 style='margin: 0;'>{status_icon} {exercise['title']}</h3>
                    <span class='badge badge-primary'>{difficulty_color[exercise['difficulty']]}</span>
                </div>
                <p style='color: #757575; margin: 0.5rem 0;'>{exercise['description']}</p>
                <p style='color: #999; font-size: 0.85rem;'>📚 {exercise['course']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("Solve", key=f"solve_{exercise['title']}", use_container_width=True):
                show_exercise_detail(exercise)
        
        st.markdown("")

def show_exercise_detail(exercise):
    """Show exercise detail and code editor"""
    st.markdown(f"""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>{exercise['title']}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"**Course:** {exercise['course']}")
    with col2:
        difficulty_color = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
        st.markdown(f"**Difficulty:** {difficulty_color[exercise['difficulty']]}")
    with col3:
        st.markdown("")
    
    st.divider()
    
    st.markdown("### 📝 Problem Description")
    st.markdown(f"**{exercise['description']}**")
    
    st.markdown("### 💻 Your Code")
    code = st.text_area(
        "Write your solution here",
        height=300,
        key="exercise_code"
    )
    
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("▶️ Run Code", use_container_width=True):
            st.success("✅ Code executed successfully!")
            st.markdown("**Output:**")
            st.code("Hello World", language="plaintext")
    
    with col2:
        if st.button("💡 Show Hint", use_container_width=True):
            st.info("💡 **Hint:** Use a loop to solve this problem")
    
    with col3:
        if st.button("👀 Show Solution", use_container_width=True):
            st.success("**Solution:**")
            st.code("# Solution code\nprint('Hello, World!')", language="python")

