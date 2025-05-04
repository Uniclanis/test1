import streamlit as st

# Din app
st.title("Välkommen till hälsokollen!")
st.write("Fyll i uppgifterna nedan:")

# Frågor till användaren
name_first = st.text_input("Förnamn:")
name_second = st.text_input("Efternamn:")
age = st.text_input("Hur gammal är du?")
weight = st.text_input("Hur mycket väger du?")
height = st.text_input("Hur lång är du?")

# När alla fält är ifyllda, visa sammanfattning
if name_first and name_second and age and weight and height:
    st.write("Se nedan för din sammanställda information:")
    st.write("---")
    st.subheader("Din information:")
    st.write(f"👤 Namn: {name_first} {name_second}")
    st.write(f"📅 Ålder: {age} år")
    st.write(f"⚖ Vikt: {weight} kg")
    st.write(f"📏 Längd: {height} cm")
    
    # JavaScript för att scrolla ner efter sammanfattningen
    scroll_js = """
        <script>
            window.scrollTo(0, document.body.scrollHeight);
        </script>
    """
    st.markdown(scroll_js, unsafe_allow_html=True)

else:
    st.write("Fyll i alla uppgifter för att se din sammanfattning.")
