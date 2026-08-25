from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    categoria = Column(String)

engine = create_engine("sqlite:///productos.db", echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:

    p1 = Producto(nombre="Remera", precio=400, stock=15, categoria="Ropa")
    p2 = Producto(nombre="Pantalon", precio=900, stock=8, categoria="Ropa")
    p3 = Producto(nombre="Zapatillas", precio=1200, stock=5, categoria="Calzado")
    p4 = Producto(nombre="Gorra", precio=300, stock=20, categoria="Accesorios")
    p5 = Producto(nombre="Mochila", precio=700, stock=10, categoria="Accesorios")

    session.add(p1)
    session.add(p2)
    session.add(p3)
    session.add(p4)
    session.add(p5)

    session.commit()

    productos = session.query(Producto).filter(Producto.precio < 500).all()

    for producto in productos:
        print(producto.nombre, producto.precio)