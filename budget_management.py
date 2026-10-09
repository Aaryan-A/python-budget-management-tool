import tkinter as tk
from tkinter import messagebox

# Function to calculate the total of all expenses
def calculate_total_expenses(expenses_amounts):
    return sum(expenses_amounts)

# Function to calculate the remaining budget after expenses
def calculate_remaining_budget(income, total_expenses):
    return income - total_expenses

# Function to add a new expense to the list
def add_expense():
    name = expense_name_entry.get().strip()
    amount = expense_amount_entry.get().strip()

    if name and amount:
        try:
            amount = float(amount)

            if amount < 0:
                messagebox.showerror(
                    "Invalid Input", "Expense amount cannot be negative."
                )
                return

            expenses_names.append(name)
            expenses_amounts.append(amount)
            expenses_list.insert(tk.END, f"{name}: ${amount:.2f}")

            expense_name_entry.delete(0, tk.END)
            expense_amount_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror(
                "Invalid Input", "Expense amount must be a number."
            )
    else:
        messagebox.showerror(
            "Missing Input",
            "Please provide both name and amount for the expense."
        )

# Function to calculate and display the results
def calculate_results():
    try:
        income = float(income_entry.get().strip())

        if income < 0:
            messagebox.showerror(
                "Invalid Input", "Income cannot be negative."
            )
            return

        total_expenses = calculate_total_expenses(expenses_amounts)
        remaining_budget = calculate_remaining_budget(
            income, total_expenses
        )

        results_label.config(
            text=f"Income: ${income:.2f}\n"
                 f"Total Expenses: ${total_expenses:.2f}\n"
                 f"Remaining Budget: ${remaining_budget:.2f}"
        )

        if savings_goal_entry.get().strip():
            try:
                savings_goal = float(savings_goal_entry.get().strip())

                if savings_goal < 0:
                    messagebox.showerror(
                        "Invalid Input",
                        "Savings goal cannot be negative."
                    )
                    return

                remaining_after_savings = calculate_remaining_budget(
                    remaining_budget, savings_goal
                )

                savings_label.config(
                    text=f"Remaining after Savings Goal: "
                         f"${remaining_after_savings:.2f}"
                )

            except ValueError:
                messagebox.showerror(
                    "Invalid Input", "Savings goal must be a number."
                )
        else:
            savings_label.config(text="")

    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Income must be a number."
        )

root = tk.Tk()
root.title("Budget Management Tool")

# Create input for yearly income
tk.Label(root, text="Yearly Income:").grid(
    row=0, column=0, padx=10, pady=5, sticky="w"
)
income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1, padx=10, pady=5)

# Create input for expense name
tk.Label(root, text="Expense Name:").grid(
    row=1, column=0, padx=10, pady=5, sticky="w"
)
expense_name_entry = tk.Entry(root)
expense_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Create input for expense amount
tk.Label(root, text="Expense Amount:").grid(
    row=2, column=0, padx=10, pady=5, sticky="w"
)
expense_amount_entry = tk.Entry(root)
expense_amount_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to add expenses
add_expense_button = tk.Button(
    root, text="Add Expense", command=add_expense
)
add_expense_button.grid(
    row=3, column=0, columnspan=2, pady=10
)

# Listbox to display all expenses
expenses_list = tk.Listbox(root, width=40, height=10)
expenses_list.grid(
    row=4, column=0, columnspan=2, padx=10, pady=5
)

# Input for savings goal
tk.Label(root, text="Savings Goal:").grid(
    row=5, column=0, padx=10, pady=5, sticky="w"
)
savings_goal_entry = tk.Entry(root)
savings_goal_entry.grid(row=5, column=1, padx=10, pady=5)

# Label to display results
results_label = tk.Label(root, text="", justify="left")
results_label.grid(
    row=6, column=0, columnspan=2, padx=10, pady=5
)

# Label to display savings goal results
savings_label = tk.Label(root, text="", justify="left")
savings_label.grid(
    row=7, column=0, columnspan=2, padx=10, pady=5
)

# Button to calculate results
calculate_button = tk.Button(
    root, text="Calculate", command=calculate_results
)
calculate_button.grid(
    row=8, column=0, columnspan=2, pady=10
)

# Initialize empty lists for expenses
expenses_names = []
expenses_amounts = []

root.mainloop()
