# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY word_freq_analysis.py .
COPY random_paragraphs.txt .
COPY requirements.txt .

# Install NLTK and download necessary resources
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader stopwords punkt

# Install any other dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script when the container starts
CMD ["python", "word_freq_analysis.py"]
