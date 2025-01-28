# 🤖 Chatbot con LangChain y GPT-4o

Un chatbot interactivo basado en **LangChain**, potenciado por **GPT-4o** y desarrollado con **Streamlit**.  
Guarda las conversaciones en una base de datos **SQLite**, permitiendo a los usuarios acceder a su historial.  

---

## 🚀 Características  

✅ **Interfaz intuitiva** con Streamlit  
✅ **Chat en tiempo real** con GPT-4o   
✅ **Historial de conversaciones** almacenado en SQLite  
✅ **Separación de páginas** (Chatbot y Historial)  
✅ **Carga segura de claves API** con `.env`  
✅ **Estilos personalizados** en la interfaz  

---

## 🛠️ Instalación y Configuración  

### 1️⃣ Clona el repositorio  

```sh
git clone https://github.com/tu-usuario/chatbot-langchain.git 
cd chatbot-langchain
```

### 2️⃣ Instala las dependencias

```sh
pip install -r requirements.txt
```

### 3️⃣ Configura la clave de OpenAI

Crea un archivo .env en la raíz del proyecto y agrega tu clave de API de OpenAI:

```sh
OPENAI_API_KEY=tu_clave_aqui
```

### 4️⃣ Ejecuta la aplicación

```sh
streamlit run main.py
```

---

## 📜 Uso del Chatbot
### 1️⃣ Escribe un mensaje en el cuadro de texto y presiona Enter.
### 2️⃣ El chatbot responderá en base a GPT-4o.
### 3️⃣ Todas las conversaciones se guardan automáticamente en la base de datos.
### 4️⃣ Para ver el historial guardado, haz clic en "📜 Ver Historial de Conversaciones" en la barra lateral.

---

## 🏗️ Tecnologías Utilizadas
### 🐍 Python 3.11+
### 🤖 LangChain (para la integración con GPT-4o)
### 🎨 Streamlit (para la interfaz gráfica)
### 🛢 SQLite (para almacenar conversaciones)
### 🔐 dotenv (para gestionar claves de API de forma segura)
