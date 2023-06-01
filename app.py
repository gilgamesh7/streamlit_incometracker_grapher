import streamlit as st
import plotly.graph_objects as go

incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = "NZD"
page_title = "Income & Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered" # wide is another option

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(f"{page_title} {page_icon}")