## Project Structure

The project has the following structure:

```
.
chatgpt_scraper/
│── .venv/                # Virtual environment
│── src/
│   ├── scrape.py
│   ├── db.py
│   ├── config.py
│── .gitignore
│── LICENSE
│── README.md
│── requirements.txt

```

- `.gitignore`: Specifies files and directories to be ignored by git.
- `README.md`: Contains documentation of this app
- `requirements.txt`: Contains project dependencies and configuration.
- `scrape.py`: Python script for scrapping web.

## Dependencies

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

For development dependencies, run:

```sh
pip install -r dev-requirements.txt
```

The application will be available at `http://127.0.0.1:5000`.

## Running the Application

To run the application, use the following command:

```sh
python scrape.py
```

This will scrape web based on given url
