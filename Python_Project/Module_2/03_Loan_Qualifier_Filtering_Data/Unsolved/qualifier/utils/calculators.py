# This script contains a variety of financial calculator functions needed to determine loan qualifications.



# Calculates user's monthly debt-to-income ratio`
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    """Calculates the monthly debt ratio.

    Args:
        monthly_debt_payment (float): The monthly debt payment.
        monthly_income (float): The monthly income.

    Returns:
        monthly_debt_ratio (int): The monthly debt ratio.
    """
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio

# Calculates user's loan-to-value

def calculate_loan_to_value_ratio(loan_amount, home_value):
    
    """Calculates users loan to value ratio based on inputs.

    Args:
        loan_amount (int): The requested loan amount.
        home_value (int): The home value.

    Returns:
        The loan-to-value ratio
    """
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio