import streamlit as st

def show_profile(user):
    """Show user profile page"""
    st.markdown(f"""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>👤 Your Profile</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Manage your account and track your progress</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # Profile info
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class='card'>
            <h3 style='margin-top: 0;'>📋 Profile Information</h3>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Username:</strong> {user['username']}</p>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Email:</strong> {user['email']}</p>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Member Since:</strong> 2024</p>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Last Active:</strong> Today</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card'>
            <h3 style='margin-top: 0;'>📊 Your Statistics</h3>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Courses Enrolled:</strong> 3</p>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Lessons Completed:</strong> 12</p>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Exercises Done:</strong> 24</p>
            <p style='color: #757575; margin: 0.5rem 0;'><strong>Certifications:</strong> 0</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Learning progress
    st.markdown("<h2>📈 Learning Progress</h2>", unsafe_allow_html=True)
    
    progress_data = {
        "Course": ["Python Fundamentals", "ML Basics", "Deep Learning"],
        "Progress": [45, 20, 0],
        "Status": ["In Progress", "In Progress", "Not Started"]
    }
    
    st.dataframe(progress_data, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Settings
    st.markdown("<h2>⚙️ Settings</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Notifications**")
        notifications = st.checkbox("Email Notifications", value=True)
        dark_mode = st.checkbox("Dark Mode", value=False)
    
    with col2:
        st.markdown("**Privacy**")
        public_profile = st.checkbox("Public Profile", value=False)
        newsletter = st.checkbox("Subscribe to Newsletter", value=True)
    
    if st.button("💾 Save Settings", use_container_width=True):
        st.success("✅ Settings saved successfully!")
    
    st.divider()
    
    # Account Management
    st.markdown("<h2>🔐 Account Management</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔑 Change Password", use_container_width=True):
            show_change_password()
    
    with col2:
        if st.button("🗑️ Delete Account", use_container_width=True):
            st.warning("⚠️ This action cannot be undone!")

def show_change_password():
    """Show change password form"""
    st.subheader("Change Password")
    
    with st.form("change_password"):
        current = st.text_input("Current Password", type="password")
        new = st.text_input("New Password", type="password")
        confirm = st.text_input("Confirm New Password", type="password")
        
        submitted = st.form_submit_button("Change Password", use_container_width=True)
        
        if submitted:
            if new == confirm:
                st.success("✅ Password changed successfully!")
            else:
                st.error("❌ Passwords do not match")

