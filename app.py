import streamlit as st
from src.db import init_db
from src.auth import is_logged_in, logout_user
from pages import home, courses, exercises, quiz, forum, profile, certifications

# Page configuration
st.set_page_config(
    page_title="AI Learn - 0 to Hero",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()

# Modern Custom CSS Design
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
    :root {
        --primary: #667eea;
        --primary-dark: #764ba2;
        --secondary: #f093fb;
        --accent: #4facfe;
        --dark: #1a1a2e;
        --light: #f8f9fa;
        --text: #2d3748;
    }
    
    html, body, [class*="css"], * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }

    /* Hide Streamlit's auto-generated multi-page nav (we use custom routing) */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 2px 0 10px rgba(102, 126, 234, 0.2);
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: white !important;
        font-weight: 500;
        font-size: 0.95rem;
        padding: 0.5rem 0;
    }
    
    [data-testid="stSidebar"] .stRadio > div {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.3) !important;
        border-color: white !important;
        transform: translateX(2px);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    /* Main Content */
    .main {
        background: #f8f9fa;
    }
    
    /* Headers */
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        letter-spacing: -0.5px;
    }
    
    h1, h2, h3 {
        color: #1a1a2e;
        font-weight: 700;
        letter-spacing: -0.3px;
    }
    
    h1 { font-size: 2.5rem; }
    h2 { font-size: 2rem; }
    h3 { font-size: 1.5rem; }
    
    /* Cards */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.15);
    }
    
    .card-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
    }
    
    .card-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0.5rem;
    }
    
    /* Course Cards */
    .course-card {
        background: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .course-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
    }
    
    .course-card-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        color: white;
        text-align: center;
        min-height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .course-card-body {
        padding: 1.5rem;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border: 2px solid #e0e0e0 !important;
        border-radius: 8px !important;
        padding: 0.6rem !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 1rem 1.5rem;
        border: none;
        background: #f0f0f0;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Metrics */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        text-align: center;
        border-left: 4px solid #667eea;
    }
    
    /* Success/Error Messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 8px;
        padding: 1rem !important;
    }
    
    .stSuccess {
        background: rgba(76, 175, 80, 0.1) !important;
        border-left: 4px solid #4caf50 !important;
    }
    
    .stError {
        background: rgba(244, 67, 54, 0.1) !important;
        border-left: 4px solid #f44336 !important;
    }
    
    .stWarning {
        background: rgba(255, 152, 0, 0.1) !important;
        border-left: 4px solid #ff9800 !important;
    }
    
    .stInfo {
        background: rgba(33, 150, 243, 0.1) !important;
        border-left: 4px solid #2196f3 !important;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, rgba(102,126,234,0), rgba(102,126,234,0.5), rgba(102,126,234,0));
        margin: 2rem 0;
    }
    
    /* Badge */
    .badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .badge-primary {
        background: rgba(102, 126, 234, 0.2);
        color: #667eea;
    }
    
    .badge-success {
        background: rgba(76, 175, 80, 0.2);
        color: #4caf50;
    }
    
    .badge-warning {
        background: rgba(255, 152, 0, 0.2);
        color: #ff9800;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Text Styling */
    .subtitle {
        color: #757575;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        h1 { font-size: 1.8rem; }
        h2 { font-size: 1.4rem; }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar radio label → internal key mapping for unauthenticated pages
_AUTH_PAGE_MAP = {
    "🏠 Home": "home",
    "📝 Register": "register",
    "🔓 Sign In": "login",
}
_AUTH_PAGE_MAP_REVERSE = {v: k for k, v in _AUTH_PAGE_MAP.items()}

# Main application
def main():
    st.sidebar.title("🤖 AI Learn")

    if is_logged_in():
        user = st.session_state.user
        st.sidebar.success(f"👋 Welcome, {user['username']}!")

        page = st.sidebar.radio(
            "Navigation",
            ["🏠 Home", "📚 Courses", "💪 Exercises", "📝 Quizzes",
             "💬 Community", "👤 Profile", "🏆 Certifications"],
            label_visibility="collapsed"
        )

        if st.sidebar.button("🚪 Log Out", use_container_width=True):
            logout_user()
            st.rerun()

        # Route to pages
        if page == "🏠 Home":
            home.show_dashboard(user)
        elif page == "📚 Courses":
            courses.show_courses(user)
        elif page == "💪 Exercises":
            exercises.show_exercises(user)
        elif page == "📝 Quizzes":
            quiz.show_quizzes(user)
        elif page == "💬 Community":
            forum.show_forum(user)
        elif page == "👤 Profile":
            profile.show_profile(user)
        elif page == "🏆 Certifications":
            certifications.show_certifications(user)
    else:
        # Determine which auth page to show.
        # Programmatic redirects (button clicks) set st.session_state.auth_page.
        # The sidebar radio is the fallback when no programmatic redirect is active.
        if "auth_page" not in st.session_state:
            st.session_state.auth_page = "home"

        # Map current auth_page key back to sidebar label so the radio reflects it
        default_label = _AUTH_PAGE_MAP_REVERSE.get(st.session_state.auth_page, "🏠 Home")
        sidebar_options = list(_AUTH_PAGE_MAP.keys())
        default_idx = sidebar_options.index(default_label)

        selected_label = st.sidebar.radio(
            "Navigation",
            sidebar_options,
            index=default_idx,
            label_visibility="collapsed"
        )

        # Sidebar selection always wins (clears any stale programmatic redirect)
        current_page = _AUTH_PAGE_MAP[selected_label]
        if current_page != st.session_state.auth_page:
            st.session_state.auth_page = current_page

        if st.session_state.auth_page == "home":
            home.show_landing_page()
        elif st.session_state.auth_page == "register":
            home.show_register()
        elif st.session_state.auth_page == "login":
            home.show_login()

if __name__ == "__main__":
    main()
