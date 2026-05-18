import streamlit as st

def show_quizzes(user):
    """Display quizzes page"""
    st.markdown("""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>📝 Quizzes & Assessments</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Test your knowledge and track your progress</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # Sample quizzes
    quizzes = [
        {
            "title": "Python Fundamentals Quiz",
            "course": "Python Fundamentals",
            "questions": 10,
            "passing_score": 70,
            "completed": False,
            "difficulty": "Easy"
        },
        {
            "title": "ML Basics Assessment",
            "course": "ML Basics",
            "questions": 15,
            "passing_score": 75,
            "completed": False,
            "difficulty": "Medium"
        }
    ]
    
    for quiz in quizzes:
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            <div class='card' style='border-left: 4px solid #667eea;'>
                <h3 style='margin-top: 0;'>{quiz['title']}</h3>
                <p style='color: #757575; margin: 0.5rem 0;'><strong>Course:</strong> {quiz['course']}</p>
                <p style='color: #757575; margin: 0.5rem 0;'><strong>Questions:</strong> {quiz['questions']} | <strong>Pass Score:</strong> {quiz['passing_score']}%</p>
                <p style='color: #999; font-size: 0.85rem;'>Difficulty: {quiz['difficulty']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("📝 Start", key=f"quiz_{quiz['title']}", use_container_width=True):
                show_quiz_detail(quiz)
        
        st.markdown("")

def show_quiz_detail(quiz):
    """Show quiz questions and answers"""
    st.markdown(f"""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>{quiz['title']}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.info(f"📋 This quiz has {quiz['questions']} questions. You need {quiz['passing_score']}% to pass.")
    
    st.divider()
    
    # Sample questions
    questions = [
        {
            "question": "What is the output of print(2**3)?",
            "options": ["6", "8", "9", "5"],
            "correct": "8"
        },
        {
            "question": "Which data type is used for storing text?",
            "options": ["int", "str", "float", "bool"],
            "correct": "str"
        },
        {
            "question": "What is Machine Learning?",
            "options": [
                "A subset of AI where systems learn from data",
                "A programming language",
                "A type of neural network",
                "A database system"
            ],
            "correct": "A subset of AI where systems learn from data"
        }
    ]
    
    st.markdown("### Answer the following questions:")
    
    answers = []
    
    for idx, q in enumerate(questions[:3]):
        st.markdown(f"<h4>Question {idx + 1}: {q['question']}</h4>", unsafe_allow_html=True)
        
        answer = st.radio(
            "Select an answer:",
            q['options'],
            key=f"q_{idx}",
            label_visibility="collapsed"
        )
        answers.append(answer)
        st.markdown("")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⬅️ Previous", use_container_width=True):
            st.info("Would navigate to previous questions")
    
    with col2:
        if st.button("➡️ Next", use_container_width=True):
            st.info("Would navigate to next questions")
    
    with col3:
        if st.button("✅ Submit Quiz", use_container_width=True):
            st.success("🎉 Quiz submitted! You scored 80%")
            st.balloons()

