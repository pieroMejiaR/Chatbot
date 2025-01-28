import streamlit as st
from database import obtener_historial

st.title("📜 Historial de Conversaciones")

# Obtener historial de la base de datos
historial = obtener_historial()

if historial:
    for h in historial:
        st.write(f"🧑 **Usuario:** {h.usuario}")
        st.write(f"🤖 **Asistente:** {h.asistente}")
        st.write("---")
else:
    st.write("❌ No hay conversaciones guardadas aún.")
