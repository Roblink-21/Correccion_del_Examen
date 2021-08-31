# Correccion_del_Examen

Realizar la corrección del examen y ponerla en un repositorio de github. Esta vez lo pueden hacer por código o manualmente con las herramientas.

Integrantes:

* Miguel Cuenca
* Luis Jacome
* Kevin Morales
* Roberth Pincha
* Carlos Quel
* Sebastian Valencia
* Michael Valenzuela

# Parte 1

* Script 1: "1.py"

1. Contiene la cosecha de datos de Twitter en base a la localización de 3 ciudadaes.

![image](https://user-images.githubusercontent.com/66259796/131237579-85f33c49-f96b-489a-bcde-5983e5d658fa.png)

2. Creación de la base de datos 'ciudad5' con las coordenadas de la primera ciudad.

![image](https://user-images.githubusercontent.com/66259796/131237591-96ccdedd-b070-4cd0-87fd-d03d53ea1177.png)

3. Procedimiento del guardado en la base de datos.

![3](https://user-images.githubusercontent.com/66259796/131237303-f0730127-7bd7-42ce-b81a-aed8d8f0dcd6.PNG)

![image](https://user-images.githubusercontent.com/66259796/131237620-20260d75-9407-40f4-8d32-f204e79ed416.png)

5. Creación de la base de datos 'ciudad2' con las coordenadas de la segunda ciudad.

![image](https://user-images.githubusercontent.com/66259796/131237628-75caf1f4-c0a5-445e-a72a-3cf5494d1b42.png)

6. Procedimiento del guardado en la base de datos.

![2](https://user-images.githubusercontent.com/66259796/131237306-4d69119e-426d-4dbd-b8de-85a06feba643.PNG)



![image](https://user-images.githubusercontent.com/66259796/131237659-f2ffe055-a232-48cf-8948-b1251a7a8610.png)

8. Creación de la base de datos 'ciudad3' con las coordenadas de la tercera ciudad.

![image](https://user-images.githubusercontent.com/66259796/131237672-89044708-2b8d-40b1-a310-0fe232e8809a.png)

9. Procedimiento del guardado en la base de datos.

![1](https://user-images.githubusercontent.com/66259796/131237292-370afe3a-55ba-4f69-8811-642f5ba8cd69.PNG)

10. Comprobación del almacenamiento de los datos en couchDB en las bases de datos 'ciudad1', 'ciudad2' y 'ciudad3'

![image](https://user-images.githubusercontent.com/66259796/131237500-c37a8318-2cec-4fd4-a100-c3a64b97bd88.png)

# Parte 2

* Script 2: "2.py"

1. Contiene la cosecha de datos de Twitter en base a un track de palabras claves.

![image](https://user-images.githubusercontent.com/66259796/131237689-20b38b37-240a-42c8-9a8e-0c67b4013ffe.png)

2. Creación de la base de datos 'track' con sus respectivas palabras claves 'atletismo','carreras'.

![image](https://user-images.githubusercontent.com/66259796/131237702-51a3609a-20c9-4c0f-bf72-5ca45447562f.png)

3. Procedimiento del guardado en la base de datos.

![4](https://user-images.githubusercontent.com/66259796/131237321-16dd1ef0-37fa-490d-bf90-11b335339d81.PNG)

4. Comprobación del almacenamiento de los datos en couchDB en la base de datos 'track'

![image](https://user-images.githubusercontent.com/66259796/131237528-5a9b2faf-ecfb-4dab-8d4b-26d99577db4e.png)

# Parte 3

1. Se empieza estableciendo la conexión con mongodb mediante pymongo y se hace la importación de las respectivas herramientas

![image](https://user-images.githubusercontent.com/58041699/131235523-e4c89d15-25d0-4ed9-b0e3-48660fb10109.png)

2. Se generan las funciones para su posterior limpieza mediante un for

![image](https://user-images.githubusercontent.com/58041699/131235530-0c03d5df-9e9e-485c-9183-871fb0a690eb.png)

![image](https://user-images.githubusercontent.com/58041699/131235533-687e6239-243b-4465-9b3b-09f2697c9851.png)

3. Se trasladan los datos al dataframe

![image](https://user-images.githubusercontent.com/58041699/131235546-6c0d42b7-43f5-4d8d-97fc-5fd32f7d43b1.png)

![image](https://user-images.githubusercontent.com/58041699/131234850-c4574f9d-704a-4328-81b6-f0a91db4fab3.png)

4. Se establece la conexión con mongodb y se insertan los datos

![image](https://user-images.githubusercontent.com/58041699/131235200-1708c939-b9dc-4b2d-bcb8-0b9518ec2b6b.png)

5. Por ultimo la información que se envio es presentada en formato JSON

![image](https://user-images.githubusercontent.com/58041699/131235219-351a6b02-39e1-4977-9bd3-f2a4e95f3f92.png)

# Parte 4
1. Empezamos  estableciendo la conexión con mongodb mediante pymongo y se hace la importación de las respectivas herramientas algo que tomar en cuenta es la direccion
del host 127.0.0.1: 27017

![image](https://user-images.githubusercontent.com/66259796/131237245-a119113d-8466-4453-b04c-009b1a1e5ce8.png)

2. Podemos apreciar en el codigo asignamos por medio de un try un pint donde nos aseguramos  el guardado exitoso del dataset. 
![image](https://user-images.githubusercontent.com/66259796/131237265-bdff3f3c-fb32-4ba0-a4ef-6dac5c45246c.png)

3. Verificamos en el comando que la terminal nos imprime el texto guardado exitosamente.
![cmdExe](https://user-images.githubusercontent.com/66259796/131237170-fc7e7f90-4780-434b-b912-8e8f156b874c.PNG)

4. Ya sale la base de datos creada  en nuestra interfaz.
![DB](https://user-images.githubusercontent.com/66259796/131237210-516e7651-ae7b-4bdd-a09e-70183ec3ab0e.PNG)

5. Como podemos apreciar ya se nos presenta datos en nuestra base  de datos.
![datasetMongoDB](https://user-images.githubusercontent.com/66259796/131237213-3bd6185c-87b6-485e-b951-ce3af1df735b.PNG)

# Parte 5

El siguiente script es desarrollado en una linea de comandos de la cual solo se recogen los csv de las cuentas de tiktok
  
  ![Captura2](https://user-images.githubusercontent.com/58041699/127724845-94bd6fc2-375c-4c40-b35f-1be9cde9d644.JPG)

  Ademas, se creo una carpeta contenedora para guardarlo y posteriormente usarlas para enviar estos datos a sql lite
  
  ![Captura](https://user-images.githubusercontent.com/58041699/127724865-6a478968-ec19-4ce4-9322-28b8f2f4ecfb.JPG)
  
  ![Captura3](https://user-images.githubusercontent.com/58041699/127724887-07de9c85-795b-4c15-93d3-e8a3e7c7b583.JPG)
  
  - Proceso SQL LITE
  
  Para ello debemos importar las librerias pandas y sql.
  Ademas se debe mencionar la base de datos para hacer la coneccion con nuestro SQL LITE
  
  ![Captura4](https://user-images.githubusercontent.com/58041699/127724907-e4cf708a-24a1-4f89-9c05-3c93db3d4cfc.JPG)
  
  ![Captura5](https://user-images.githubusercontent.com/58041699/127724934-a8fc877d-4af2-4ea9-a146-088c361dad0b.JPG)

  Por ultimo, junto a la nueva bd creada en sql, enviamos los datos de csv
  
  ![Captura6](https://user-images.githubusercontent.com/58041699/127724964-60aacbbb-9b18-429a-9d0d-86375f3e1948.JPG)
  
  # Evidencia 5
  
  ![Captura7](https://user-images.githubusercontent.com/58041699/127725009-f6cfdb0b-9bd9-467a-81b6-a1a89f236443.JPG)

# Parte 7

1. Creamos la base de datos en nuestro CouchDB.

![image](https://user-images.githubusercontent.com/58041699/131396511-2e4f0a7d-528c-4718-8350-43c406ddcd6d.png)

2. Establecemos  el codigo para poder ingresar a nuestro couch db desde Jupyter notebook.

![image](https://user-images.githubusercontent.com/58041699/131396584-e112a790-52df-40fa-8de1-3bbbee3f5e0e.png)

3. Asignamos el nombre de la base de datos.

![image](https://user-images.githubusercontent.com/58041699/131396735-a68a012f-2b77-4482-b6e3-d52a03624e5d.png)

4. Nuestra base de datos fue creada en nuestro couchDb. 

![image](https://user-images.githubusercontent.com/58041699/131396774-cb08e6b0-2a14-49e9-9a56-7144a1d0619b.png)

5. Establacemos la conexión con mongoDB.

![image](https://user-images.githubusercontent.com/58041699/131396829-d24d99c1-c985-4b7b-8c06-d7ee25d8146b.png)

6. Nos presenta una pantalla el estado de la conexión.

![image](https://user-images.githubusercontent.com/58041699/131396856-bab52fb7-6d52-434c-9e2c-403250e59915.png)

7.Nuestra base de datos en couchDB ya contiene nuestra base de datos .

![image](https://user-images.githubusercontent.com/58041699/131396953-2fc01b22-058d-48c4-9ac9-ba263aa4b672.png)

8. Podemos apreciar los datos guardados en nuestra base de datos. 

![image](https://user-images.githubusercontent.com/58041699/131397001-acc47cde-c074-43f4-9ec8-ee86e02be746.png)


# Parte 8
1. 
![image](https://user-images.githubusercontent.com/58041699/131410362-8551cc3e-c813-46d9-a75d-cf15617250ee.png)

2.Importamos las librerias necesarias en nuestro Jupyter Notebook .

![image](https://user-images.githubusercontent.com/58041699/131410427-3e337bc2-6a94-4986-9e31-b87c7ffa3ceb.png)

3. Establecemos conexión con nuestro mongoDB  y ademas selecionamos nuestra base de datos. 

![image](https://user-images.githubusercontent.com/58041699/131410750-1edf0c32-7a29-4ee2-91c1-aa74718892d3.png)

4. Ingresamos a nuestro mongoDB Atlas  y copiamos al dirección para poder sincronizar con nuestro MongoDB Compas

![image](https://user-images.githubusercontent.com/58041699/131410894-f7ce2164-ef0f-4736-b614-92cf4d209284.png)

5. La dirección copiada de mongo atlas la ingresamos en nuestro cliente , y creamos la base de datos

![image](https://user-images.githubusercontent.com/58041699/131410811-a1420fe7-7662-4c05-894c-55baea301e7c.png)

6. Establecemos en nuestro codigo para poder crear nuestra abse de datos.

![image](https://user-images.githubusercontent.com/58041699/131410994-aa47d8d3-ba38-403e-8837-c3e04e779c2d.png)

7. Confirmamos la creación de nuestra base de datos, y no hemos presentado ningun problema. 

![image](https://user-images.githubusercontent.com/58041699/131411022-2fbca63a-9b2f-4268-8133-49b9ef672f17.png)

8. Podemos apreciar en nuestro interfaz de mongoDB ya tenmos nuestra abse creada con sus respectivos datos y sus atributos.

![image](https://user-images.githubusercontent.com/58041699/131411112-4a8dd9f7-aca9-48cf-b22f-a3304c991dd5.png)

# Parte 9
1. Importamos las librerias necesarias en nuestro Jupyter Notebook .

![image](https://user-images.githubusercontent.com/58041699/131416774-528b803b-035d-4ffe-ac79-8d6cc4d9e128.png)

2. Establecemos conexión con MongoDB , donde seleccionamos la base de datos o una base de datos local.

![image](https://user-images.githubusercontent.com/58041699/131416793-f5e152f2-559a-4518-8747-fe3a163bb227.png)

3. Se nos presenta el estado de conexión sobre nuestra base de datos.
 
![image](https://user-images.githubusercontent.com/58041699/131416820-ae16a421-ac23-4c0a-96fc-9fe481e583c3.png)

4. Trasladamos nuestra lista a un dataframe , generando un archivo csv.

![image](https://user-images.githubusercontent.com/58041699/131416832-baa1057d-ed92-41e8-9b2f-8d86eb7ccda3.png)

5. Se nos presenta los datos que han sido grabados en nuestra CSV con sus respectivos  atributos.

![image](https://user-images.githubusercontent.com/58041699/131416851-cf0c1e8f-595d-4f08-8f99-b0f99794f6b3.png)


# Parte 10
1. Importamos las librerias necesarias en nuestro Jupyter Notebook.

![image](https://user-images.githubusercontent.com/58041699/131416276-c56ff258-59c6-4d12-a417-627503ad46ba.png)

2. Establecemos conexión con MongoDB , donde seleccionamos la base de datos o una base de datos local.

![image](https://user-images.githubusercontent.com/58041699/131416306-441a405a-7389-4dab-ac56-56677e99c546.png)

3. Se nos presenta el estado de conexión sobre nuestra base de datos.

![image](https://user-images.githubusercontent.com/58041699/131416333-58461121-bdc4-4066-aa96-a3b0a3eaf5f2.png)

4. Trasladamos nuestra lista a un dataframe , generando un archivo json.

![image](https://user-images.githubusercontent.com/58041699/131416362-48bd292f-4988-4550-ad33-7677f0fa2453.png)

5. Se nos presenta los datos que han sido grabados en nuestra CSV con sus respectivos  atributos.

![image](https://user-images.githubusercontent.com/58041699/131416385-b8927b7e-5225-4bde-985b-5cccb9e0f53d.png)





