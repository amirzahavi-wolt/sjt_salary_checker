## Calculator using Streamlit
from typing import Dict
import streamlit as st

# Title and input
st.title("Simple Salary Calculator")
total_hours_worked = st.text_input("Enter the total amount of hours worked (monthly)")
fifty_hours_worked = st.text_input("Enter the amount of hours worked on Saturdays (150% hourly wage, monthly)")
hundred_hours_worked = st.text_input("Enter the total amount of hours worked on holidays/sundays (200% hourly wage, monthly)")
base_hourly_wage = st.text_input("Enter your base hourly wage in EUR(for example - 12.5)")
tax_rate = st.text_input("Enter your yearly tax rate (from your Vero tax card. for example 0.21 if your tax rate is 21 percent)")

# Function to generate nudge
def calculate(total_hours_worked, fifty_hours_worked, hundred_hours_worked, base_hourly_wage, tax_rate) -> Dict[str, float]:
    base_wage = float(total_hours_worked) * float(base_hourly_wage)
    fifty_wage = float(fifty_hours_worked) * (0.5 * float(base_hourly_wage))
    hundred_wage = float(hundred_hours_worked) * (1.0 * float(base_hourly_wage))
    total_wage = base_wage + fifty_wage + hundred_wage
    pension_contribution = total_wage * 0.075
    unemployment_insurance_contribution = total_wage * 0.0079
    income_tax = float(total_wage) * float(tax_rate)
    net_income = total_wage - income_tax - unemployment_insurance_contribution - pension_contribution

    return {
        "base_wage": round(base_wage, 2),
        "fifty_wage": round(fifty_wage, 2),
        "hundred_wage": round(hundred_wage, 2),
        "total_wage": round(total_wage, 2),
        "pension_contribution": round(pension_contribution, 2),
        "unemployment_insurance_contribution": round(unemployment_insurance_contribution, 2),
        "income_tax": round(income_tax, 2),
        "net_income": round(net_income, 2),
    }

if st.button("Calculate"):
    res = calculate(total_hours_worked, fifty_hours_worked, hundred_hours_worked, base_hourly_wage, tax_rate)
    st.write(
        f"""
            Estimated salary breakdown:
            -----------------------------------------------------------------------
            Regular wage: €{res["base_wage"]}, \n
            Additional wages for hours worked on Saturdays: €{res["fifty_wage"]}, \n
            Additional wages for hours worked on holidays/sundays: €{res["hundred_wage"]}, \n
            -----------------------------------------------------------------------
            Total Gross Income: €{res["total_wage"]}, \n
            Pension Contribution: €{res["pension_contribution"]}, \n
            Unemployment Insurance Contribution: €{res["unemployment_insurance_contribution"]}, \n
            Income Tax: €{res["income_tax"]}, \n
            Expected Net Income: €{res["net_income"]}
            -----------------------------------------------------------------------
        """)
