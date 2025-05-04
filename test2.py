import streamlit as st

st.title("Välkommen till hälsokollen! 💬")

st.write("Fyll i uppgifterna nedan:")

# Namn med formatering
name_first = st.text_input("Förnamn").strip().capitalize()
name_second = st.text_input("Efternamn").strip().capitalize()

# Ålder, vikt, längd
age = st.text_input("Hur gammal är du? (år)")
weight = st.text_input("Hur mycket väger du? (kg)")
height = st.text_input("Hur lång är du? (cm)")

# När allt är ifyllt – visa sammanfattning
if name_first and name_second and age and weight and height:
    st.success("✅ Alla uppgifter är ifyllda!")
    st.markdown("⬇️ Scrolla ner för att se din sammanställda information")
    st.write("---")
    st.subheader("Din information:")
    st.write(f"👤 Namn: {name_first} {name_second}")
    st.write(f"📅 Ålder: {age} år")
    st.write(f"⚖ Vikt: {weight} kg")
    st.write(f"📏 Längd: {height} cm")

    # (valfritt) visa varning
    st.warning("⚠️ Detta kännetecknar extrem övervikt för din ålder.")
    st.error("🚨 Sök hjälp!")

else:
    st.info("👉 Fyll i alla fält för att få en sammanställning.")
