import streamlit as st


def show_forum(user):
    """Display forum/community page"""
    if "selected_post" in st.session_state:
        show_forum_post(st.session_state.selected_post)
        return

    st.markdown(
        """
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>💬 Community Forum</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Ask questions, share ideas, and learn together</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        search = st.text_input(
            "🔍 Search discussions", placeholder="Search forum posts..."
        )

    with col2:
        st.markdown("")

    with col3:
        if st.button("➕ New Discussion", use_container_width=True):
            st.session_state.creating_post = True
            st.rerun()

    if st.session_state.get("creating_post"):
        show_create_post()
        return

    st.divider()

    # Sample forum posts
    posts = [
        {
            "title": "How to start with Python APIs?",
            "author": "Alex",
            "category": "Python & Production",
            "replies": 5,
            "views": 42,
            "content": "I'm new to FastAPI and want to build AI APIs. Where should I start?",
            "solved": False,
        },
        {
            "title": "Best practices for Dockerizing ML models",
            "author": "Jordan",
            "category": "ML & MLOps",
            "replies": 8,
            "views": 156,
            "content": "What are the best practices for creating Dockerfiles for ML projects?",
            "solved": True,
        },
        {
            "title": "RAG vs Fine-tuning",
            "author": "Sam",
            "category": "LLMs & AI Agents",
            "replies": 12,
            "views": 203,
            "content": "When should I use Retrieval-Augmented Generation versus fine-tuning an LLM?",
            "solved": False,
        },
    ]

    for post in posts:
        if search.lower() and search.lower() not in post["title"].lower():
            continue

        solved_badge = "✅" if post["solved"] else ""

        col1, col2, col3, col4, col5 = st.columns([3, 0.5, 0.5, 0.5, 0.5])

        with col1:
            st.markdown(
                f"""
            <div class='card' style='border-left: 4px solid #667eea;'>
                <h3 style='margin-top: 0; margin-bottom: 0.5rem;'>{solved_badge} {post["title"]}</h3>
                <p style='color: #757575; font-size: 0.9rem; margin: 0.3rem 0;'>By <strong>{post["author"]}</strong> • {post["category"]}</p>
                <p style='color: #999; font-size: 0.85rem; margin: 0.3rem 0;'>{post["content"][:100]}...</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                f"<div style='text-align: center;'><strong style='font-size: 1.2rem;'>{post['replies']}</strong><br><small style='color: #999;'>💬</small></div>",
                unsafe_allow_html=True,
            )

        with col3:
            st.markdown(
                f"<div style='text-align: center;'><strong style='font-size: 1.2rem;'>{post['views']}</strong><br><small style='color: #999;'>👁️</small></div>",
                unsafe_allow_html=True,
            )

        with col4:
            st.markdown("")

        with col5:
            if st.button("View", key=f"post_{post['title']}", use_container_width=True):
                st.session_state.selected_post = post
                st.rerun()

        st.markdown("")


def show_create_post():
    """Show create new discussion form"""
    if st.button("⬅️ Back to Forum"):
        del st.session_state.creating_post
        st.rerun()
        
    st.subheader("Create New Discussion")

    with st.form("create_post"):
        title = st.text_input("Discussion Title")
        category = st.selectbox(
            "Category",
            ["Python & Production", "ML & MLOps", "LLMs & AI Agents", "General"],
        )
        content = st.text_area("Your Question/Discussion", height=200)

        submitted = st.form_submit_button("Post Discussion")

        if submitted and title and content:
            st.success("Discussion posted successfully!")


def show_forum_post(post):
    """Show forum post with replies"""
    if st.button("⬅️ Back to Forum"):
        del st.session_state.selected_post
        st.rerun()

    st.title(post["title"])

    st.markdown(f"**Posted by:** {post['author']} | **Category:** {post['category']}")
    st.markdown(f"**Views:** {post['views']} | **Replies:** {post['replies']}")

    st.divider()

    st.markdown("### Original Question")
    st.markdown(post["content"])

    st.divider()

    st.markdown("### Replies")

    # Sample replies
    replies = [
        {
            "author": "Morgan",
            "content": "Start with Python basics first. The course covers everything you need!",
            "helpful": 12,
        },
        {
            "author": "Casey",
            "content": "I'd recommend doing the Python module first, then jumping into ML basics.",
            "helpful": 8,
        },
    ]

    for reply in replies:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"**{reply['author']}**")
            st.markdown(reply["content"])

        with col2:
            st.markdown(f"👍 {reply['helpful']}")

    st.divider()

    # Reply form
    st.markdown("### Your Reply")
    reply_text = st.text_area("Write your response", height=150)

    if st.button("Post Reply"):
        if reply_text:
            st.success("Reply posted!")
        else:
            st.warning("Please write a reply first")
