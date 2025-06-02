# README.md

# Ecosystem IO Authentication

Authentication service for Ecosystem IO using Flask and Auth0.

## Project Structure

```
flask-auth0-app
├── src
│   ├── app.py
│   ├── templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── static
│   │   └── css
│   │       └── style.css
│   └── config.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd flask-auth0-app
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file with your Auth0 credentials:**
   ```env
   AUTH0_DOMAIN=your-domain.auth0.com
   AUTH0_CLIENT_ID=your-client-id
   AUTH0_CLIENT_SECRET=your-client-secret
   API_IDENTIFIER=your-api-identifier
   FLASK_SECRET_KEY=your-secret-key
   ```

5. **Run the application:**
   ```bash
   python src/app.py
   ```

6. **Access the application:**
   Open your browser and go to `http://localhost:5000`.

## Usage

- Navigate to the login page to authenticate using Auth0.
- After logging in, you will be redirected to the home page.
- Access the dashboard after successful authentication.

## Features

- Auth0 Integration
- User Authentication
- Protected Routes
- Profile Management

## License

This project is licensed under the MIT License.