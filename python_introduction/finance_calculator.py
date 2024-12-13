# Prompt the user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_interest_rate = 0.05  # 5% annual interest rate (as a decimal)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Display results in a human-readable format
print(f"Your monthly savings are ${monthly_savings}.")  # Format to display 2 decimal places
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")