"""
Course content and curriculum structure
"""

COURSES = {
    "python_fundamentals": {
        "title": "Python Fundamentals for AI",
        "description": "Learn Python basics from scratch - the foundation for AI development",
        "level": "Beginner",
        "duration_hours": 20,
        "lessons": [
            {
                "title": "Getting Started with Python",
                "content": """
# Getting Started with Python

## What is Python?
Python is a high-level, interpreted programming language known for its simplicity and readability.

## Why Python for AI?
- Easy to learn and read
- Extensive libraries (NumPy, Pandas, TensorFlow, PyTorch)
- Large AI/ML community
- Industry standard for machine learning

## Installation
1. Download from python.org
2. Install and add to PATH
3. Verify: `python --version`

## Your First Program
```python
print("Hello, AI Developer!")
```
                """,
                "exercises": [
                    {
                        "title": "Print Your Name",
                        "description": "Write a program that prints your name",
                        "starter_code": "# Write your code here\n",
                        "solution_code": 'print("Your Name")',
                        "difficulty": "Easy"
                    }
                ]
            },
            {
                "title": "Variables and Data Types",
                "content": """
# Variables and Data Types

## What are Variables?
Variables store data values. In Python, you don't need to declare the type.

## Data Types
- **int**: Integer numbers (1, 2, -5)
- **float**: Decimal numbers (3.14, 2.5)
- **str**: Text strings ("hello")
- **bool**: True or False
- **list**: Ordered collection [1, 2, 3]
- **dict**: Key-value pairs {"name": "AI"}

## Variable Naming Rules
- Start with letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive
- Use snake_case for multiple words

## Example
```python
name = "Alice"
age = 25
gpa = 3.8
is_student = True
```
                """,
                "exercises": [
                    {
                        "title": "Create Variables",
                        "description": "Create variables for your personal information",
                        "starter_code": "# Create variables for name, age, and favorite_language\n",
                        "solution_code": 'name = "Your Name"\nage = 25\nfavorite_language = "Python"',
                        "difficulty": "Easy"
                    }
                ]
            },
            {
                "title": "Control Flow - If/Else",
                "content": """
# Control Flow: If/Else Statements

## Making Decisions in Code
Control flow lets your program make decisions.

## If Statement
```python
if condition:
    # Code if condition is True
```

## If/Else Statement
```python
if condition:
    # Code if True
else:
    # Code if False
```

## If/Elif/Else
```python
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

## Comparison Operators
- `==` Equal
- `!=` Not equal
- `<` Less than
- `>` Greater than
- `<=` Less than or equal
- `>=` Greater than or equal
                """,
                "exercises": [
                    {
                        "title": "Grade Calculator",
                        "description": "Create an if/else statement that assigns grades",
                        "starter_code": "score = 85\n# Write code to print the grade (A/B/C/D/F)\n",
                        "solution_code": 'score = 85\nif score >= 90:\n    print("A")\nelif score >= 80:\n    print("B")\nelif score >= 70:\n    print("C")\nelse:\n    print("F")',
                        "difficulty": "Easy"
                    }
                ]
            }
        ]
    },
    "ml_basics": {
        "title": "Machine Learning Basics",
        "description": "Understand core ML concepts, supervised/unsupervised learning, and evaluation metrics",
        "level": "Intermediate",
        "duration_hours": 25,
        "lessons": [
            {
                "title": "What is Machine Learning?",
                "content": """
# Machine Learning Fundamentals

## What is Machine Learning?
Machine Learning is a subset of AI where systems learn from data without being explicitly programmed.

## Three Types of ML

### 1. Supervised Learning
Learn from labeled data (input-output pairs)
- Classification: Predicting categories
- Regression: Predicting continuous values

### 2. Unsupervised Learning
Find patterns in unlabeled data
- Clustering: Grouping similar data
- Dimensionality Reduction: Simplifying data

### 3. Reinforcement Learning
Learn through interaction and rewards
- Agent learns from environment feedback

## ML Workflow
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Selection
5. Training
6. Evaluation
7. Deployment
                """,
                "exercises": []
            }
        ]
    },
    "deep_learning": {
        "title": "Deep Learning Essentials",
        "description": "Neural networks, backpropagation, and practical deep learning with TensorFlow/PyTorch",
        "level": "Advanced",
        "duration_hours": 30,
        "lessons": [
            {
                "title": "Neural Networks Basics",
                "content": """
# Neural Networks Fundamentals

## What is a Neural Network?
Inspired by biological neurons, artificial neural networks are computing systems that learn patterns.

## Basic Components
1. **Neurons**: Process inputs and produce outputs
2. **Weights**: Parameters that get learned
3. **Biases**: Additional learnable parameters
4. **Activation Functions**: Introduce non-linearity

## Network Architecture
- **Input Layer**: Receives features
- **Hidden Layers**: Process information
- **Output Layer**: Produces predictions

## Training
- Forward Pass: Data flows through network
- Loss Calculation: Measure error
- Backward Pass (Backpropagation): Update weights
- Repeat until convergence
                """,
                "exercises": []
            }
        ]
    }
}

def get_all_courses():
    """Get list of all courses"""
    return [(key, course["title"], course["level"]) for key, course in COURSES.items()]

def get_course(course_key):
    """Get detailed course information"""
    return COURSES.get(course_key)

def get_lessons(course_key):
    """Get lessons for a course"""
    course = COURSES.get(course_key)
    if course:
        return course["lessons"]
    return []

def get_lesson(course_key, lesson_index):
    """Get specific lesson"""
    course = COURSES.get(course_key)
    if course and lesson_index < len(course["lessons"]):
        return course["lessons"][lesson_index]
    return None
