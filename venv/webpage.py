import streamlit as ys

ys.title("My to-do App")
ys.subheader("This Is My Todo App")
ys.write("This App is used to Increase Your productivity")

for todo in todos:
    ys.checkbox(todo)