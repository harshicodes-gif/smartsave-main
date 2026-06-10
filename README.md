# 💰 SmartSave

SmartSave is a student-focused personal finance application that helps students manage their pocket money effectively. The platform enables users to track expenses, monitor spending habits, develop savings discipline, and make smarter financial decisions through analytics, predictions, and AI-powered financial guidance.

Developed independently by **Harshita**.

---

## 📖 Overview

Managing pocket money can be challenging for students, especially when balancing daily expenses, entertainment, transportation, and savings goals. Many students lack a simple and engaging tool to understand where their money goes and how they can improve their spending habits.

SmartSave addresses this problem by providing a centralized platform where students can:

- Record and categorize expenses
- Track spending patterns
- Monitor savings progress
- Receive financial recommendations
- Visualize spending behavior
- Build healthy money management habits

---

## 🎯 Problem Statement

Students often receive fixed pocket money but struggle to:

- Track daily spending
- Identify unnecessary expenses
- Maintain a monthly budget
- Develop consistent saving habits
- Understand spending trends

SmartSave provides an intuitive and engaging solution that helps students become financially aware and responsible.

---

## 🚀 Features

### 💵 Expense Tracking
- Add and manage daily expenses
- Store transaction history
- Categorize spending activities
- Track overall expenditure

### 📊 Analytics Dashboard
- View spending summaries
- Analyze expense categories
- Monitor financial trends
- Understand spending behavior through visualizations

### 🤖 AI Savings Coach
- Personalized saving recommendations
- Financial awareness tips
- Spending improvement suggestions
- Smart budgeting guidance

### 🎮 Savings Gamification
- Savings levels and achievements
- Reward-based engagement
- Encourages consistent saving habits
- Interactive financial learning experience

### 🔮 Expense Prediction
- Estimate future spending patterns
- Forecast month-end balance
- Improve budget planning

### 🧾 OCR-Based Receipt Processing (Planned Enhancement)
- Scan receipts
- Extract spending information automatically
- Reduce manual data entry

### 🏷️ Smart Categorization
- Automatically categorize expenses
- Improve spending analysis
- Simplify transaction management

---

## 🏗️ System Architecture

```text
SMARTSAVE
│
├── backend
│   ├── database
│   │   └── db.py
│   │
│   ├── models
│   │   ├── transactions.py
│   │   └── user.py
│   │
│   └── services
│       ├── ai_coach_service.py
│       ├── budget_service.py
│       ├── categorizer_service.py
│       ├── gamification_service.py
│       ├── ocr_service.py
│       ├── parser_service.py
│       └── prediction_service.py
│
├── frontend
│   ├── components
│   │   ├── cards.py
│   │   └── charts.py
│   │
│   ├── pages
│   │   ├── dashboard.py
│   │   ├── analytics.py
│   │   ├── ai_coach.py
│   │   └── savings_game.py
│   │
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technology Stack

| Layer | Technology |
|---------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite |
| Data Processing | Pandas |
| Visualization | Plotly |
| Version Control | Git & GitLab |
| Future AI Integration | OpenAI / Local AI Models |

---

## 📦 Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to Project Directory

```bash
cd SMARTSAVE
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Launch the Streamlit application:

```bash
streamlit run frontend/app.py
```

The application will start locally and open in your default web browser.

---

## 📈 Application Workflow

1. User enters expense information.
2. Expense is stored in the database.
3. SmartSave categorizes spending.
4. Dashboard updates analytics.
5. AI Coach generates recommendations.
6. Prediction engine forecasts future spending.
7. Gamification module rewards saving behavior.

---

## 🎯 Target Users

- School students
- College students
- Young adults managing pocket money
- First-time budget planners
- Students learning financial literacy

---

## 🌟 Future Enhancements

### Version 2.0 Roadmap

- Receipt OCR using computer vision
- AI-powered financial chatbot
- Goal-based savings tracker
- Budget alerts and notifications
- Monthly financial reports
- Student leaderboards
- Mobile application
- Cloud database support
- Multi-user authentication
- Bank statement integration

---

## 📚 Key Learning Outcomes

This project demonstrates practical experience in:

- Full-stack Python development
- Streamlit application development
- SQLite database management
- Software architecture design
- Modular programming principles
- Financial analytics implementation
- Data visualization techniques
- AI-assisted recommendation systems

---

## 🔒 Security Considerations

- Local SQLite storage
- Modular backend architecture
- Separation of frontend and backend responsibilities
- Easily extendable authentication layer for future releases

---

## 👨‍💻 Developer

### Harshita

SmartSave was independently designed and developed as a personal project focused on improving financial literacy and money management among students.

Responsibilities included:

- System architecture design
- Frontend development
- Backend development
- Database implementation
- Analytics design
- AI module integration planning
- Testing and deployment

---

## 📄 License

This project is intended for educational, academic, and demonstration purposes.

---

## 💡 Vision

SmartSave aims to make financial literacy accessible to every student by transforming pocket money management into an engaging, data-driven, and rewarding experience.
