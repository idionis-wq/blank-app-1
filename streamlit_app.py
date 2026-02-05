import streamlit as st

st.set_page_config(page_title="MeinZweithaar – KI Demo", page_icon="💇‍♀️")

FIRMA = "MeinZweithaar"
ADRESSE = "Podbielskistraße 199, 30177 Hannover"
OEFFNUNG = "Montag bis Samstag von 09:00 bis 18:00 Uhr"
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.data = {}

st.title("💬 Willkommen bei MeinZweithaar –")
st.write("Ich bin der digitale Assistent und unterstütze Sie gerne diskret und unverbindlich.Sie können mir Fragen stellen zu: Beratung rund um Zweithaar & Haarersatz Termin-Anfragen Öffnungszeiten & Adresse")

user = st.text_input("Nachricht eingeben:")

if user:
    if st.session_state.step == "start":
        if "termin" in user.lower():
            st.write("🤖 Gerne 😊 Wie ist Ihr Name?")
            st.session_state.step = "name"
        elif "adresse" in user.lower():
            st.write(f"🤖 Sie finden uns in der {ADRESSE}.")
        elif "öffnungs" in user.lower():
            st.write(f"🤖 Wir sind {OEFFNUNG} für Sie da.")
        else:
            st.write("🤖 Wie kann ich Ihnen helfen? (Termin, Adresse, Öffnungszeiten)")

    elif st.session_state.step == "name":
        st.session_state.data["name"] = user
        st.write("🤖 Vielen Dank 😊 Worum geht es bei Ihrem Termin?")
        st.write("👉 Herren / Damen / Zweithaar")
        st.session_state.step = "kategorie"

    elif st.session_state.step == "kategorie":
        st.session_state.data["kategorie"] = user
        st.write("🤖 Bitte beschreiben Sie kurz Ihr Anliegen.")
        st.session_state.step = "anliegen"

    elif st.session_state.step == "anliegen":
        st.session_state.data["anliegen"] = user
        st.write("🤖 Wann wünschen Sie den Termin?")
        st.session_state.step = "termin"

    elif st.session_state.step == "termin":
        st.session_state.data["termin"] = user

        st.success("✅ Termin-Anfrage aufgenommen")
        st.write("🤖 Vielen Dank 😊 Wir melden uns zeitnah zur Bestätigung.")

        st.subheader("📱 WhatsApp-Vorschau")
        st.code(
            f"Hallo {st.session_state.data['name']}, vielen Dank für Ihre Anfrage bei MeinZweithaar 😊\n\n"
            f"Bereich: {st.session_state.data['kategorie']}\n"
            f"Anliegen: {st.session_state.data['anliegen']}\n"
            f"Wunschtermin: {st.session_state.data['termin']}\n\n"
            "Wir melden uns schnellstmöglich zur Bestätigung.\n"
            "Ihr Team von MeinZweithaar"
        )

        st.session_state.step = "start"
        st.session_state.data = {}
