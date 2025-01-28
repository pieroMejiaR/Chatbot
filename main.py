import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from database import guardar_mensaje

# Cargar variables de entorno desde .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Verificar si la clave API está configurada
if not OPENAI_API_KEY:
    st.error("🔴 ERROR: Falta la clave de OpenAI en el archivo .env")
    st.stop()

# Inicializar el modelo de chat
llm = ChatOpenAI(model_name="gpt-4o-mini")

# Configurar memoria para recordar la conversación
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Estilos
st.markdown("""
    <style>
        .stChatMessage {
            border-radius: 15px;
            padding: 10px;
        }
        .stChatMessageUser {
            background-color: #DCF8C6;
            color: black;
        }
        .stChatMessageAssistant {
            background-color: #E5E5EA;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Chatbot con LangChain y GPT-4o")

# Inicializar historial de mensajes en la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Entrada del usuario
a_input = st.chat_input("Escribe tu mensaje...")
if a_input:
    # Guardar mensaje del usuario en la sesión
    st.session_state.messages.append({"role": "user", "content": a_input})
    st.chat_message("user").write(a_input)
    
    # Obtener respuesta del modelo
    response = llm.invoke(a_input)
    memory.save_context({"input": a_input}, {"output": response.content})
    
    # Guardar en la base de datos
    guardar_mensaje(a_input, response.content)
    
    # Mostrar respuesta en la sesión
    st.session_state.messages.append({"role": "assistant", "content": response.content})
    st.chat_message("assistant").write(response.content)
