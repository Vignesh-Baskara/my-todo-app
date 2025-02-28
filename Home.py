import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todos(todos)

st.set_page_config(layout="wide")

st.title("My-Todo-App")
st.subheader("Chase your Tasks")
st.write("<h1>This app boosts your productivity.</h1>",
         unsafe_allow_html=True)

st.text_input(label="A*****Z", placeholder="Add your todo here", on_change=add_todo, key='new_todo')

for i, todo in enumerate(todos):
    cb = st.checkbox(todo, key=todo)
    if cb:
        todos.pop(i)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


