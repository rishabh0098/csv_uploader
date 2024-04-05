# csv_uploader
## Starting with Docker

Make sure you have Docker installed on your machine. And allocated execution permissions to the `docker-run.sh` script.

After that, create a `.env` file in the `csv_uploader_backend` directory with the following content:

```bash
SECRET_KEY=<your-secret-key>
DEBUG=False
```

After that, run the `docker-run.sh` script.

```bash
sudo chmod +x docker-run.sh
sudo ./docker-run.sh
```

## Starting with Django and React

First launch the API server.

```bash
cd csv_uploader_backend
pip install -r requirements.txt
python manage.py runserver
```

The API server will be available at `http://localhost:8000/`.

Then launch the React client.

```bash
cd csv_uploader_frontend
yarn install
yarn start
```

The React client will be available at `http://localhost:3000/`. And you can upload csv files.

Assignment Document - https://docs.google.com/document/d/1XXorO2ba7w6ZFpAgsfisbwPEvLZzwSUhVliuhk-g2W0/edit

The database is modelled as mentioned in the document.

#### Assumption
Following assumptions we made while handling the CSV:
1. A person can have first name, middle name, last name only.
2. I have kept a City to State mapping in the code (CityToState.js) with few entries as of now, all the cities which part of the input CSV should be there for entries to be correctly populated in DB.
3. Every column where a class is being mentioned should have the word "class" in it (case insensitive).