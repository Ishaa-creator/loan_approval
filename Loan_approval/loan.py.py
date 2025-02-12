import pandas as pd

# Load the previous dataset
df = pd.read_csv('loan_data.csv')

# EMI Calculation
def calculate_emi(loan_amount, interest_rate, loan_term_years):
    monthly_rate = (interest_rate / 100) / 12  # Convert annual rate to monthly
    loan_term_months = loan_term_years * 12
    emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** loan_term_months) / ((1 + monthly_rate) ** loan_term_months - 1)
    return emi, loan_term_months

# FOIR Calculation
def calculate_foir(emi, monthly_income):
    return emi / monthly_income

# Probabilities (Pre-calculated based on previous dataset)
prob_approved = df['loan_status'].value_counts(normalize=True).get('Approved', 0)
prob_rejected = df['loan_status'].value_counts(normalize=True).get('Rejected', 0)

# CIBIL and Employment Probabilities
prob_cibil_high = (df['cibil_score'] > 500).mean()
prob_self_employed = (df['self_employed'] == 'Yes').mean()

# Industry default rate
default_rate = 0.20  # 20% default rate

# Parameters for decision making
foir_threshold = 0.5
minimum_cibil_score = 600

# Variables to store consolidated results
consolidated_potential_gain = 0
consolidated_potential_loss = 0
total_loan_amount = 0
approved_loans = 0

# Function to handle each loan decision
def process_loan_application(cibil_score, self_employed, monthly_income, loan_amount, interest_rate, loan_term):
    emi, loan_term_months = calculate_emi(loan_amount, interest_rate, loan_term)
    foir = calculate_foir(emi, monthly_income)

    # Decision-making based on FOIR, CIBIL score, and self-employment status
    if foir <= foir_threshold and cibil_score >= minimum_cibil_score:
        loan_decision = "Approved"
        potential_gain = emi * loan_term_months  # Total EMI payments (loan + interest)
        potential_loss = 0
    else:
        loan_decision = "Rejected"
        potential_gain = 0
        potential_loss = loan_amount  # Loss is the full loan amount if rejected

    return loan_decision, emi, potential_gain, potential_loss

# Loop for 5 loan entries
for i in range(5):
    print(f"\nEnter details for Loan {i + 1}:")
    cibil_score = int(input("Enter your CIBIL score: "))
    self_employed = input("Are you self-employed? (Yes/No): ").strip().lower()
    monthly_income = float(input("Enter your monthly income (in your local currency): "))
    loan_amount = float(input("Enter the loan amount you're applying for (in your local currency): "))
    interest_rate = float(input("Enter the interest rate (percentage): "))
    loan_term = int(input("Enter loan term (in years): "))

    # Process the loan application
    loan_decision, emi, potential_gain, potential_loss = process_loan_application(cibil_score, self_employed, monthly_income, loan_amount, interest_rate, loan_term)

    # Output the individual loan result (but no gain/loss per loan)
    print(f"\n--- Loan {i + 1} Result ---")
    print(f"Loan Decision: {loan_decision}")
    print(f"Your calculated EMI is: ₹{emi:.2f}")

    # Update the consolidated totals (only for approved loans)
   if loan_decision == "Approved":
        total_loan_amount += loan_amount
        consolidated_potential_gain += potential_gain
        approved_loans += 1
    else:
        consolidated_potential_loss += potential_loss

# Final loss adjustment for default rate (20%)
# Apply default rate only to the approved loans
adjusted_loss_due_to_defaults = consolidated_potential_loss + (consolidated_potential_gain * default_rate)

# Print consolidated result
print("\n--- Consolidated Results ---")
print(f"Total Loan Amount for Approved Loans: ₹{total_loan_amount:.2f}")
print(f"Total Potential Gain for Bank (with no defaults): ₹{consolidated_potential_gain:.2f}")
print(f"Total Potential Loss for Bank (due to defaults at 20%): ₹{adjusted_loss_due_to_defaults:.2f}")
print(f"(Note: A 20% default rate means 20 loans out of every 100 are expected to default.)")