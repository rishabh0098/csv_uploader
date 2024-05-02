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

The API server will be available at `http://127.0.0.1:8000/api/csv_uploader_api/`.

Then launch the React client.

```bash
cd csv_uploader_frontend
yarn install
yarn start
```

The React client will be available at `http://localhost:3000/`. And you can upload csv files.
