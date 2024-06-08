# use an offical pytrhon runtime as a base image
from python:3.9-slim

#Set the working directory in the container
WORKDIR /app

# Copy the dependencies file into the container at /app
COPY requirements.txt .

# Print the contents of requirements.txt for debugging
RUN cat requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt --verbose
# Copy teh rest of the application code, into the container
COPY . .

# Expose ports
EXPOSE 5600
EXPOSE 5601

# Command to run the Flask application
CMD ["sh", "-c", "python start_ctrlService.py & python start_dataService.py"]