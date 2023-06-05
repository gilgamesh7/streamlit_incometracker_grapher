import streamlit as st
from streamlit_option_menu import option_menu
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


# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],
    orientation="horizontal"
)

if selected == "Data Entry":
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

if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved_periods_key"):
        period = st.selectbox("Select Period:", ["2022_March"])
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            comment = "Test Comment ..."
            incomes = {'Salary': 1000, 'Blog': 2000, 'Other Income': 3000}
            expenses = {'Rent': 20, 'Utilities': 30, 'Groceries': 40, 'Car': 50, 'Other Expenses': 60, 'Saving': 70}

            # Aggregate metrics
            total_income = sum(incomes.values())
            total_expenses = sum(expenses.values())
            remaining_budget = total_income - total_expenses

            # Display aggegated metrics
            income_col, expense_col, remaining_col = st.columns(3)
            income_col.metric("Total Income" , f"{total_income} {currency}")
            expense_col.metric("Total Expenses", f"{total_expenses} {currency}")
            remaining_col.metric("RemainingBudget", f"{remaining_budget} {currency}")
            st.text(f"Comment : {comment}")

            # Create SanKey chart
            label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
            source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
            value = list(incomes.values()) + list(expenses.values())

            # List -> Dict -> Sankey
            link = dict(source=source, target=target, value=value)
            node = dict(label=label, pad=20, thickness=30, color="#E694FF")
            data = go.Sankey(link=link, node=node)

            # Plot
            fig = go.Figure(data)
            fig.update_layout(margin=dict(l=0, t=5, b=5))
            st.plotly_chart(fig, use_container_width=True)

