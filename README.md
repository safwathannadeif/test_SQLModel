CRUD FastApi SQLModel:
Installtions: pip install sqlmodel & pip install psycopg2 [postgresSQL]
When sqlmodel is installed, SQLAlchemy and Pydantic are automatically installed.
Files in this repository:
pkg cfg:
cfg_app.py: 		Toml application configuration

db_config.py: 		data class for postgres configuarion
cfg_app.py: 		reading the Tmol app configuration
pkg data: 		testing json data file for initial Apis testing.
			json file for reading, searching, and writing APIs. The src Apis are in test pkg. .
pkg model: 		hero model is the model from SQL Model Documentation: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/
			The hero model is used as guide.
			The stock model is the one created in this project.
pkg router: 		CRUD Apis routers configuration for here and stock models

SRC pkg: 		The main module app is hosted in this package.

How to run: 		use the test_SQLModel directory to run the server.
			uvicorn src.main:app    --host localhost --port 800 --reload
