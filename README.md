# Python Budget Management Tool

A Python application that helps users track expenses, calculate their remaining budget, and plan savings goals through a graphical user interface (GUI) built with Tkinter.

## Features

- **Expense Tracking:** Add expenses with a name and amount.
- **Expense Removal:** Select an expense from the list and remove it using the **Remove Expense** button.
- **Total Expenses:** Calculates the sum of all recorded expenses.
- **Budget Calculation:** Calculates the remaining budget after expenses are deducted from yearly income.
- **Savings Goal Planning:** Estimates the money remaining after setting a savings goal.
- **Input Validation:** Displays error messages for missing or invalid inputs and prevents negative income, expenses, and savings goals.
- **Graphical User Interface:** Provides input fields, buttons, and a selectable list of expenses using Tkinter.
- **Expense Management:** Keeps the expense names and amounts synchronized when expenses are added or removed.

## Technologies Used

- Python
- Tkinter
- Lists and Functions
- Conditional Statements
- Exception Handling
- Graphical User Interface (GUI) Development

## How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the folder containing `budget_management.py`.
4. Run the application:

   ```bash
   python budget_management.py
   ```

   On Windows, you can also use:

   ```powershell
   py budget_management.py
   ```

5. Enter your yearly income.
6. Add expenses by entering an expense name and amount, then clicking **Add Expense**.
7. To remove an expense, select it from the expense list and click **Remove Expense**.
8. Optionally, enter a savings goal.
9. Click **Calculate** to view your income, total expenses, remaining budget, and remaining budget after the savings goal.

## Requirements

- Python 3
- Tkinter (typically included with standard Python installations)
- A desktop environment that supports graphical applications

**Note:** This application requires a graphical desktop environment to display its Tkinter interface. Standard Google Colab sessions and headless cloud environments, such as GitHub Codespaces without a configured graphical display, do not normally support opening the GUI directly.

## Author

Aaryan Aggarwal
