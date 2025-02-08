# loan_approval
## Loan approval and Bank profitability using Bayesian Theorem 

In this project, we built a model to evaluate loan approval decisions and calculate potential gain and loss for a bank based on user input and pre-existing loan data. The project is structured around a few key components:

1. Loan Dataset: We used a dataset containing past loan information, which included features such as loan status (Approved/Rejected), CIBIL score, employment status (self-employed or not), monthly income, loan amount, interest rate, and loan term.

2. User Input: The program takes user input for:
   - CIBIL score
   - Employment status
   - Monthly income
   - Loan amount
   - Interest rate
   - Loan term (years)

3. Loan Approval Logic:
   - EMI (Equated Monthly Installment) Calculation: Based on the input loan amount, interest rate, and loan term, we calculate the monthly EMI using the standard loan EMI formula.
   
   - FOIR (Fixed Obligations to Income Ratio): FOIR is calculated as EMI divided by monthly income, and it's a key criterion for loan approval. A FOIR of 0.5 or less indicates that the borrower can repay the loan comfortably.

   - Approval Criteria: The loan is approved if:
     1. The FOIR is ≤ 0.5
     2. The CIBIL score is ≥ 600
     3. The user’s employment status and income support the repayment capability.

   - If any of these conditions are violated, the loan is rejected.

4. Bayesian Probability Calculation:
   Using Bayes' Theorem, we calculate the probability of loan approval based on factors such as:
   - CIBIL score being above 500
   - Whether the applicant is self-employed
   - Monthly income being higher than the EMI
   
   These prior probabilities are calculated from historical data in the dataset, allowing the system to make probabilistic decisions on future loan applications.

5. Potential Gain and Loss for the Bank:
   - Potential Gain: For approved loans, the total potential gain is calculated as the total repayment amount (EMIs) over the entire loan period. The formula used is the EMI multiplied by the total number of installments (months).
   - Potential Loss: We introduced a 20% default rate. This means that 20 out of every 100 loans are expected to default. Thus, 20% of the total loan amount from approved loans is considered as potential loss due to defaults.

6. Consolidated Output:
   After the user enters multiple loan applications (e.g., 5 loans), the model:
   - Outputs the decision for each loan (Approved/Rejected)
   - Provides the EMI for each approved loan
   - Finally, displays consolidated results:
     - Total loan amount for all approved loans
     - Total potential gain for the bank from the approved loans
     - Total potential loss for the bank considering the 20% default rate.

 Example:
For 5 sample loan applications, the system calculates whether each loan is approved or rejected, based on the applicant's FOIR and CIBIL score. It then consolidates the total potential gain and loss for the bank. The default rate of 20% is factored into the loss calculation.

---

This project provides a practical way to analyze loan approvals based on real-world banking criteria while factoring in potential profit and risk, all within the framework of Bayesian probability and loan evaluation logic.

