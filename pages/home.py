import streamlit as st
import pyotp
import qrcode
from src.auth import register_user, login_user


def show_landing_page():
    """Landing page for unauthenticated users"""

    # Hero Section
    st.markdown(
        """
    <div style='text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); 
    border-radius: 16px; color: white; margin-bottom: 3rem;'>
        <h1 style='font-size: 3.5rem; margin: 0; font-weight: 800;'>🤖 AI Learn</h1>
        <p style='font-size: 1.8rem; margin: 1rem 0 0 0; font-weight: 300; opacity: 0.95;'>From Zero to AI Developer Hero</p>
        <p style='font-size: 1rem; margin-top: 1rem; opacity: 0.8; max-width: 600px; margin-left: auto; margin-right: auto;'>
            Master Python, Machine Learning, and Deep Learning with hands-on projects and expert guidance
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Stats Section
    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        ("📚", "75+", "Lessons"),
        ("💻", "150+", "Exercises"),
        ("🎯", "3", "Courses"),
        ("👥", "10K+", "Learners"),
    ]

    for col, (emoji, number, label) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(
                f"""
            <div class='metric-card'>
                <div style='font-size: 2.5rem;'>{emoji}</div>
                <div style='font-size: 2rem; font-weight: 700; color: #667eea;'>{number}</div>
                <div style='color: #757575; font-weight: 600;'>{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Learning Path
    st.markdown(
        "<h2 style='text-align: center; margin-bottom: 3rem;'>📈 Your Learning Journey</h2>",
        unsafe_allow_html=True,
    )

    path_col1, path_col2, path_col3 = st.columns(3)

    courses_info = [
        (
            "🐍",
            "Python & Production",
            "20 hours",
            "Beginner",
            "Master Python basics, APIs, and Data Engineering",
        ),
        (
            "🤖",
            "ML & MLOps",
            "25 hours",
            "Intermediate",
            "Learn ML algorithms, Docker, Kubernetes, CI/CD",
        ),
        (
            "⚡",
            "LLMs & AI Agents",
            "30 hours",
            "Advanced",
            "RAG architectures, AI Agents, and LLM integration",
        ),
    ]

    for col, (emoji, title, hours, level, desc) in zip(
        [path_col1, path_col2, path_col3], courses_info
    ):
        with col:
            st.markdown(
                f"""
            <div class='course-card'>
                <div class='course-card-header' style='font-size: 3rem;'>{emoji}</div>
                <div class='course-card-body'>
                    <h3 style='margin-top: 0;'>{title}</h3>
                    <p style='color: #667eea; font-weight: 600;'>{hours} • {level}</p>
                    <p style='color: #757575; font-size: 0.95rem;'>{desc}</p>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Features Section
    st.markdown(
        "<h2 style='text-align: center; margin-bottom: 3rem;'>✨ Why Choose AI Learn?</h2>",
        unsafe_allow_html=True,
    )

    features = [
        ("🎓", "Expert Content", "Curriculum designed by AI industry professionals"),
        ("💪", "Hands-On Practice", "100+ exercises with instant feedback"),
        ("🏆", "Certifications", "Recognized certificates upon completion"),
        ("💬", "Community Support", "Active forums and peer learning"),
        ("📊", "Progress Tracking", "Detailed analytics and personalized dashboards"),
        ("🎯", "Self-Paced", "Learn at your own speed, anytime, anywhere"),
    ]

    feat_col1, feat_col2, feat_col3 = st.columns(3)

    for i, (emoji, title, desc) in enumerate(features):
        col = [feat_col1, feat_col2, feat_col3][i % 3]
        with col:
            st.markdown(
                f"""
            <div class='card' style='text-align: center;'>
                <div style='font-size: 2.5rem; margin-bottom: 1rem;'>{emoji}</div>
                <h3 style='margin-top: 0; margin-bottom: 0.5rem;'>{title}</h3>
                <p style='color: #757575; font-size: 0.95rem;'>{desc}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # CTA Section
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("📝 Create Account", use_container_width=True, key="cta_register"):
            st.session_state.auth_page = "register"
            st.rerun()

    with col2:
        if st.button("🔓 Sign In", use_container_width=True, key="cta_login"):
            st.session_state.auth_page = "login"
            st.rerun()

    st.divider()

    # Testimonials Section
    st.markdown(
        "<h2 style='text-align: center; margin-bottom: 3rem;'>⭐ What Our Learners Say</h2>",
        unsafe_allow_html=True,
    )

    testimonials = [
        (
            "Priya",
            "⭐⭐⭐⭐⭐",
            "This platform changed my career! I went from zero coding knowledge to landing an ML internship.",
        ),
        (
            "Alex",
            "⭐⭐⭐⭐⭐",
            "The hands-on exercises are incredible. I actually understand the concepts now.",
        ),
        (
            "Jordan",
            "⭐⭐⭐⭐⭐",
            "Best investment for learning AI. The community is super helpful!",
        ),
    ]

    test_col1, test_col2, test_col3 = st.columns(3)

    for col, (name, rating, text) in zip(
        [test_col1, test_col2, test_col3], testimonials
    ):
        with col:
            st.markdown(
                f"""
            <div class='card'>
                <p style='font-size: 1.2rem; margin-bottom: 0.5rem;'>{rating}</p>
                <p style='color: #757575; font-style: italic; margin: 1rem 0;'>"{text}"</p>
                <p style='font-weight: 700; color: #667eea;'>— {name}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )


def show_register():
    """Registration page"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            """
        <div class='card-header' style='text-align: center;'>
            <h2 style='color: white; margin: 0;'>📝 Create Your Account</h2>
            <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Join 10,000+ AI Learners Today</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # OAuth Buttons
        oauth_col1, oauth_col2 = st.columns(2)
        with oauth_col1:
            if st.button("🌐 Continue with Google", use_container_width=True):
                st.success("Google OAuth simulated successfully! You can now sign in.")
        with oauth_col2:
            if st.button("💼 Continue with LinkedIn", use_container_width=True):
                st.success("LinkedIn OAuth simulated successfully! You can now sign in.")

        st.markdown("<div style='text-align: center; margin: 1.5rem 0; color: #757575; font-size: 0.9rem; font-weight: 600;'>OR REGISTER VIA EMAIL</div>", unsafe_allow_html=True)

        with st.form("register_form"):
            username = st.text_input("Username", placeholder="Choose a unique username")
            email = st.text_input("Email", placeholder="your@email.com")
            
            st.markdown("<label style='font-size: 0.9rem; color: #31333F;'>Mobile Number (for 2FA)</label>", unsafe_allow_html=True)
            mobile_col1, mobile_col2 = st.columns([1, 2])
            with mobile_col1:
                country_code = st.selectbox("Code", ["+1 (US)", "+44 (UK)", "+91 (IN)", "+61 (AU)", "+81 (JP)", "+49 (DE)"], label_visibility="collapsed")
            with mobile_col2:
                mobile = st.text_input("Mobile Number", placeholder="234 567 8900", label_visibility="collapsed")
            password = st.text_input(
                "Password", type="password", placeholder="At least 6 characters"
            )
            password_confirm = st.text_input("Confirm Password", type="password")

            st.markdown("")
            col_a, col_b = st.columns(2)

            with col_a:
                submitted = st.form_submit_button(
                    "Create Account", use_container_width=True
                )

            with col_b:
                if st.form_submit_button("← Back to Home", use_container_width=True):
                    st.session_state.auth_page = "home"
                    st.rerun()

            if submitted:
                # We can store mobile number in db, but for now we just mock it in UI
                if not mobile:
                    st.warning("⚠️ Mobile Number is recommended for 2-Step Verification.")
                
                success, message, totp_secret = register_user(
                    username, email, password, password_confirm
                )
                if success:
                    st.success(message)
                    st.info(
                        "🎉 Account created! Please set up your Authenticator app by scanning the QR code below, then sign in."
                    )
                    
                    if totp_secret:
                        uri = pyotp.totp.TOTP(totp_secret).provisioning_uri(name=email, issuer_name="AI Learn")
                        qr = qrcode.make(uri)
                        
                        st.image(qr.get_image(), caption="Scan with Google Authenticator or Authy", width=250)
                        st.code(totp_secret, language="plaintext")
                        st.markdown("<p style='text-align:center; color:#757575;'>If you can't scan the QR code, manually enter the secret key above.</p>", unsafe_allow_html=True)

                else:
                    st.error(f"❌ {message}")


def show_login():
    """Login page"""
    if "pending_2fa_user" in st.session_state:
        show_2fa_verification()
        return

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            """
        <div class='card-header' style='text-align: center;'>
            <h2 style='color: white; margin: 0;'>🔓 Welcome Back</h2>
            <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Sign in to continue your learning journey</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # OAuth Buttons
        oauth_col1, oauth_col2 = st.columns(2)
        with oauth_col1:
            if st.button("🌐 Sign in with Google", use_container_width=True):
                st.info("Simulating Google Login... Proceeding to 2FA.")
                st.session_state.pending_2fa_user = {"username": "GoogleUser", "id": 999}
                st.rerun()
        with oauth_col2:
            if st.button("💼 Sign in with LinkedIn", use_container_width=True):
                st.info("Simulating LinkedIn Login... Proceeding to 2FA.")
                st.session_state.pending_2fa_user = {"username": "LinkedInUser", "id": 998}
                st.rerun()

        st.markdown("<div style='text-align: center; margin: 1.5rem 0; color: #757575; font-size: 0.9rem; font-weight: 600;'>OR LOGIN VIA EMAIL / USERNAME</div>", unsafe_allow_html=True)

        with st.form("login_form"):
            identifier = st.text_input("Username / Email", placeholder="Your username or email")
            password = st.text_input(
                "Password", type="password", placeholder="Your password"
            )

            st.markdown("")
            col_a, col_b = st.columns(2)

            with col_a:
                submitted = st.form_submit_button("Sign In", use_container_width=True)

            with col_b:
                if st.form_submit_button("← Back to Home", use_container_width=True):
                    st.session_state.auth_page = "home"
                    st.rerun()

            if submitted:
                success, result = login_user(identifier, password)
                if success:
                    # Trigger 2-Step Verification
                    st.session_state.pending_2fa_user = dict(result)
                    st.rerun()
                else:
                    st.error(f"❌ {result}")

def show_2fa_verification():
    """2-Step Verification Screen"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            """
        <div class='card-header' style='text-align: center;'>
            <h2 style='color: white; margin: 0;'>🔐 2-Step Verification</h2>
            <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>For extra security, please verify your identity</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.info("📲 Open your Authenticator App (e.g. Google Authenticator) and enter the 6-digit code for AI Learn.")
        
        with st.form("2fa_form"):
            verification_code = st.text_input("Authenticator Code", placeholder="Enter 6-digit code")
            
            st.markdown("")
            col_a, col_b = st.columns(2)
            with col_a:
                verified = st.form_submit_button("Verify & Login", use_container_width=True)
            with col_b:
                if st.form_submit_button("Cancel", use_container_width=True):
                    del st.session_state.pending_2fa_user
                    st.rerun()
            
            if verified:
                user = st.session_state.pending_2fa_user
                totp_secret = user.get("totp_secret")
                
                is_valid = False
                if totp_secret:
                    totp = pyotp.TOTP(totp_secret)
                    is_valid = totp.verify(verification_code.strip())
                else:
                    # Legacy user bypass (or prompt to set up)
                    is_valid = True
                    
                if is_valid:
                    del st.session_state.pending_2fa_user
                    st.session_state.user = user
                    st.success(f"🎉 Verification successful! Welcome back, {user['username']}!")
                    st.rerun()
                else:
                    st.error("❌ Incorrect verification code. Please try again.")


def show_dashboard(user):
    """Dashboard for logged-in users"""
    # Welcome Section
    st.markdown(
        f"""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>👋 Welcome back, {user["username"]}!</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Keep up the momentum and continue learning</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        (col1, "📚", "Courses Enrolled", "3", "2 in progress"),
        (col2, "✅", "Lessons Completed", "12", "+3 this week"),
        (col3, "💪", "Exercises Done", "24", "+12 this week"),
        (col4, "🔥", "Learning Streak", "7 days", "Keep it up!"),
    ]

    for col, emoji, label, value, detail in metrics:
        with col:
            st.markdown(
                f"""
            <div class='metric-card'>
                <div style='font-size: 2rem;'>{emoji}</div>
                <div style='font-size: 2.2rem; font-weight: 700; color: #667eea; margin: 0.5rem 0;'>{value}</div>
                <div style='color: #757575; font-weight: 600; font-size: 0.9rem;'>{label}</div>
                <div style='color: #999; font-size: 0.85rem; margin-top: 0.3rem;'>{detail}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Courses In Progress
    st.markdown("<h2>📖 Continue Learning</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    courses = [
        (col1, "🐍", "Python & Production", "45%", "9/20 hours completed"),
        (col2, "🤖", "ML & MLOps", "20%", "5/25 hours completed"),
        (col3, "⚡", "LLMs & AI Agents", "0%", "Not started"),
    ]

    for col, emoji, title, progress, detail in courses:
        with col:
            st.markdown(
                f"""
            <div class='course-card'>
                <div class='course-card-header' style='font-size: 2.5rem;'>{emoji}</div>
                <div class='course-card-body'>
                    <h3 style='margin-top: 0;'>{title}</h3>
                    <p style='color: #757575; font-size: 0.9rem;'>{detail}</p>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.progress(int(progress.replace("%", "")) / 100, text=progress)

    st.divider()

    # Recommendations
    st.markdown("<h2>🎯 Next Steps</h2>", unsafe_allow_html=True)

    rec_col1, rec_col2 = st.columns(2)

    with rec_col1:
        st.markdown(
            """
        <div class='card' style='border-left: 4px solid #667eea;'>
            <h3 style='margin-top: 0;'>📖 Continue Lesson</h3>
            <p>Complete "Data Engineering & Preprocessing" in Python & Production</p>
            <p style='color: #667eea; font-weight: 600;'>→ Resume Learning</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with rec_col2:
        st.markdown(
            """
        <div class='card' style='border-left: 4px solid #667eea;'>
            <h3 style='margin-top: 0;'>💪 Practice Exercise</h3>
            <p>Solve the "Fibonacci Generator" exercise to strengthen your skills</p>
            <p style='color: #667eea; font-weight: 600;'>→ Start Exercise</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    # Recent activity
    st.markdown("### 📊 Your Recent Activity")

    activity_data = {
        "Course": ["Python & Production", "ML & MLOps", "LLMs & AI Agents"],
        "Progress": [45, 20, 0],
        "Last Accessed": ["Today", "2 days ago", "Not started"],
    }

    st.dataframe(activity_data, use_container_width=True)

    st.divider()

    # Recommended next steps
    st.markdown("### 🎯 Recommended Next Steps")
    st.info("""
    - **Complete Python Module 2**: Building your first API
    - **Take the Python Quiz**: Test your fundamentals knowledge
    - **Join the Forum**: Ask questions and help others
    """)
