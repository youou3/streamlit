import streamlit as st
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host=st.secrets["host"],
        database=st.secrets["database"],
        user=st.secrets["user"],
        password=st.secrets["password"],
    )
    return conn

def run_query(query):
    conn = connect_to_db() 
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def main():
    st.title("Streamlit Demo")
    query = st.text_input("Enter your SQL query")
    if st.button("Run Query"):
        results = run_query(query)
        st.write(results)


if __name__ == "__main__":
    main()


