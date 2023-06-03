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
