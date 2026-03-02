import argparse
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILENAME = "expenses.csv"

def init_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Description", "Category", "Amount"])
            
def add_expense(description, amount, category):
    """Add a new expense to the CSV file."""
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILENAME, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, description, category, amount])
    
    print(f"✅ Added: {description} (${amount}) - {category}")

def list_expenses():
    """Read and display all expenses."""
    if not os.path.exists(FILENAME):
        print("No expenses found. Add one first!")
        return

    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header row
        
        print("\n--- Your Expenses ---")
        print(f"{'Date':<12} {'Description':<20} {'Category':<10} {'Amount':>10}")
        print("-" * 55)
        
        total = 0.0
        for row in reader:
            # row = [Date, Description, Category, Amount]
            date, desc, cat, amt = row
            amount = float(amt)
            total += amount
            print(f"{date:<12} {desc:<20} {cat:<10} ${amount:>9.2f}")
            
        print("-" * 55)
        print(f"Total Spent: ${total:.2f}\n")

def summary_expenses(category=None, month=None):
    """Calculate total expenses, with optional filters."""
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return

    total = 0.0
    count = 0
    
    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        
        for row in reader:
            # row = [Date, Description, Category, Amount]
            row_date, row_desc, row_cat, row_amt = row
            amount = float(row_amt)
            
            # --- FILTERING LOGIC ---
            match = True
            
            # Filter by Category (case-insensitive)
            if category and row_cat.lower() != category.lower():
                match = False
            
            # Filter by Month
            if month:
                # Extract month from the date string (YYYY-MM-DD)
                try:
                    row_month = int(row_date.split('-')[1])
                    if row_month != month:
                        match = False
                except:
                    pass # Skip rows with bad dates

            # --- ACCUMULATE ---
            if match:
                total += amount
                count += 1

    # --- DISPLAY ---
    print("\n--- Expense Summary ---")
    if category:
        print(f"Category Filter: {category.capitalize()}")
    if month:
        print(f"Month Filter: {month}")
    
    print(f"Transactions found: {count}")
    print(f"Total Spent: ${total:.2f}")
    print("-----------------------\n")

def plot_expenses():
    """Generate a bar chart of expenses by category."""
    if not os.path.exists(FILENAME):
        print("No expenses to plot.")
        return

    # Dictionary to hold totals per category
    category_totals = {}

    with open(FILENAME, mode='r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        
        for row in reader:
            # row = [Date, Description, Category, Amount]
            if len(row) < 4: continue # Safety check
            
            category = row[2]
            amount = float(row[3])
            
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if not category_totals:
        print("No data to plot.")
        return

    # --- PLOTTING ---
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue', edgecolor='black')
    
    plt.title("Total Expenses by Category", fontsize=16)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Amount ($)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of bars
    for i, v in enumerate(amounts):
        plt.text(i, v + 0.5, f"${v:.2f}", ha='center', fontweight='bold')

    # Save the file
    output_file = "expenses_chart.png"
    plt.savefig(output_file)
    plt.close() # Close the plot to free memory
    
    print(f"📊 Chart saved as '{output_file}'")

def main():
    init_file()
    
    parser = argparse.ArgumentParser(description="Track your expenses")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ADD Command
    parser_add = subparsers.add_parser("add", help="Add an expense")
    parser_add.add_argument("description", type=str, help="What did you buy?")
    parser_add.add_argument("amount", type=float, help="How much did it cost?")
    parser_add.add_argument("--category", type=str, default="General", help="Category (e.g., Food, Transport)")

    # LIST Command
    subparsers.add_parser("list", help="List all expenses")

    # SUMMARY Command
    parser_summary = subparsers.add_parser("summary", help="View summary of expenses")
    parser_summary.add_argument("--category", type=str, help="Filter by category")
    parser_summary.add_argument("--month", type=int, help="Filter by month (1-12)")
    
    # PLOT Command
    subparsers.add_parser("plot", help="Generate a bar chart of expenses")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summary_expenses(args.category, args.month)
    elif args.command == "plot":
        plot_expenses()
        
if __name__ == "__main__":
    main()