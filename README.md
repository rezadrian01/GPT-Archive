## Project Structure

The project has the following structure:

```

GPT-Archive/
│── .venv/
│── src/
│   ├── static/
│   │   ├── js/
│   │   │   ├── script.js
│   ├── templates/
│   │   ├── index.html
│   ├── app.py
│   ├── db.py
│   ├── config.py
│   ├── scrape.py
│── .env.example
│── .gitignore
│── LICENSE
│── README.md
│── requirements.txt
│── tailwind.config.js

```

- `.venv/`: Directory for the virtual environment.
- `src/`: Contains the source code of the project.
  - `static/`: Directory for static files.
    - `js/`: Directory for JavaScript files.
      - `script.js`: JavaScript file for client-side scripting.
  - `templates/`: Directory for HTML templates.
    - `index.html`: Main HTML template.
  - `app.py`: Main application script.
  - `db.py`: Database configuration and interaction script.
  - `config.py`: Configuration settings for the application.
  - `scrape.py`: Python script for web scraping.
- `.env.example`: Example environment configuration file.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `LICENSE`: License information for the project.
- `README.md`: Contains documentation of this app.
- `requirements.txt`: Contains project dependencies and configuration.
- `tailwind.config.js`: Configuration file for Tailwind CSS.

## Dependencies

First, you need to create a virtual environment:

```sh
python -m venv .venv
```

Then, you need to activate the virtual environment:

```sh
source .venv/Scripts/activate
```

**To deactivate the virtual environment, you can type:**

```sh
deactivate
```

Then install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## Database Configuration

You need to turn on the MySql Server and then create a new database

## Environment Variables Configuration

Copy .env.example file and rename it to .env

```sh
cp .env.example .env
```

Then, replace variable value with your database configuration

## Running the Application

To run the application, use the following command:

```sh
python src/app.py
```

This will turn on the flask server and you can visit it on <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>
