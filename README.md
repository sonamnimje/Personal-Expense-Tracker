# Personal Expense Tracker

A modern web application built with Flask to help users track their personal expenses efficiently. The application features a beautiful UI with animated gradients and provides a seamless experience for managing daily expenses.

## 🌟 Features

### Core Functionality
- Add new expenses with detailed information
  - Description
  - Amount (in Indian Rupees - ₹)
  - Category
  - Automatic date tracking
- View all expenses in a clean, organized table
- Delete unwanted expenses
- Real-time total expense calculation
- Responsive design for all devices

### Categories
- Food
- Transportation
- Entertainment
- Bills
- Shopping
- Other

### Technical Features
- Modern UI with animated gradient background
- Responsive design using Bootstrap 5
- Real-time data updates
- Flash messages for user feedback
- Confirmation dialogs for deletions
- SQLite database for data persistence

## 🛠️ Technology Stack

- **Backend Framework:** Flask 3.0.2
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:**
  - HTML5
  - CSS3 (Custom animations and gradients)
  - Bootstrap 5.3.0
- **Additional Libraries:**
  - Flask-SQLAlchemy 3.1.1
  - Flask-Login 0.6.3
  - python-dotenv 1.0.1
  - Werkzeug 3.0.1

## 📋 Prerequisites

Before running the application, ensure you have:
- Python 3.8 or higher installed
- pip (Python package installer)
- A modern web browser

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Create and activate virtual environment**
   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
expense-tracker/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── static/
│   └── style.css      # Custom CSS styles
├── templates/
│   └── index.html     # Main template file
└── expenses.db        # SQLite database (created automatically)
```

## 💻 Usage Guide

1. **Adding an Expense**
   - Fill in the expense description
   - Enter the amount in Indian Rupees
   - Select a category from the dropdown
   - Click "Add Expense"

2. **Viewing Expenses**
   - All expenses are displayed in the table
   - Sorted by date (newest first)
   - Total amount shown at the top

3. **Deleting an Expense**
   - Click the "Delete" button next to the expense
   - Confirm the deletion in the popup dialog

## 🔒 Security Features

- Form validation for all inputs
- SQL injection prevention through SQLAlchemy
- CSRF protection
- Secure password handling (if implemented)

## 🎨 UI/UX Features

- Animated gradient background
- Responsive card layout
- Interactive buttons with hover effects
- Clean and modern typography
- Consistent color scheme
- Mobile-friendly design

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Author

[Your Name]

## 🙏 Acknowledgments

- Flask documentation
- Bootstrap team
- SQLAlchemy documentation 