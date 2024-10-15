%%writefile app.py
import streamlit as st
import math

def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return result
    except Exception as e:
        return str(e)

st.title("Scientific Calculator")

expression = st.text_input("Enter a mathematical expression (use math functions like sqrt, sin, cos, etc.):")

if st.button("Calculate"):
    result = calculate(expression)
    st.write("Result:", result)
