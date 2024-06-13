import streamlit as st

# Initialize the connection to the database
conn = st.connection("postgresql",type="sql")

# Perform some SQL queries
df = conn.query('select * from say_hello;', ttl='10m')

# Print results
for row in df.iterrows():
    st.write(f"row: {row}")
    st.write(f"{row.id} has a :{row.first_name}")
