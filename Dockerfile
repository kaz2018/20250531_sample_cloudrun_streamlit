# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY pyproject.toml uv.lock ./

# Install uv for faster dependency management
RUN pip install uv

# Install dependencies
RUN uv sync --frozen

# Copy application files
COPY . .

# Create .streamlit directory and copy config
RUN mkdir -p .streamlit
COPY .streamlit/config.toml .streamlit/

# Expose port 8080
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/_stcore/health || exit 1

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port", "8080"]