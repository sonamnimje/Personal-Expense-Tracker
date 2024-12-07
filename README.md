# Personal-Expense-Tracker
# Description:

ExpenseTracker is a user-friendly personal finance app designed to help individuals track and manage their expenses. With ExpenseTracker, you can easily record your daily expenses, categorize them, and set budgets to stay on top of your finances.

# Core Features:

1. Expense Tracking: Record your daily expenses with ease, including date, amount, category, and notes.
2. Categorization: Categorize your expenses into predefined categories (e.g., Food, Transportation, Entertainment) or create custom categories.
3. Budgeting: Set budgets for specific categories or overall expenses to stay within your means.
4. Reporting: Generate reports to visualize your spending habits, including pie charts, bar graphs, and detailed expense lists.
5. Alerts: Receive notifications when you go over budget or when a bill is due.
6. Data Import/Export: Import data from other apps or export data to spreadsheets for further analysis.
 # Technologies Used
Frontend-- HTML/CSS: Standard markup languages for building web pages.

Database--
1. MySQL: A popular open-source relational database management system.
2. MongoDB: A popular NoSQL database management system.

# Installation-
To run this project locally, follow these steps:

Step 1: Importing Required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Step 2: Initializing Session State
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

Step 3: Defining Functions
def add_expense(date, category, amount, description):
    new_expense = pd.DataFrame([[date, category, amount, description]], columns=st.session_state.expenses.columns)
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

def load_expenses():
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])
    if uploaded_file is not None:
        st.session_state.expenses = pd.read_csv(uploaded_file)

def save_expenses():
    st.session_state.expenses.to_csv('expenses.csv', index=False)
    st.success("Expenses saved successfully")

def visualize_expenses():
    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots()
        sns.barplot(data=st.session_state.expenses, x='Category', y="Amount", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No Expenses to Visualize!")

  Step 4: Building the Streamlit Interface
  st.title("DevDuniya Expense Tracker")

with st.sidebar:
    st.header('Add Expense')
    date = st.date_input("Date")
    category = st.selectbox('Category', ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other'])
    amount = st.number_input('Amount', min_value=0.0, format="%.2f")
    description = st.text_input('Description')
    if st.button('Add'):
        add_expense(date, category, amount, description)
        st.success("Expense Added!")
        
    st.header('File Operations')
    if st.button('Save Expenses'):
        save_expenses()
    if st.button('Load Expenses'):
        load_expenses()

st.header('Expenses')
st.write(st.session_state.expenses)

st.header('Visualization')
if st.button('Visualize Expenses'):
    visualize_expenses[test_data_csv.txt](https://github.com/user-attachments/files/18040389/test_data_csv.txt)
