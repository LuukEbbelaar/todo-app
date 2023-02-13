import streamlit as st
from modules import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")

st.write('This app is to increase productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="input new todo", label_visibility='hidden',
              placeholder='Enter a new todo...',
              on_change=add_todo, key='new_todo')

