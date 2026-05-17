import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Notes Frontend", layout="centered")

st.title("📝 Notes Frontend")
st.write("Frontend für die Notes-API")

st.subheader("📋 Alle Notes")

notes = []

try:
    response = requests.get(f"{API_URL}/notes")
    notes = response.json()
except Exception:
    st.error("Backend nicht erreichbar")
    st.stop()

if not notes:
    st.info("Noch keine Notes vorhanden.")
else:
    titles = [note["title"] for note in notes]

    selected_title = st.selectbox(
        "Note auswählen",
        titles
    )

    selected_note = next(
        note for note in notes if note["title"] == selected_title
    )

    st.markdown("### 📝 Details")
    st.write("**Titel:**", selected_note["title"])
    st.write("**Inhalt:**", selected_note["content"])
    st.write("**Kategorie:**", selected_note["category"])
    st.write("**Tags:**", ", ".join(selected_note["tags"]))

    st.divider()
st.subheader("➕ Neue Note erstellen")

with st.form("create_note_form"):
    title = st.text_input("Titel")
    content = st.text_area("Inhalt")
    category = st.text_input("Kategorie", value="general")
    tags_input = st.text_input("Tags (kommagetrennt)", value="")

    submitted = st.form_submit_button("Create Note")

    if submitted:
        tags = [t.strip() for t in tags_input.split(",") if t.strip()]

        payload = {
            "title": title,
            "content": content,
            "category": category,
            "tags": tags,
        }

        try:
            resp = requests.post(f"{API_URL}/notes", json=payload)
            if resp.status_code == 201:
                st.success("✅ Note erfolgreich erstellt")
                st.rerun()
            else:
                st.error(f"❌ Fehler: {resp.status_code}")
                st.json(resp.json())
        except Exception:
            st.error("Backend nicht erreichbar")