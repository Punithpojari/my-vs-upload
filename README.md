# 🤖 DecodeLabsPPRobot

DecodeLabsPPRobot is a simple AI-inspired command-line chatbot developed in Python. It interacts with users by recognizing predefined keywords and responding with relevant information using a keyword-matching approach. The chatbot also simulates human-like conversation with a typing effect and timestamps for responses.

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

---

## 📄 License

This project is created for educational and learning purposes.
