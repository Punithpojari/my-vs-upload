# 🤖 DecodeLabsPPRobot

DecodeLabsPPRobot is a simple AI-inspired command-line chatbot developed in Python. It interacts with users by recognizing predefined keywords and responding with relevant information using a keyword-matching approach. The chatbot also simulates human-like conversation with a typing effect and timestamps for responses.

MY FIRST PROJECT 

## 📌 Features
- 👋 Greets users with personalized messages.
- 💬 Responds to common greetings.
- 📞 Provides contact information.
- 🧠 Explains its working logic.
- 🙏 Responds to thank-you messages.
- ⌨️ Typing animation for realistic interaction.
- 🕒 Displays timestamps for every bot response.
- 🚪 Supports exit commands (`exit`, `bye`).
- ❌ Handles unknown queries gracefully.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Libraries Used:**
  - `time` – Creates typing animation.
  - `random` – Selects random responses.
  - `datetime` – Displays current date and time.
- **Concepts Used:**
  - Object-Oriented Programming (OOP)
  - Classes and Objects
  - Dictionaries
  - Lists
  - Loops
  - Conditional Statements
  - Functions
  - Exception Handling
  - String Manipulation
  - Keyword Matching Algorithm

## 📂 Project Structure

DecodeLabsPPRobot/
│
├── chatbot.py
└── README.md

---

## ⚙️ How It Works

1. The program asks the user to enter their name.
2. The chatbot welcomes the user.
3. The user enters a message.
4. The chatbot converts the input to lowercase.
5. It searches the knowledge base for matching keywords.
6. If a match is found, a random response is returned.
7. If no keyword matches, a default response is displayed.
8. The conversation continues until the user types `exit` or `bye`.

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/DecodeLabsPPRobot.git
```

Go to the project folder:

```bash
cd DecodeLabsPPRobot
```

Run the chatbot:

```bash
python chatbot.py
``

## 📸 Sample Output

```
Enter your name: Punith

[2026-07-22 10:30:12] BOT:
Hello Punith! I am DecodeLabsPPRobot. How can I assist you today?

Punith: hi

[2026-07-22 10:30:15] BOT:
Hello! How can I assist you today?

Punith: contact

[2026-07-22 10:30:20] BOT:
Phone : +1-234-567-8901
Email : decodelabs.tech@gmail.com
Location : Bangalore, Karnataka, India

Punith: bye

[2026-07-22 10:30:28] BOT:
Goodbye! Have a great day!
```

## 📚 Skills Demonstrated

- Python Programming
- Object-Oriented Programming
- Data Structures (Dictionary & List)
- User Input Handling
- Exception Handling
- Console Application Development
- Keyword-Based Chatbot Logic
- Randomized Responses
- Real-Time Output Formatting

## 🔮 Future Improvements

- NLP integration using NLTK or spaCy
- Voice input and speech output
- GUI using Tkinter or PyQt
- Database integration for storing conversations
- Machine Learning-based intent recognition
- Web deployment using Flask or Django
- Support for multiple languages
- API integration for real-time information

---

## 👨‍💻 Author

**Punith C**

Python Developer | AI Enthusiast | Computer Science Student

MY SECOND PROJECT

# Data Classification Using AI

A simple AI classification project implemented in **pure Python** without using external libraries. This project demonstrates the basic concepts of supervised machine learning using the **1-Nearest Neighbor (1-NN)** classification algorithm and Euclidean Distance.

## 📌 Project Overview

This project classifies data into different categories based on the nearest training sample. It is designed for beginners to understand how a basic AI classification model works without relying on machine learning frameworks such as Scikit-learn.

## 🚀 Features

- Pure Python implementation
- No external libraries used
- Uses Euclidean Distance for classification
- Splits dataset into training and testing data
- Predicts class labels
- Calculates classification accuracy
- Beginner-friendly code with comments

## 🛠 Technologies Used

- Python 3
- Built-in `math` module

## 📂 Project Structure

```
Data-Classification-Using-AI/
│── dat.py
│── README.md
```

## ⚙️ Algorithm

The project uses the **1-Nearest Neighbor (1-NN)** algorithm.

Steps:
1. Store the dataset.
2. Split the dataset into training and testing sets.
3. Calculate Euclidean distance.
4. Find the nearest training sample.
5. Predict the class label.
6. Compare the prediction with the actual class.
7. Calculate the overall accuracy.

## 📊 Sample Output

```
=========================================
DATA CLASSIFICATION USING AI
=========================================

Total Samples: 10
Training Samples: 6
Testing Samples: 4

Prediction Results

Input: 5.1 3.5 | Actual: A | Predicted: A
Input: 5.4 3.9 | Actual: A | Predicted: A
Input: 6.8 3.2 | Actual: B | Predicted: B
Input: 6.4 3.2 | Actual: B | Predicted: B

Correct Predictions: 4
Total Test Samples: 4
Accuracy: 100.0%
```

## ▶️ How to Run

1. Clone the repository.

```
git clone https://github.com/your-username/Data-Classification-Using-AI.git
```

2. Navigate to the project folder.

```
cd Data-Classification-Using-AI
```

3. Run the program.

```
python dat.py
```

## 🎯 Learning Outcomes

- Supervised Learning basics
- Data classification
- Euclidean Distance
- Nearest Neighbor algorithm
- Python programming fundamentals
- Model evaluation

## 📚 Future Improvements

- Support larger datasets
- Implement K-Nearest Neighbors (KNN)
- Read data from CSV files
- Improve dataset splitting
- Add graphical visualization

## 👨‍💻 Author

**Punith C**

Computer Science Engineering Student

