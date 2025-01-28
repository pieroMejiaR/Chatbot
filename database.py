from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Conectar a la base de datos SQLite
DATABASE_URL = "sqlite:///chatbot.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Definir la tabla de conversaciones
class Conversacion(Base):
    __tablename__ = "conversaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(Text, nullable=False)
    asistente = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Función para guardar mensajes en la base de datos
def guardar_mensaje(usuario, asistente):
    nueva_conversacion = Conversacion(usuario=usuario, asistente=asistente)
    session.add(nueva_conversacion)
    session.commit()

def obtener_historial():
    return session.query(Conversacion).order_by(Conversacion.timestamp).all()
