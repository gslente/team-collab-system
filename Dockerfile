### BACKEND SETUP
# Use an official Python runtime as a parent image
FROM python:latest AS backend

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /usr/src/app/team-collab-system

# install python requirements
RUN pip install --upgrade pip

# copy code files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Bash file
ENTRYPOINT [ "/usr/src/app/team-collab-system/entrypoint.sh" ]