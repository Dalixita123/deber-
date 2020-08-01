from .models import Cliente,Producto,Factura,DetalleFactua

'''
------------------------------------------------------------
        Insertar registros en los modelos
------------------------------------------------------------
'''

#1)
P = Producto(descripcion='Aceite Girazol',precio=1.50,stock=2000)  
P.save()
#2)
Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000) 


#insertar 2 registos de producto adicionales
Producto.objects.create(descripcion='Mantequilla 500kg',precio=2.50,stock=2000) 
Producto.objects.create(descripcion='Manjar',precio=0.70,stock=5000) 
Producto.objects.create(descripcion='Fideos Don Vitorio',precio=1.40,stock=300) 
Producto.objects.create(descripcion='Nutrileche',precio=0.90,stock=500) 
Producto.objects.create(descripcion='Atun Bankam',precio=1.20,stock=1000) 
#--insertar 2 registos de Cliente
cliente1= Cliente(ruc='09401140927001',nombre='Karla Estefania Moran Garcia ',direccion='Milagro')#Instanciamos Cliente en varible cliente1 con valores
cliente1.save()#funcion save() guarda lo que contiene la variable cliente1 a la base de datos

Cliente.objects.create(ruc='0981287585001',nombre='Juan Carlos Zambrano Macias',direccion='Guayaquil') 
   # -----------------registos de Cliente adicionales
Cliente.objects.create(ruc='0998122285001',nombre='Mario Jesua Miranda Coello',direccion='Bucay') 
Cliente.objects.create(ruc='0918276162001',nombre='Diana Marina Solis Fuentes',direccion='Empalme') 
Cliente.objects.create(ruc='0812711121001',nombre='Maria Renata Alvarado Vera',direccion='Duran') 
Cliente.objects.create(ruc='0837122812001',nombre='Carlos Manuel Sanchez Marin',direccion='Milagro')
Cliente.objects.create(ruc='0837122812001',nombre='Jesus Martin Torres Castro',direccion='Balzar')

#--insertar 2 registro de Factura 
factura1= Factura(cliente=cliente1,fecha='2020-08-01',total=2.40)#Instanciamos Factura en varible factura1 con valores
factura1.save()#funcion save() guarda lo que contiene la variable factura1 a la base de datos
cliente2= Cliente.objects.get(id=2) #consultamos cliente con id =2 y asignamos a variable cliente2
Factura.objects.create(cliente=2,fecha='2020-07-20',total=15.00)#funcion create() recibe todos los valores  y hace un impacto directo a la base 

#--insertar 2 registro de DetalleFactura 
    
    #detalle factura 1
producto2= Producto.objects.get(id=2)#consultamos el producto con id 2
DetalleFactura.objects.create(factura=factura1,producto=P)#Usamos variable P y factura1 creadas  anteriormente 
DetalleFactura.objects.create(factura=factura1,producto=producto2)#Creamos otro item con producto2 y la misma factura
    #detalle factura 2
factura2 = Factura.objects.get(id=2)#consultamos factura con id 2 y asignamos a variable factura2
detallefactura2 = DetalleFactura(producto=P,factura=factura2)#Instanciamos DetalleFactura  a variable detallefactura2
detallefactura2.save()#funcion save() guarda la instancia asignada a la base de datos
'''
------------------------------------------------------------
        Actualizar  registros en los modelos
------------------------------------------------------------
'''
    #1)
p = Producto.objects.get(id=1)
p.precio=1.3
p.save()
    #2)
Producto.objects.filter(id=1).update(precio=1.7)

#--modificar 2 registro de Producto
Producto.objects.filter(descripcion='Coca Cola').update(iva=True,precio=1.50,stock=500000)#Actualizan directa a la base de datos
producto2 = Producto.objects.get(id=1)#consultamos producto id 2
producto2.iva=False
producto2.stock=4000
producto2.precio=2.5
producto2.save()
#--modificar 2 registro de Cliente
Cliente.objects.filter(ruc='09401140927001',direccion='Milagro').update(direccion='Duran',nombre='Karla Stefany Moran Garcia')
    
clienteu = Cliente.objects.get(ruc='0981287585001')
producto = Producto.objects.get(id=1)
clienteu.direccion='Yaguachi'
clienteu.producto =producto
clienteu.save()

'''
------------------------------------------------------------
        Eliminar registros en los modelos 
------------------------------------------------------------
'''
    #1)
p=Producto.objects.get(id=2)
p.delete()
    #2) 
Producto.objects.filter(id=6).delete()


'''
------------------------------------------------------------
       Querys de un modelo 
------------------------------------------------------------
'''
#1)
p=Producto.objects.all()
    #---adicionales
Cliente.objects.all()
Factura.objects.all()
DetalleFactua.objects.all()
#2)
p=Producto.objects.get(id=2)
    #---- adicional
Cliente.objects.get(id=7)
Factura.objects.get(id=1)
DetalleFactura.objects.get(id=3)
#3)
Producto.objects.filter(id__lte=2)
    #---adicional
Cliente.objects.filter(id__lte=4)#id <=
Factura.objects.filter(id__lte=2)
DetalleFactura.objects.filter(id__lte=1)
#4)
Producto.objects.exclude(descripcion__icontains='Cola')
    #---adicional
Cliente.objects.exclude(nombre__icontains='sol')
c= Cliente.objects.get(id=2)
Factura.objects.exclude(cliente=c)
f = Factura.objects.get(id=1)
DetalleFactura.objects.exclude(factura=f)

#5)
Producto.objects.filter(id__gte=4)#id >=
    #-----adicional
Cliente.objects.filter(id__gte=7)
Factura.objects.filter(id__gte=1)
DetalleFactua.objects.filter(id__gte=2)

#6)
Producto.objects.filter(id__gt=4).values('id','descripcion')# id >4
    #-----adicional
Cliente.objects.filter(id__gt=4).values('id','descripcion')
Factura.objects.filter(id__gt=1).values('id','fecha')
DetalleFactura.objects.filter(id__gt=2).values('id','producto')
#7)
Producto.objects.filter(id__lt=4).values('id','descripcion')# id < 4
        #-----adicional
Cliente.objects.filter(id__lt=4).values('id','descripcion')
Factura.objects.filter(id__lt=1).values('id','fecha')
DetalleFactura.objects.filter(id__lt=2).values('id','producto')
#8)
Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')
    #-----adicional
Cliente.objects.filter(descripcion='Coca Cola').values('id','descripcion')
Factura.objects.filter(fecha='2020-07-20').values('id','fecha')
DetalleFactura.objects.filter(id=2).values('id','producto','factura')


'''
------------------------------------------------------------
       Querys de varios modelos (relacionados) 
------------------------------------------------------------
'''

#1)
Factura.objects.filter(cliente__nombre='Juan Carlos Zambrano Macias')
Factura.objects.filter(cliente__id=1)

DetalleFactura.objects.filter(factura__cliente__id=1 )
DetalleFactura.objects.filter(producto__id=1 )
#2)
c= Cliente.objects.get(nombre='Juan Carlos Zambrano Macias')
c2 = Cliente.objects.get(id=1)
#3)
c.factura_set.all() 
c2.factura_set.all()
#4)
c.factura_set.filter(id=2)
c2.factura_set.filter(id=1)
#5)
Factura.objects.select_related('cliente').filter(cliente__nombre='Juan Carlos Zambrano Macias')
#6) 
Cliente.objects.prefetch_related('producto').filter(nombre='Juan Carlos Zambrano Macias').values('nombre','producto__descripcion')