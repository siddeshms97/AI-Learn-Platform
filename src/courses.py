"""
Course content and curriculum structure
"""

COURSES = {
    "math_stats_ai": {
        "title": "Mathematics & Statistics for AI",
        "description": "Essential mathematical foundations required for understanding and building modern AI models.",
        "level": "Beginner",
        "duration_hours": 15,
        "lessons": [
            {
                "title": "Linear Algebra & Calculus for AI",
                "content": """
# Linear Algebra & Calculus for AI

## Linear Algebra
Linear Algebra is the language of machine learning. Data is represented as vectors and matrices, and neural networks are essentially a series of matrix multiplications.
- **Vectors & Matrices**: Representing data points and transformations.
- **Matrix Multiplication**: The core operation in neural networks.
- **Eigenvalues & Eigenvectors**: Essential for dimensionality reduction techniques like PCA.

## Calculus
Calculus, specifically differential calculus, is how models learn.
- **Derivatives & Gradients**: Understanding how changing a parameter affects the error.
- **Chain Rule**: The mathematical engine behind backpropagation in deep learning.

**Real-world Scenario:**
When fine-tuning a Large Language Model (LLM) on a custom dataset, understanding gradients helps you debug issues like "exploding gradients" or "vanishing gradients", allowing you to adjust learning rates or choose appropriate activation functions effectively.
                """,
                "exercises": []
            },
            {
                "title": "Probability & Statistics",
                "content": """
# Probability & Statistics

## Making Sense of Data
AI is essentially probabilistic pattern matching. You need statistics to evaluate your models and probability to understand their predictions.
- **Distributions**: Normal, Binomial, Poisson distributions.
- **Bayes' Theorem**: Updating probabilities based on new evidence—fundamental to many ML algorithms.
- **Hypothesis Testing & P-values**: Determining if your model's improvement is statistically significant or just random noise.

**Real-world Scenario:**
An AI Engineer at an e-commerce company trains a new recommendation algorithm. Before rolling it out to all users, they run an A/B test. Using hypothesis testing and statistical significance, they prove the new model increases sales by 4% without it just being a random fluke.
                """,
                "exercises": []
            }
        ]
    },
    "python_fundamentals": {
        "title": "Python & Production Engineering",
        "description": "Learn Python basics, Data Engineering, and MLOps fundamentals required for modern AI.",
        "level": "Beginner",
        "duration_hours": 20,
        "lessons": [
            {
                "title": "Python for AI Developers & FastAPI",
                "content": """
# Python for AI Developers & FastAPI

## Beyond Basics
Modern AI developers need more than just scripts. You need to write production-ready code. FastAPI is the go-to framework for serving ML models because of its speed and asynchronous capabilities.

## Best Practices for AI Inference in FastAPI
The most common mistake is running heavy AI inference directly in an `async def` endpoint, which blocks the event loop.

1. **Handling Inference (CPU-Bound vs. Async)**:
   - **Don't block the event loop:** FastAPI’s `async` event loop is designed for I/O-bound tasks.
   - **Use `run_in_threadpool`:** For CPU-bound inference, use standard `def` endpoints, which FastAPI automatically executes in a separate thread pool. Alternatively, if you must use `async def`, you can explicitly offload the prediction using `starlette.concurrency.run_in_threadpool`.

2. **Model Loading & Lifecycle**:
   - **Load models on startup:** Load your model into memory during the application startup phase using FastAPI’s lifespan events—not inside the request endpoint.
   - **Keep it in memory:** Store the loaded model in a global state so it can be reused across all requests.

**Real-world Scenario:**
A fintech startup needs to serve a fraud detection model. Every transaction hitting the API must be evaluated in under 50ms. By using FastAPI's lifespan events to load the XGBoost model into memory at startup, and using threadpools for the CPU-bound inference, the team successfully handles 10,000 requests per second without dropping connections.

## Your First API
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["model"] = load_my_model()
    yield
    # Clean up
    ml_models.clear()

app = FastAPI(lifespan=lifespan)

@app.post("/predict")
def predict(data: dict):
    # Standard def runs in threadpool, not blocking event loop
    return ml_models["model"].predict(data)
```
                """,
                "exercises": [
                    {
                        "title": "Build a Lifespan API",
                        "description": "Write a simple FastAPI endpoint using lifespan to load a dummy dictionary as a 'model'.",
                        "starter_code": "from fastapi import FastAPI\n\n# Create your app here\n",
                        "solution_code": 'from contextlib import asynccontextmanager\nfrom fastapi import FastAPI\n\nmodels = {}\n@asynccontextmanager\nasync def lifespan(app: FastAPI):\n    models["dummy"] = "loaded"\n    yield\n    models.clear()\n\napp = FastAPI(lifespan=lifespan)\n\n@app.get("/")\ndef home():\n    return {"model_status": models.get("dummy")}',
                        "difficulty": "Medium",
                    }
                ],
            },
            {
                "title": "Data Engineering & Preprocessing",
                "content": """
# Data Engineering & Preprocessing

## The Importance of Data
AI is only as good as the data it's trained on. AI engineers spend a significant amount of time cleaning and processing data.

## Key Skills
- **SQL / NoSQL**: Querying large datasets.
- **Pandas & Polars**: Data manipulation and cleaning (Polars for high-performance multi-threading).
- **Feature Engineering**: Transforming raw data into meaningful features.

**Real-world Scenario:**
A logistics company streams IoT data from thousands of delivery trucks. An AI Developer builds a data pipeline using Apache Kafka and Python (Pandas/Polars) to clean the messy sensor data (handling missing GPS coordinates and outlier speed values) before feeding it into a predictive maintenance model that forecasts engine failures.

## Example: Cleaning with Pandas
```python
import pandas as pd

df = pd.read_csv("data.csv")
df.dropna(inplace=True) # Remove missing values
df['feature'] = df['feature'] / 255.0 # Normalize
```
                """,
                "exercises": [
                    {
                        "title": "Normalize Data",
                        "description": "Write a function to normalize a list of numbers between 0 and 1.",
                        "starter_code": "def normalize(data):\n    pass\n",
                        "solution_code": "def normalize(data):\n    min_val = min(data)\n    max_val = max(data)\n    return [(x - min_val) / (max_val - min_val) for x in data]",
                        "difficulty": "Easy",
                    }
                ],
            },
        ],
    },
    "ml_basics": {
        "title": "Machine Learning & MLOps",
        "description": "Master ML algorithms, model evaluation, and deployment using Docker and Kubernetes.",
        "level": "Intermediate",
        "duration_hours": 25,
        "lessons": [
            {
                "title": "Applied Machine Learning",
                "content": """
# Applied Machine Learning

## Core Algorithms
- **Supervised Learning**: Classification and Regression (Random Forests, Gradient Boosting like XGBoost/LightGBM).
- **Unsupervised Learning**: Clustering (K-Means) and Dimensionality Reduction (PCA).

## Model Evaluation
In production, accuracy isn't enough.
- Precision, Recall, F1-Score for imbalanced datasets.
- ROC-AUC curves.
- Cross-validation to prevent overfitting.

**Real-world Scenario:**
A SaaS company wants to predict customer churn. The dataset is highly imbalanced (only 2% of users churn). An AI Developer uses SMOTE to balance the dataset and focuses on the "Recall" metric instead of accuracy to ensure they catch as many at-risk customers as possible, triggering automated retention emails.
                """,
                "exercises": [],
            },
            {
                "title": "MLOps & Kubernetes Deployment",
                "content": """
# MLOps & Kubernetes Deployment

## Bridging the Gap to Production
A model on a laptop is useless. AI Developers must deploy models reliably.

## Core Concepts
1. **Containerize Your ML Model (Docker)**
   Docker packages your ML model, dependencies, and runtime environment into a single, portable container. This solves the "it works on my machine" problem.
2. **Kubernetes (K8s)**
   An orchestration platform that automates the deployment, scaling, and management of these containers. It handles load balancing, self-healing, and auto-scaling.

**Real-world Scenario:**
An AI image generation startup goes viral on Twitter. Traffic spikes from 100 requests/hour to 50,000 requests/minute. Because the AI Developer containerized the model with Docker and deployed it on Kubernetes, the K8s Horizontal Pod Autoscaler (HPA) automatically provisions 200 new GPU-enabled pods to handle the load, preventing the service from crashing.

## Example Dockerfile for ML
```dockerfile
FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```
                """,
                "exercises": [],
            },
        ],
    },
    "deep_learning": {
        "title": "LLMs, RAG & AI Agents",
        "description": "Build modern AI applications using Large Language Models, RAG architectures, and AI Agents.",
        "level": "Advanced",
        "duration_hours": 30,
        "lessons": [
            {
                "title": "Deep Learning & Frameworks",
                "content": """
# Deep Learning & Frameworks

## The Foundation
Neural networks, CNNs, and RNNs built the modern AI boom. Transformers revolutionized NLP.

## Frameworks
- **PyTorch**: The industry standard for research and modern production AI.
- **TensorFlow**: Highly adopted in enterprise environments.

Understanding tensors, backpropagation, and distributed training is crucial for fine-tuning models.

**Real-world Scenario:**
A manufacturing company needs an automated visual inspection system. An AI Developer uses PyTorch to fine-tune a pre-trained ResNet50 model on thousands of images of scratched and dented metal parts. The model is then deployed to edge devices on the factory floor, identifying defects in milliseconds and stopping the assembly line when necessary.
                """,
                "exercises": [],
            },
            {
                "title": "RAG Architecture & LangChain",
                "content": """
# RAG Architecture & AI Agents

## Retrieval-Augmented Generation (RAG)
LLMs hallucinate and lack private data. RAG solves this by retrieving relevant documents from a Vector Database before generating an answer.

## The Core RAG Pipeline
### 1. Indexing Phase (Data Preparation)
- **Document Loading:** Ingesting data from sources like PDFs or databases.
- **Text Splitting (Chunking):** Breaking large documents into smaller pieces to fit the LLM's context window.
- **Embedding:** Converting chunks into numerical vectors (embeddings).
- **Storage:** Saving embeddings in a vector database (e.g., Pinecone, ChromaDB).

### 2. Retrieval & Generation Phase
- **Retrieval:** The system converts the user query into an embedding and performs a similarity search.
- **Augmentation:** Retrieved chunks and the original query are combined into a prompt.
- **Generation:** The LLM generates a grounded response.

## AI Agents
Moving beyond standard RAG, **Agentic RAG** uses agents that decide *if* and *when* to retrieve information. They can use tools (search, calculators, APIs) to solve complex, multi-step problems autonomously.

**Real-world Scenario:**
A global bank builds an internal AI Assistant for their HR department. Since LLMs don't know the bank's specific leave policies, an AI Developer builds a RAG system using LangChain and a Vector DB. When an employee asks "How many days of paternity leave do I get in the UK?", the Agent retrieves the exact UK HR policy PDF chunk and generates a cited, accurate answer.
                """,
                "exercises": [],
            },
        ],
    },
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
