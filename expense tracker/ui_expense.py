import streamlit as st
from expense import (
    add_expense,
    total_expenses,
    filter_expenses_by_category
)
from storage import load_expenses, save_expenses

if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()
    
st.title("Expense Tracker")
amount = st.number_input("Amount", min_value=0.0)
category = st.text_input("Category")

if st.button("Add Expense"):
    add_expense(st.session_state.expenses, amount, category)
    save_expenses(st.session_state.expenses)
    st.success("Expense added!")

st.subheader("Total")
st.write(total_expenses(st.session_state.expenses))

st.subheader("Filter by category")
filter_cat = st.text_input("Category to filter")

if filter_cat:
    filtered = list(
        filter_expenses_by_category(st.session_state.expenses, filter_cat)
    )
    st.write(filtered)
