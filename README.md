## 👋 ¡Bienvenidos usuarios a mi proyecto! control de inventario

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un sistema de control de inventario en Python que permite gestionar productos y sus cantidades disponibles utilizando un diccionario como estructura principal de datos.

Cada producto se almacena como una clave dentro del diccionario, mientras que la cantidad disponible se guarda como su valor correspondiente. Esta estructura permite acceder rápidamente a la información, actualizar el stock de manera dinámica y mantener un control organizado de los productos registrados.

El sistema funciona mediante un menú interactivo en consola que permite al usuario visualizar el inventario, actualizar cantidades, agregar nuevos productos y recibir alertas automáticas cuando el stock es bajo. Esta estructura interactiva facilita la gestión continua de los productos, ya que el usuario puede realizar múltiples operaciones sin reiniciar el programa.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar el uso de diccionarios para la gestión de datos.
- Aplicar funciones para modularizar el programa.
- Utilizar condicionales para validar productos y cantidades.
- Desarrollar un menú interactivo con bucles.
- Implementar alertas automáticas de bajo inventario.
- Simular el funcionamiento básico de un sistema de gestión de stock.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Condicionales (`if`, `elif`, `else`)
- Bucles `while`
- Bucles `for`
- Validación de datos
- Manejo de excepciones (`try` / `except`)
- Control de valores negativos

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `inventario` donde:
   - La clave representa el nombre del producto.
   - El valor representa la cantidad disponible.

2. El sistema muestra un menú con las siguientes opciones:
   - Mostrar inventario.
   - Actualizar stock.
   - Agregar producto.
   - Salir.

3. Cuando se actualiza el stock:
   - Se puede sumar o restar cantidad.
   - Se valida que el valor ingresado sea numérico.
   - El sistema evita cantidades negativas.

4. Si la cantidad de un producto es menor o igual al límite establecido, el sistema muestra una alerta de bajo inventario.

5. El programa se ejecuta continuamente hasta que el usuario decide salir.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```