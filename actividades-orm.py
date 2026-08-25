from sqlalchemy import Column, Integer, String,Boolean, Float, desc , create_engine, or_
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    categoria = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    activo = Column(Boolean, default= True)

engine = create_engine("sqlite:///producto.db", echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    producto =[
     Producto(nombre="Teclado mecanico", categoria="perifericos", precio=8500, stock=15 ),
     Producto(nombre="Mouse inalambrico", categoria="perifericos", precio=4200, stock=30 ),
     Producto(nombre="Monitor 24 pulgadas", categoria="monitores", precio=62000, stock=8 ),
     Producto(nombre="Auriculares bluetooth", categoria="audio", precio=12300, stock=20 ),
     Producto(nombre="Webcam Full HD", categoria="perifericos", precio=9800, stock=12),
     Producto(nombre="SSD 1TB", categoria="almacenamiento", precio=18500, stock=25),
     Producto(nombre="RAM 16GB", categoria="componentes", precio=15600, stock=18),
     Producto(nombre="Mousepad XL", categoria="perifericos", precio=2100, stock=40),
     Producto(nombre="Hub USB-C", categoria="accesorios", precio=5400, stock=6, activo = False),
     Producto(nombre="Cable HDMI", categoria="accesorios", precio=1800, stock=50)
    ]
 
    session.add_all(producto)

    session.commit()
    print(session.query(Producto).count())

    #result = session.query(Producto).filter(Producto.categoria == "perifericos").all()
    
    #for r in result:
    #   print(r.nombre, r.precio)

    #precioMayor = session.query(Producto).filter(Producto.precio > 10000).group_by(Producto.nombre).order_by(Producto.precio.desc()).all() 

    #for p in precioMayor:
    #    print (p.nombre, p.precio)

    #stockMenor = session.query(Producto).filter(Producto.stock <= 12, Producto.activo == True).group_by(Producto.nombre).all() 

    #for s in stockMenor:
    #    print(s.nombre,s.stock)

    #precioEntre = session.query(Producto).filter(Producto.precio > 5000, Producto.precio < 20000).group_by(Producto.nombre).all()  

    #for p in precioEntre:
    #    print(p.nombre,p.precio)

    #masCaro = session.query(Producto).order_by(Producto.precio.desc()).first() 

    #print(masCaro.nombre, masCaro.precio)

    #productoInactivo = session.query(Producto).filter(Producto.activo == False).group_by(Producto.nombre).all()

    #for p in productoInactivo:
    #    print(p.nombre)

    #categoriaOr = session.query(Producto).filter(or_(Producto.categoria == "audio", Producto.categoria == "componente")).all()


    #for c in categoriaOr:
    #    print(c.nombre, c.categoria)
    
    #contieneA = session.query(Producto).filter(Producto.nombre.contains("a")).group_by(Producto.nombre).all()

    #for c in contieneA:
    #    print(c.nombre)

    empiezaConM = session.query(Producto).filter(Producto.nombre.startswith("M")).group_by(Producto.nombre).all()

    for e in empiezaConM:
        print(e.nombre)