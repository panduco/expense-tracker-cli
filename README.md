# 💰 Expense Tracker CLI

A powerful command-line tool to track, analyze, and visualize your personal finances. 
Built with Python, this tool uses CSV for data storage and Matplotlib for generating visual reports.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Track Expenses:** Add expenses with descriptions, amounts, and custom categories.
- **List View:** View all recorded expenses in a clean, formatted table.
- **Data Analysis:** Summarize spending by category or month.
- **Visualization:** Generate beautiful bar charts of your spending habits.
- **Portable Data:** Uses CSV format, so you can open your data in Excel or Google Sheets anytime.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/expense-tracker-cli.git
   cd expense-tracker-cli
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Adding an Expense
Add a description and amount. You can optionally specify a category.
```bash
python expense.py add "Groceries" 55.00 --category Food
python expense.py add "Movie Ticket" 15.00 --category Entertainment
python expense.py add "Rent" 1200 --category Bills
```

### Listing Expenses
View all entries in a formatted table with a running total.
```bash
python expense.py list
```

### Summarizing Expenses
View totals filtered by category or month.

**Total Summary:**
```bash
python expense.py summary
```

**Filter by Category:**
```bash
python expense.py summary --category Food
```

**Filter by Month (1-12):**
```bash
python expense.py summary --month 10
```

### Visualizing Expenses
Generate a bar chart image (`expenses_chart.png`) showing spending per category.
```bash
python expense.py plot
```
*(A file named `expenses_chart.png` will be saved in your project folder).*

## 📊 Screenshots

**Listing Expenses:**
```text
--- Your Expenses ---
Date         Description          Category       Amount
-------------------------------------------------------
2023-10-27   Groceries            Food          $   55.00
2023-10-27   Rent                 Bills         $ 1200.00
-------------------------------------------------------
Total Spent: $1255.00
```

**Visualization:**
*(Tip: Take a screenshot of the generated `expenses_chart.png` and paste it here!)*

## 📂 Project Structure

```
expense-tracker-cli/
├── expense.py          # Main application logic
├── expenses.csv        # Local database (auto-generated)
├── expenses_chart.png  # Generated chart
├── requirements.txt    # Dependencies (matplotlib)
└── README.md
```

## 📜 License

This project is licensed under the MIT License.