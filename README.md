Overview:
The app allows users to:

Record expenses (amount, category, description, date).
View and manage expenses.
Analyze spending patterns (e.g., summaries, graphs, and reports).
Set budgets to monitor financial goals.

Development Plan:

1. Core Features
Add Expenses: Input expense details (amount, category, description, date).
View Expenses: Display a list of recorded expenses, categorized and sortable.
Delete/Edit Expenses: Modify or remove incorrect entries.
Expense History: Keep all records saved persistently.
2. Additional Features
Budget Tracking: Set monthly limits and warn users of overspending.
Analytics: Graphs showing expenses by category or time (using matplotlib or plotly).
Recurring Expenses: Automate regular entries (e.g., rent, subscriptions).
Export Data: Save reports as CSV, JSON, or PDF for offline analysis.

Tech Stack:
Backend (Core Logic)-
Python: For managing data, file operations, and core business logic.
JSON or SQLite: For persistent data storage.
Frontend-
CLI-based (basic): Command-line interaction for quick use.
GUI-based (advanced): Use Python libraries like:
Tkinter: Simple built-in GUI framework.
PyQt or Kivy: For more advanced UI/UX.
