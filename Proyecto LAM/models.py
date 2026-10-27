from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(20))
    direccion = Column(String(200))

    # Relación uno a uno con Usuario
    usuario = relationship("Usuario", back_populates="cliente", uselist=False)


class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # Relación con Rol
    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    rol = relationship("Rol", back_populates="usuarios")

    # Relación con Cliente
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=True)
    cliente = relationship("Cliente", back_populates="usuario")