Utilizacion de shell para modificar base de datos
ingreso:
>python manage.py shell

desde la carpeta de la aplicacion ingresamos al archivo models e importamos el modelo que necesitamos
>from <<nombreAPP>>.models import <<nombreModelo>>

creamos una variable y en ella guardamos el nuevo valor que vamos a ingresar en la base de datos, accediendo al modelo correspondiente
>p=Project(name="pruebaNombre")

podemos comprobar si la variable se creo
> p
salida: <Project: Project object (None)>

guardamos la variable creada
>p.save()

podemos ver los valores guardados en la base de datos
>Project.objects.all()

podemos ver los valores segun su id
>Projects.objects.get(id=1)

podemos ver los valores segun el nombre de la propiedad
>Projects.objects.get(name='pruebaNombre')

podemos realizar una busqueda
>Project.objects.filter(name__startswith="prueba")
se busca segun si hay una coincidencia en las primera parte del nombre

Otra manera de acceder a realizar una busqueda seria guardando los objetos del modelo en una variable
>p= Project.objects 

realizamos la misma busqueda accediendo a la variable
>p.filter(name__startwith="prueba")

