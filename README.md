# Moral Games Web

¡Bienvenido a Trivia Quest, el emocionante mundo de desafíos intelectuales! Sumérgete en una experiencia única llena de preguntas intrigantes y opciones cautivadoras.

En Trivia Quest, no solo encontrarás preguntas, sino una aventura para poner a prueba tu conocimiento y desbloquear el genio que llevas dentro. Prepárate para explorar el fascinante universo de opciones A, B, C y D, donde cada elección te acerca más a la victoria.

¡Únete a nosotros y eleva tu ingenio con cada pregunta! La diversión comienza aquí, en Trivia Quest, donde el aprendizaje se fusiona con la emoción. ¡Que comience el desafío!. [Trivia Quest](https://trivia-quest-17c2d37d8833.herokuapp.com/).

## Obtener los archivos estáticos

Antes de desplegar la aplicación en Heroku, asegúrate de recopilar los archivos estáticos necesarios. Ejecuta el siguiente comando:

```bash
python manage.py collectstatic
```

## Despliegue

A continuación, se detallan los pasos para desplegar Trivia Quest en un entorno de producción. 

## Despliegue en Heroku

Para desplegar Trivia Quest en Heroku, asegúrate de tener una cuenta en [Heroku](https://www.heroku.com/).

### Configuración previa:

1. **Crear una cuenta en Heroku:**
    - Si aún no tienes una cuenta, regístrate en [Heroku](https://signup.heroku.com/).

2. **Instalar el Heroku CLI:**
    - Descarga e instala el [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

3. **Iniciar sesión en Heroku:**
    - Ejecuta el siguiente comando e ingresa tus credenciales:
      ```bash
      heroku login
      ```

### Despliegue:

1. **Crear una nueva aplicación en Heroku:**
    ```bash
    heroku create nombre-unico-de-tu-aplicacion
    ```

2. **Configurar variables de entorno:**
    - Configura las variables de entorno necesarias en tu aplicación Heroku utilizando el comando `heroku config:set`.

3. **Desplegar la aplicación:**
    ```bash
    git push heroku master
    ```

4. **Aplicar migraciones en Heroku:**
    ```bash
    heroku run python manage.py migrate
    ```

4. **Configurar la Base de Datos en Heroku:**
Utiliza el siguiente comando para agregar una base de datos PostgreSQL como add-on en Heroku:
    ```bash
    heroku addons:create heroku-postgresql:mini
    ```

5. **Abrir la aplicación en el navegador:**
    ```bash
    heroku open
    ```

6. **¡Listo!**

    Tu aplicación Trivia Quest ahora está desplegada en Heroku.