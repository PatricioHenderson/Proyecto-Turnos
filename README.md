# Proyecto-Turnos

Proyecto realizado para que un usuario pueda loguearse en el sistema y agendar un turno.

# El Diagrama de flujo es el siguiente:

![Screenshot](https://github.com/PatricioHenderson/Proyecto-Turnos/blob/main/assets/Captura.JPG)

Al ingresar el usuario verá la siguiente pantalla:
![Screenshot](https://github.com/PatricioHenderson/Proyecto-Turnos/blob/main/assets/signup.JPG)

En la cual debera crear un usuario, que será almacenado en una base de datos SQLAlchemy, guardando las contraseñas bajo el protocolo "sha256".
En caso de ya existir el usuario, no le dara la posbilidad de volver a crear otro usuario con el mismo correo electronico

Si es un usuario que ya posee una cuenta, puede acceder directamente a esta pantalla y loguearse.

Por último puede cerrar sesión, o Acceder a la sección Turnos (solo si ya se encuentra logueado) y agendar un turno.

![Screenshot](https://github.com/PatricioHenderson/Proyecto-Turnos/blob/main/assets/turnos.JPG)
