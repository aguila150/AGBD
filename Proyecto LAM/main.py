from database import Base, Session, engine
from models import Cliente, Rol, Usuario

# Borra las tablas existentes y las crea de nuevo con la estructura actualizada
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()

# 1. Crear el cliente
nuevo_cliente = Cliente(
    nombre="Juan",
    apellido="Pérez",
    email="juan@mail.com",
    telefono="1112345678",  # Tamaño corto para que entre en VARCHAR(20)
    direccion="Av. Siempre Viva 742",
)

# 2. Crear el rol
nuevo_rol = Rol(nombre="Admin")

# 3. Crear el usuario enlazándolo al cliente y al rol directamente
nuevo_usuario = Usuario(
    nombre="lam",
    email="lam@gmail.com",
    rol=nuevo_rol,
    cliente=nuevo_cliente,
)

# Guardar todo en la base de datos
session.add_all([nuevo_cliente, nuevo_rol, nuevo_usuario])
session.commit()
session.close()

print("¡Tablas recreadas y registros guardados exitosamente!")