
# Arduino and Webcam Security with Google Drive Integration

## Overview

This project aims to enhance security by integrating an Arduino-based motion sensor system with a webcam and Google Drive. When the motion sensor is triggered, the Arduino communicates with an application that instructs the webcam to capture a picture. The captured image is then automatically uploaded to your Google Drive account using PyDrive.

## Setup Process

### 1. Project Creation on Google Cloud Console

- Go to [Google Cloud Console](https://console.cloud.google.com/cloud-resource-manager) and create your own project.
- Search for 'Google Drive API,' select the entry, and enable it.
- Navigate to 'Credentials,' click 'Create Credentials,' and select 'OAuth client ID.'
- Configure the consent screen by selecting 'Web application' as the application type and entering the necessary information.
- Download the JSON file containing authentication information, rename it to "client_secrets.json," and place it in your working directory.

### 2. Automatic and Custom Authentication with settings.yaml

- Complete the first five steps mentioned above and download the JSON file.
- Edit the "client_id" and "client_secret" in the "Sample settings.yaml" file with the information from your downloaded JSON file.
- This enables a custom authentication flow, preventing repetitive authentication prompts.

## Usage

1. Install required libraries and navigate to the `app` directory:

    ```bash
    cd app
    pip install -r requirements.txt
    ```

2. Execute the script to start the motion sensor system:

    ```bash
    python listener.py
    ```

Now, the system is fully automated. The motion sensor triggers the webcam, and the captured images are seamlessly uploaded to your Google Drive account without the need for repeated authentication.



## License

This project is licensed under the [MIT License](LICENSE).
