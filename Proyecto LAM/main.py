from database import engine, Session, Base
from models import Cliente

Base.metadata.create_all(engine)

session = Session()
nuevo = Cliente(
    nombre="Juan Pérez",
    email="juan@mail.com",
    telefono="+54 11 1234-5678",
    direccion="Av. Siempre Viva 742"
)
session.add(nuevo) 
session.commit()
session.close()

print("Cuenta creada")