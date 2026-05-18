import streamlit as st
import time

def show_interview_prep(user):
    """Show Interview Preparation Page"""
    st.markdown(
        """
    <div class='card-header'>
        <h1 style='color: white; margin: 0;'>👔 Interview Preparation</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 0.5rem;'>Master the technical interviews for AI & ML Engineering roles</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    
    st.markdown("")

    tabs = st.tabs(["📝 Technical Questions", "💻 Coding Tests", "🎙️ Mock Interview"])
    
    # -------------------------------------------------------------
    # TAB 1: TECHNICAL QUESTIONS
    # -------------------------------------------------------------
    with tabs[0]:
        st.markdown("<h2>Common AI/ML Interview Questions</h2>", unsafe_allow_html=True)
        st.write("Click on the questions to reveal the answers.")
        
        qa_bank = {
            "Machine Learning Basics": [
                {
                    "q": "What is the bias-variance tradeoff?",
                    "a": "**Bias** is the error introduced by approximating a real-world problem too simplistically (Underfitting). **Variance** is the error introduced by making the model too complex, causing it to fit the noise in the training data (Overfitting). The tradeoff involves finding the sweet spot where both are minimized."
                },
                {
                    "q": "How does Random Forest work?",
                    "a": "Random Forest is an ensemble learning method that constructs a multitude of decision trees at training time. It uses 'Bagging' (Bootstrap Aggregating) by training each tree on a random subset of data and features. The final prediction is made by averaging the predictions (regression) or taking a majority vote (classification) across all trees."
                },
                {
                    "q": "Explain Precision vs. Recall. When would you prioritize Recall?",
                    "a": "**Precision** is True Positives / (True Positives + False Positives) - 'Out of all predicted positives, how many were actual positives?'.\n**Recall** is True Positives / (True Positives + False Negatives) - 'Out of all actual positives, how many did we find?'.\nYou prioritize Recall when False Negatives are highly dangerous (e.g., Cancer detection, Fraud detection)."
                }
            ],
            "Deep Learning & NLP": [
                {
                    "q": "What is the vanishing gradient problem and how do LSTMs/ResNets solve it?",
                    "a": "During backpropagation in deep networks, gradients are multiplied. If the gradients are < 1, multiplying them repeatedly causes them to 'vanish' to 0, stopping earlier layers from learning. **LSTMs** solve this using cell states and gates that allow gradients to flow unchanged. **ResNets** solve this using skip-connections (adding the input to the output of a layer block)."
                },
                {
                    "q": "Explain the Self-Attention mechanism in Transformers.",
                    "a": "Self-attention allows the model to look at other words in the input sequence to better understand the context of the current word. It computes a Query, Key, and Value for each word. The dot product of a word's Query with all other Keys determines the 'attention score', dictating how much focus to put on the corresponding Values."
                }
            ],
            "MLOps & Deployment": [
                {
                    "q": "How would you deploy an ML model to handle variable traffic spikes?",
                    "a": "I would containerize the model using **Docker** and expose it via a high-performance ASGI server like **FastAPI**. I would then deploy the container to **Kubernetes (K8s)** and configure a Horizontal Pod Autoscaler (HPA) to automatically spin up more pods based on CPU/Memory usage or custom metrics like concurrent requests."
                }
            ]
        }
        
        for category, qas in qa_bank.items():
            st.markdown(f"### {category}")
            for item in qas:
                with st.expander(f"❓ {item['q']}"):
                    st.markdown(item["a"])
            st.markdown("<br>", unsafe_allow_html=True)
            
    # -------------------------------------------------------------
    # TAB 2: CODING TESTS
    # -------------------------------------------------------------
    with tabs[1]:
        st.markdown("<h2>AI Engineer Coding Challenges</h2>", unsafe_allow_html=True)
        st.write("Write the code for the following scenarios commonly asked in live coding rounds.")
        
        coding_tests = [
            {
                "title": "1. Implement Batching for an API",
                "desc": "Write a Python class `BatchProcessor` that accepts items and processes them in batches of a given size `batch_size`. If the batch size is not reached within `timeout` seconds, process whatever is in the batch.",
                "solution": '''import time\nimport threading\n\nclass BatchProcessor:\n    def __init__(self, batch_size, timeout, process_func):\n        self.batch_size = batch_size\n        self.timeout = timeout\n        self.process_func = process_func\n        self.batch = []\n        self.lock = threading.Lock()\n        self.timer = None\n\n    def add_item(self, item):\n        with self.lock:\n            self.batch.append(item)\n            if len(self.batch) == 1:\n                self.timer = threading.Timer(self.timeout, self._flush)\n                self.timer.start()\n            \n            if len(self.batch) >= self.batch_size:\n                if self.timer:\n                    self.timer.cancel()\n                self._flush()\n\n    def _flush(self):\n        with self.lock:\n            if not self.batch:\n                return\n            items_to_process = self.batch[:]\n            self.batch.clear()\n        \n        self.process_func(items_to_process)'''
            },
            {
                "title": "2. Calculate Moving Average",
                "desc": "Given an array of floats and a window size `k`, write an optimized function to calculate the moving average. Do not use external libraries like NumPy.",
                "solution": '''def moving_average(arr, k):\n    if not arr or k <= 0 or k > len(arr):\n        return []\n    \n    result = []\n    window_sum = sum(arr[:k])\n    result.append(window_sum / k)\n    \n    for i in range(len(arr) - k):\n        window_sum = window_sum - arr[i] + arr[i + k]\n        result.append(window_sum / k)\n        \n    return result'''
            },
            {
                "title": "3. Softmax Function from Scratch",
                "desc": "Implement the Softmax activation function mathematically in pure Python. Ensure numerical stability (prevent overflow).",
                "solution": '''import math\n\ndef softmax(logits):\n    # Subtract max for numerical stability\n    max_logit = max(logits)\n    exp_values = [math.exp(x - max_logit) for x in logits]\n    sum_exp = sum(exp_values)\n    \n    return [ex / sum_exp for ex in exp_values]'''
            }
        ]
        
        for test in coding_tests:
            st.markdown(f"### {test['title']}")
            st.markdown(f"**Problem:** {test['desc']}")
            
            user_code = st.text_area("Your Solution:", height=150, key=f"code_{test['title']}")
            
            if st.button("Reveal Official Solution", key=f"btn_{test['title']}"):
                st.code(test['solution'], language='python')
            
            st.divider()

    # -------------------------------------------------------------
    # TAB 3: MOCK INTERVIEW
    # -------------------------------------------------------------
    with tabs[2]:
        st.markdown("<h2>🎙️ Interactive Mock Interview Simulator</h2>", unsafe_allow_html=True)
        st.write("Simulate a behavioral and technical interview round. The AI Hiring Manager will ask you a question. Type your response below.")
        
        if "mock_interview_started" not in st.session_state:
            st.session_state.mock_interview_started = False
            st.session_state.mock_q_idx = 0
            st.session_state.mock_history = []
            
        mock_questions = [
            "Tell me about a time you had to optimize a machine learning model that was running too slowly in production.",
            "How would you explain the concept of embeddings to a non-technical stakeholder?",
            "What metrics would you use to evaluate a recommendation system, and why?",
            "Can you describe your experience with CI/CD pipelines in an AI context?"
        ]
        
        if not st.session_state.mock_interview_started:
            if st.button("▶️ Start Mock Interview", use_container_width=True):
                st.session_state.mock_interview_started = True
                st.rerun()
        else:
            # Display chat history
            for msg in st.session_state.mock_history:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
            
            # Show current question if we haven't reached the end
            if st.session_state.mock_q_idx < len(mock_questions):
                current_q = mock_questions[st.session_state.mock_q_idx]
                
                # If the AI hasn't asked the question yet in the history, display it
                if not st.session_state.mock_history or st.session_state.mock_history[-1]["role"] == "user":
                    with st.chat_message("assistant"):
                        st.markdown(f"**Interviewer:** {current_q}")
                        
                # Input for user
                user_answer = st.chat_input("Type your answer here...")
                if user_answer:
                    # Save AI question to history
                    st.session_state.mock_history.append({"role": "assistant", "content": f"**Interviewer:** {current_q}"})
                    # Save user answer to history
                    st.session_state.mock_history.append({"role": "user", "content": user_answer})
                    
                    # Generate simulated feedback
                    with st.spinner("Interviewer is evaluating your answer..."):
                        time.sleep(1.5) # Simulate thinking
                        feedback = "That's a very solid approach. I like how you focused on the core problem. Let's move to the next question."
                        st.session_state.mock_history.append({"role": "assistant", "content": f"**Feedback:** {feedback}"})
                    
                    st.session_state.mock_q_idx += 1
                    st.rerun()
                    
            else:
                st.success("🎉 You have completed the mock interview!")
                if st.button("Restart Interview"):
                    st.session_state.mock_interview_started = False
                    st.session_state.mock_q_idx = 0
                    st.session_state.mock_history = []
                    st.rerun()
