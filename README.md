## Installation

1. Install the dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Launching the Application

### Launching the Web Application

1. Navigate to the app directory:

    ```bash
    cd app
    ```

2. Launch the application using Uvicorn:

    ```bash
    uvicorn main:app --reload --port 8000
    ```

### Launching the API

1. Navigate to the API directory:

    ```bash
    cd api
    ```

2. Launch the API using Uvicorn:

    ```bash
    uvicorn api:app --reload --port 8001
    ```

## Video

https://youtu.be/myFPFtQ4FME

