expenses = [
    {"amount": 1200, "desc": "Bus fare", "category": "transport"},
    {"amount": 2500, "desc": "Groceries", "category": "food"},
    {"amount": 800, "desc": "Phone credit", "category": "utilities"},
    {"amount": 1500, "desc": "Taxi", "category": "transport"},
]


def add_expense():
    # Safely read amount
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Read description
    while True:
        desc = input("Enter description: ").strip()

        if not desc:
            print("Description cannot be empty.")
            continue

        break

    # Read category
    while True:
        category = input("Enter category: ").strip().lower()

        if not category:
            print("Category cannot be empty.")
            continue

        break

    expense = {
        "amount": amount,
        "desc": desc,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")


def list_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['desc']} | "
            f"{expense['category']} | "
            f"KSh {expense['amount']:.2f}"
        )


def filter_by_category():
    category = input("Enter category to filter: ").strip().lower()

    matches = [
        expense
        for expense in expenses
        if expense["category"] == category
    ]

    if not matches:
        print(f"No expenses found in the '{category}' category.")
        return

    print(f"\n--- {category.title()} Expenses ---")

    for i, expense in enumerate(matches, start=1):
        print(
            f"{i}. {expense['desc']} | "
            f"KSh {expense['amount']:.2f}"
        )


def show_summary():
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(expense["amount"] for expense in expenses)
    count = len(expenses)
    average = total / count
    largest = max(expenses, key=lambda expense: expense["amount"])

    print("\n--- Expense Summary ---")
    print(f"Total spent: KSh {total:.2f}")
    print(f"Number of expenses: {count}")
    print(f"Average expense: KSh {average:.2f}")
    print(
        f"Largest expense: {largest['desc']} "
        f"(KSh {largest['amount']:.2f})"
    )

    # Per-category totals
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + expense["amount"]
        )

    print("\nPer-category totals:")

    for category, amount in category_totals.items():
        print(f"- {category.title()}: KSh {amount:.2f}")


# Main menu loop
while True:
    print("\n===== SpendWise =====")
    print("1. Add expense")
    print("2. List all")
    print("3. Filter by category")
    print("4. Summary")
    print("5. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        list_expenses()

    elif choice == "3":
        filter_by_category()

    elif choice == "4":
        show_summary()

    elif choice == "5":
        print("Goodbye! Thanks for using SpendWise.")
        break

    else:
        print("Invalid option. Please choose 1–5.")
