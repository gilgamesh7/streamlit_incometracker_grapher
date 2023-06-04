import streamlit as st
import plotly.graph_objects as go

import calendar
from datetime import datetime

# Set up global values
incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = "NZD"
page_title = "Income & Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered" # wide is another option

# Basic webpage configuration
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(f"{page_title} {page_icon}")

# Drop downs for period
years = [datetime.today().year-1, datetime.today().year, datetime.today().year+1]
months = list(calendar.month_name[1:])

# Form for entering currency
st.header(f"Data entry in {currency}")

with st.form ("entry_form_key", clear_on_submit=True):
    # Drop downs
    month_col, year_col = st.columns(2)
    month_col.selectbox("Select Month:", months, key="month")
    year_col.selectbox("Select Year:", years, key="year")

    # Divider
    "---"

    # Expanders, with number input boxes & add/subtract 
    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income} : ", min_value=0, format="%i", step=5, key=income)

    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense} : ", min_value=0, format="%i", step=5, key=expense)

    # Text area
    with st.expander("Comments"):
        st.text_area("",placeholder="Enter a comment here ...")

    "---"

    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = f"{str(st.session_state['year'])}_{str(st.session_state['month'])}" 
        incomes_dict = {income : st.session_state[income] for income in incomes}
        expenses_dict = {expense : st.session_state[expense] for expense in expenses}
        

        # Success message in green
        st.success("Financial data saved successfully")

"---"

st.header("Data Visualization")
with st.form("saved_periods_key"):
    period = st.selectbox("Select Period:", ["2022_March"])
    submitted = st.form_submit_button("Plot Period")
    if submitted:
        comment = "Test Comment ..."
        incomes = {'Salary': 10000000, 'Blog': 20000, 'Other Income': 300000}
        expenses = {'Rent': 20, 'Utilities': 30, 'Groceries': 40, 'Car': 50, 'Other Expenses': 60, 'Saving': 70}

        


