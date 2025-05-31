# Greeting App

A simple Streamlit web application that displays a friendly greeting message.

## Features

- Clean, centered layout with a welcoming "Hello!" message
- Responsive design that works on different screen sizes
- Simple and intuitive user interface

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Streamlit

### Installation

1. Install the required dependencies:
   ```bash
   pip install streamlit
   ```

2. Run the application:
   ```bash
   streamlit run app.py --server.port 8080
   ```

3. Open your browser and navigate to `http://localhost:8080`

## Project Structure

```
├── .streamlit/
│   └── config.toml      # Streamlit server configuration
├── app.py               # Main application file
├── README.md            # Project documentation
└── pyproject.toml       # Project dependencies
```

## Configuration

The app is configured to run on port 5000 with the following server settings:
- Headless mode enabled
- Accessible from all network interfaces (0.0.0.0)
- Optimized for deployment

## Deployment

This application is ready for deployment on cloud platforms that support Streamlit applications. The server configuration is already set up for production use.

## Usage

Simply visit the application URL to see the greeting message. The app displays:
- A welcoming "Hello!" title with a wave emoji
- A friendly welcome message
- An encouraging note to have a wonderful day

Perfect for testing deployment setups or as a starting point for more complex Streamlit applications.