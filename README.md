# elektra-back
Proceso para creación y redención de tarjetas


<!-- TODO: PROJECT LOGO --> ![Logo Transparente](https://user-images.githubusercontent.com/72032602/189195290-134ad579-56f8-466b-9369-2b4418a507b0.png)
<br />
<p align="center">

  <h1 align="center">Tarjetas Backend</h1>

</p>


### Built With

* [Django](https://docs.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Poetry](https://python-poetry.org/)



<!-- GETTING STARTED -->
## Getting Started

To start contributing to our work, please follow the intructions below.

### Prerequisites

* Python

  ```sh
  pyenv install 3.8.6
  ```
* Poetry

  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```

### Installation


1. Clone the repo

   ```sh
   git clone https://github.com/RobertoAR9/elektra-back.git
   ```

2. Set up the recommended Python version (^3.6.8)

   ```sh
   pyenv local 3.8.6
   ```

3. Install packages with poetry
   
   ```sh
   poetry install
   ```
   
4. Install pre-commit hooks

   ```sh
   pre-commit install
   ```

5. Enter your credentials db in a `.env` from `.env.sample`

   ```.env
   MONGO_DB='ENTER NAME_DB'
   MONGO_USER='ENTER USER_DB'
   MONGO_PWD='ENTER PWD_DB'
   MONGO_PORT='ENTER PORT_DB'
   MONGO_HOST='ENTER HOST_DB'
   ```

6. Run the migrations

   ```sh
   python manage.py migrate
   ```


8. Load fixture to authentication or createsuperuser

    ```sh
    python manage.py loaddata apps/cards/fixtures/user.json
    ```

9. Run the server

   ```sh
   python manage.py runserver
   ```


<!-- USAGE EXAMPLES -->
## Docs

_Please refer to the [Documentation](https://speeding-comet-286773.postman.co/workspace/My-Workspace~232e4395-f21c-4add-8d66-9bcd83bc8e2a/collection/32600932-e30cd0b1-aa42-4fcc-b2d6-08689e1a972a?action=share&creator=32600932&active-environment=32600932-5ccea480-e880-4940-a402-582c235b63d0)_


1. Modeling DB

    ```sh
    {
        "email" : "test@gmail.com",
        "clabe" : "09876123",
        "properties" : {
            "transmitter" : "Sucursal", //Sucursal o Línea
            "type" : "Física", //Física o Digital
            "amount": 2000,
            "balance": 1500,
            "currency" : "MXN",
            "expiration_date" : "2020-10-13 03:30:00" //Required False
        }
    }
    ```

2. Access to the administration panel
_Link [Panel-Administration](http://127.0.0.1:8000/admin/cards/)_


3. Credentials to acces admin panel and authentication api
  username: "user-test"
  pass: "prueba123."


<!-- CONTACT -->
## Contact

Roberto Rodriguez - robertoar0309@gmail.com

