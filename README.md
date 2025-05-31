# Interactive Streamlit Demo App

A comprehensive Streamlit web application that demonstrates the full range of interactive features available in Streamlit. This app serves as both a greeting application and a showcase of Streamlit's capabilities.

## Features

### User Input Components
- **Text Input**: Collect user names with instant feedback
- **Text Area**: Multi-line text input for longer messages
- **File Upload**: Support for text, CSV, JSON, and image files with preview functionality
- **Selection Widgets**: Dropdown menus, multi-select options, sliders, and number inputs
- **Date Picker**: Calendar interface for date selection

### Interactive Elements
- **Dynamic Buttons**: Responsive buttons with visual feedback and animations
- **Real-time Updates**: Content that changes based on user input
- **Random Content Generation**: Fun facts displayed on demand
- **Visual Feedback**: Success messages, balloons animation, and info displays

### File Handling
- **Multiple File Types**: Supports text files, CSV, JSON, and images (PNG, JPG, JPEG)
- **File Preview**: Automatic content display based on file type
- **File Information**: Shows filename, size, and type details

### Layout Features
- **Organized Sections**: Clear content organization with subheaders
- **Column Layout**: Multi-column button arrangement
- **Visual Separators**: Dividers for content organization
- **Responsive Design**: Works across different screen sizes

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

## What You Can Do

This demo app showcases various Streamlit capabilities:

### Personal Information
- Enter your name to receive a personalized greeting
- Share your thoughts in the text area for immediate feedback
- Select your favorite color from the dropdown menu
- Choose multiple hobbies from the selection list
- Use the slider to indicate your age
- Pick your lucky number with the number input
- Select your birthday using the date picker

### File Interactions
- Upload text files to see their content preview (limited to first 500 characters)
- Upload images (PNG, JPG, JPEG) to display them in the app
- Upload CSV or JSON files to view file details
- See file information including name, size, and type

### Interactive Features
- Click "Say Hello" to trigger a balloon animation and success message
- Use "Show Info" to display an information alert
- Try "Random Fact" to see interesting trivia that changes each time

### Learning Streamlit
This app demonstrates key Streamlit components:
- `st.text_input()` and `st.text_area()` for text collection
- `st.file_uploader()` for file handling with type restrictions
- `st.selectbox()` and `st.multiselect()` for option selection
- `st.slider()` and `st.number_input()` for numeric input
- `st.date_input()` for date selection
- `st.button()` with different styling and interactions
- `st.columns()` for layout organization
- `st.balloons()` for visual effects
- `st.success()`, `st.info()` for user feedback

Perfect for learning Streamlit development, testing deployment workflows, or as a foundation for more complex applications.