# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy environment/requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Set default command (optional)
CMD ["sleep", "infinity"]
