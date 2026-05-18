import streamlit as st

def show_certifications(user):
    """Show certifications page"""
    st.markdown("""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>🏆 Your Certifications</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Track and share your achievements</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    st.markdown("""
    Earn certificates by completing courses and passing final assessments.
    These certifications can be shared on your resume and LinkedIn profile.
    """)
    
    st.divider()
    
    # Available certifications
    st.markdown("<h2>🎯 Available Certifications</h2>", unsafe_allow_html=True)
    
    certifications = [
        {
            "name": "Python Fundamentals Certification",
            "course": "Python Fundamentals",
            "requirements": "Complete all lessons and score 80% on final quiz",
            "progress": 45,
            "status": "In Progress"
        },
        {
            "name": "ML Basics Certification",
            "course": "ML Basics",
            "requirements": "Complete all lessons and score 75% on final quiz",
            "progress": 20,
            "status": "In Progress"
        },
        {
            "name": "Deep Learning Specialist",
            "course": "Deep Learning",
            "requirements": "Complete all lessons and final project",
            "progress": 0,
            "status": "Not Started"
        }
    ]
    
    for cert in certifications:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            status_color = {
                "Completed": "🟢",
                "In Progress": "🟡",
                "Not Started": "⚪"
            }
            
            st.markdown(f"""
            <div class='card' style='border-left: 4px solid #667eea;'>
                <h3 style='margin-top: 0;'>{cert['name']}</h3>
                <p style='color: #757575; margin: 0.5rem 0;'><strong>Course:</strong> {cert['course']}</p>
                <p style='color: #757575; margin: 0.5rem 0;'><strong>Requirements:</strong> {cert['requirements']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.progress(cert['progress'] / 100, text=f"{cert['progress']}%")
        
        with col2:
            st.markdown(f"""
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2rem;'>{status_color[cert['status']]}</div>
                <p style='margin: 0.5rem 0; color: #757575; font-weight: 600;'>{cert['status']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("")
    
    st.divider()
    
    # Earned certificates
    st.markdown("<h2>✅ Your Certificates</h2>", unsafe_allow_html=True)
    
    st.info("📭 You haven't earned any certificates yet. Complete courses to earn them!")
    
    st.divider()
    
    st.markdown("<h2>ℹ️ How It Works</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    1. **Enroll** in a course
    2. **Complete** all lessons and exercises
    3. **Pass** the final quiz with the required score
    4. **Earn** your certificate
    5. **Share** on LinkedIn, GitHub, or resume
    
    Each certificate is digitally signed and verifiable on AI Learn's platform.
    """)

