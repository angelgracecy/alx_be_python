monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

interest_rate = 0.05
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

print(f"Your monthly savings: ${monthly_savings:.2f}")
print(f"Your projected annual savings (including interest): ${projected_annual_savings:.2f}")
