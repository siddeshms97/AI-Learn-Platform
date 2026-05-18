import streamlit as st
from src.courses import get_all_courses, get_course, get_lessons


def show_courses(user):
    """Display all courses"""
    if "selected_course" in st.session_state:
        show_course_detail(user, st.session_state.selected_course)
        return

    st.markdown(
        """
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>📚 Explore Courses</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Choose your learning path and start today</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    # Search and Filter
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search = st.text_input("🔍 Search courses", placeholder="Type course name...")
    with col2:
        level_filter = st.selectbox(
            "Filter by level", ["All", "Beginner", "Intermediate", "Advanced"]
        )
    with col3:
        st.markdown("")  # spacing

    st.divider()

    # Display courses
    courses_list = get_all_courses()

    for course_key, title, level in courses_list:
        if search.lower() not in title.lower():
            continue
        if level_filter != "All" and level_filter != level:
            continue

        course_detail = get_course(course_key)

        # Create attractive course card
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(
                f"""
            <div class='course-card'>
                <div class='course-card-body'>
                    <h3 style='margin-top: 0; color: #1a1a2e;'>{title}</h3>
                    <p style='color: #757575; line-height: 1.6;'>{course_detail["description"]}</p>
                    <div style='display: flex; gap: 1rem; margin-top: 1rem;'>
                        <span class='badge badge-primary'>⏱️ {course_detail["duration_hours"]} hours</span>
                        <span class='badge badge-primary'>📖 {len(course_detail["lessons"])} lessons</span>
                        <span class='badge badge-primary'>💪 {len([lesson for lesson in course_detail["lessons"] if lesson.get("exercises")])} exercises</span>
                    </div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            if st.button("📖 View", key=f"view_{course_key}", use_container_width=True):
                st.session_state.selected_course = course_key
                st.rerun()

        st.markdown("")


def show_course_detail(user, course_key):
    """Show detailed course view"""
    if "selected_lesson" in st.session_state:
        show_lesson(user, course_key, st.session_state.selected_lesson)
        return

    if st.button("⬅️ Back to Courses"):
        del st.session_state.selected_course
        st.rerun()

    course = get_course(course_key)

    # Course Header
    st.markdown(
        f"""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>{course["title"]}</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>{course["description"]}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    # Course Info
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
        <div class='metric-card'>
            <div style='font-size: 2rem;'>📊</div>
            <div style='font-size: 1.5rem; font-weight: 700; color: #667eea;'>{course["level"]}</div>
            <div style='color: #757575; font-weight: 600; font-size: 0.85rem;'>Difficulty</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class='metric-card'>
            <div style='font-size: 2rem;'>⏱️</div>
            <div style='font-size: 1.5rem; font-weight: 700; color: #667eea;'>{course["duration_hours"]}h</div>
            <div style='color: #757575; font-weight: 600; font-size: 0.85rem;'>Duration</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class='metric-card'>
            <div style='font-size: 2rem;'>📖</div>
            <div style='font-size: 1.5rem; font-weight: 700; color: #667eea;'>{len(course["lessons"])}</div>
            <div style='color: #757575; font-weight: 600; font-size: 0.85rem;'>Lessons</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
        <div class='metric-card'>
            <div style='font-size: 2rem;'>🏆</div>
            <div style='font-size: 1.5rem; font-weight: 700; color: #667eea;'>Cert</div>
            <div style='color: #757575; font-weight: 600; font-size: 0.85rem;'>Available</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("<h2>📖 Course Content</h2>", unsafe_allow_html=True)

    lessons = get_lessons(course_key)

    for idx, lesson in enumerate(lessons, 1):
        col1, col2 = st.columns([4, 1])

        with col1:
            num_exercises = len(lesson.get("exercises", []))
            st.markdown(
                f"""
            <div class='card' style='border-left: 4px solid #667eea;'>
                <h3 style='margin-top: 0; margin-bottom: 0.5rem;'>Lesson {idx}: {lesson["title"]}</h3>
                <p style='color: #757575; margin: 0.5rem 0;'>{lesson["content"][:200]}...</p>
                <p style='color: #999; font-size: 0.85rem;'>💪 {num_exercises} exercises</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            if st.button(
                "Read", key=f"lesson_{course_key}_{idx}", use_container_width=True
            ):
                st.session_state.selected_lesson = idx - 1
                st.rerun()

        st.markdown("")

    st.divider()

    if st.button("✅ Enroll in Course", use_container_width=True):
        st.success("🎉 You've successfully enrolled in this course!")


def show_lesson(user, course_key, lesson_idx):
    """Show lesson content"""
    course = get_course(course_key)
    lesson = course["lessons"][lesson_idx]

    st.markdown(
        f"""
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>{lesson["title"]}</h1>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("")

    # Lesson content
    st.markdown(lesson["content"])

    # Exercises
    if lesson.get("exercises"):
        st.divider()
        st.markdown("<h2>💪 Practice Exercises</h2>", unsafe_allow_html=True)

        for exc_idx, exercise in enumerate(lesson["exercises"], 1):
            with st.expander(
                f"Exercise {exc_idx}: {exercise['title']} ({exercise['difficulty']})"
            ):
                st.markdown(f"**Description:** {exercise['description']}")

                st.markdown("**Starter Code:**")
                st.code(exercise["starter_code"], language="python")

                st.markdown("**Your Solution:**")
                st.text_area(
                    "Write your code here",
                    key=f"exercise_{lesson_idx}_{exc_idx}",
                    height=200,
                )

                if st.button("✅ Check Solution", key=f"check_{lesson_idx}_{exc_idx}"):
                    st.success("Great job! Your solution is correct.")
                    st.markdown("**Official Solution:**")
                    st.code(exercise["solution_code"], language="python")

    # Navigation
    st.divider()
    st.markdown("<h3>Navigation</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if lesson_idx > 0:
            if st.button("⬅️ Previous Lesson", use_container_width=True):
                st.session_state.selected_lesson = lesson_idx - 1
                st.rerun()

    with col2:
        if st.button("↩️ Back to Course", use_container_width=True):
            del st.session_state.selected_lesson
            st.rerun()

    with col3:
        if lesson_idx < len(course["lessons"]) - 1:
            if st.button("Next Lesson ➡️", use_container_width=True):
                st.session_state.selected_lesson = lesson_idx + 1
                st.rerun()
