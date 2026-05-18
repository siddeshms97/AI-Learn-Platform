# 🤖 AI Learn - From 0 to AI Developer Hero

A comprehensive web-based learning platform for aspiring AI developers, built with Streamlit. Learn Python, Machine Learning, and Deep Learning from scratch with interactive lessons, exercises, quizzes, and community support.

## Features

- 📚 **Structured Curriculum**: Three comprehensive courses (Python Fundamentals → ML Basics → Deep Learning)
- 💻 **Interactive Exercises**: Write and test code directly in the browser
- 📝 **Quizzes & Assessments**: Evaluate your knowledge with interactive quizzes
- 💬 **Community Forum**: Discuss with other learners and get help
- 🏆 **Certifications**: Earn verifiable certificates upon course completion
- 👤 **Progress Tracking**: Monitor your learning journey and stay motivated
- 🔐 **User Authentication**: Secure login and registration

## Project Structure

```
AI Learn/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Project dependencies
├── README.md                 # This file
├── src/
│   ├── __init__.py
│   ├── db.py                # Database setup and queries
│   ├── auth.py              # Authentication and password hashing
│   └── courses.py           # Course content and curriculum
├── pages/
│   ├── __init__.py
│   ├── home.py              # Landing page, login, register
│   ├── courses.py           # Course listing and content
│   ├── exercises.py         # Interactive exercises
│   ├── quiz.py              # Quizzes and assessments
│   ├── forum.py             # Community forum
│   ├── profile.py           # User profile and settings
│   └── certifications.py    # Certificates and achievements
├── data/                    # SQLite database location
├── courses/                 # Course content files (future)
└── assets/                  # Images and static files
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or download the project**
```bash
cd "AI Learn"
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open in browser**
The application will automatically open at `http://localhost:8501`

## Usage

### For New Users
1. Click "Register" in the sidebar
2. Create your account with username, email, and password
3. Log in with your credentials
4. Start with Python Fundamentals course

### For Learners
1. **Browse Courses**: View all available courses and their descriptions
2. **Enroll**: Click "Enroll" to add a course to your dashboard
3. **Learn**: Read lessons with interactive content
4. **Practice**: Complete exercises with starter code
5. **Quiz**: Test your knowledge with quizzes
6. **Forum**: Ask questions and help others
7. **Certificate**: Earn certificates upon course completion

## Course Curriculum

### 1. Python Fundamentals for AI (20 hours)
- Getting Started with Python
- Variables and Data Types
- Control Flow (If/Else)
- Functions and Loops
- Object-Oriented Programming
- Working with Libraries

### 2. Machine Learning Basics (25 hours)
- What is Machine Learning?
- Supervised Learning
- Unsupervised Learning
- Model Evaluation
- Scikit-learn Fundamentals
- Real-world ML Projects

### 3. Deep Learning Essentials (30 hours)
- Neural Networks Fundamentals
- Convolutional Neural Networks (CNNs)
- Recurrent Neural Networks (RNNs)
- TensorFlow/Keras
- PyTorch Basics
- Deploying Models

## Database Schema

The application uses SQLite with the following main tables:
- **users**: User accounts and authentication
- **courses**: Course information
- **lessons**: Individual lesson content
- **exercises**: Coding exercises
- **user_progress**: Track learning progress
- **quizzes**: Quiz questions and answers
- **forum_posts**: Community discussions
- **certifications**: Earned certificates

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite3
- **Authentication**: bcrypt
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Plotly

## Features in Development

- [ ] Interactive code execution environment
- [ ] Real-time code collaboration
- [ ] Advanced analytics dashboard
- [ ] Mobile app version
- [ ] Video lessons
- [ ] AI-powered learning recommendations
- [ ] Industry partnerships and job board

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Roadmap

- Q3 2024: Video lessons and live coding sessions
- Q4 2024: AI-powered learning paths
- Q1 2025: Mobile application
- Q2 2025: Industry partnerships and certifications

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- 📧 Email: support@ailearn.com
- 💬 Forum: In-app community forum
- 📚 Documentation: Check README and course content
- 🐛 Issues: Report bugs in the GitHub issues tab

## Acknowledgments

- Inspired by platforms like Codecademy, Coursera, and DataCamp
- Python and AI communities for inspiration
- Open source libraries that make this possible

---

**Happy Learning! 🚀 Start your journey to becoming an AI developer hero today!**
