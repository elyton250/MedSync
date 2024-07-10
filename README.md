# MedSync

![MedSync Logo](path_to_logo_image) 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

MedSync is an advanced Electronic Health Record (EHR) system designed to centralize and manage patient data efficiently. It provides seamless integration for medical records, ensuring that healthcare providers can access patient information quickly and securely. With MedSync, hospitals and clinics can enhance patient care, streamline workflows, and improve data accuracy.

## Features

- **Centralized Data Management**: Store and manage patient records in one centralized database.
- **Patient Management**: Add, update, and delete patient information.
- **Doctor Management**: Manage doctor profiles and specialties.
- **Department Management**: Organize hospital departments and their respective details.
- **Medical History**: Record and track patients' medical history.
- **Secure Access**: Ensure data security with robust authentication and authorization mechanisms.
- **User-Friendly Interface**: Intuitive UI for easy navigation and operation.

## Technologies

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Frontend**: HTML, CSS, JavaScript, react
- **Environment Management**: python-dotenv
- **Others**:Nginx

## Installation

### Prerequisites

- Python 3.8+
- MongoDB
- pip (Python package installer)

### Steps

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/medsync.git
    cd medsync
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    - Create a `.env` file in the project root directory and add the following:
      ```
      MONGODB_DB=medsync
      MONGODB_HOST=localhost
      MONGODB_PORT=27017
      ```

5. **Run the application**
    ```sh
    flask run
    ```

## Usage

Once the application is up and running, you can access it at `http://localhost:5000`. You can use the provided UI to navigate through the different functionalities, including patient management, doctor management, department management, and recording medical histories.

## API Endpoints

### Patient Endpoints

- `GET /patients`: Retrieve all patients
- `GET /patients/<id>`: Retrieve a patient by ID
- `POST /patients`: Add a new patient
- `PUT /patients/<id>`: Update a patient by ID
- `DELETE /patients/<id>`: Delete a patient by ID

### Doctor Endpoints

- `GET /doctors`: Retrieve all doctors
- `GET /doctors/<id>`: Retrieve a doctor by ID
- `POST /doctors`: Add a new doctor
- `PUT /doctors/<id>`: Update a doctor by ID
- `DELETE /doctors/<id>`: Delete a doctor by ID

### Department Endpoints

- `GET /departments`: Retrieve all departments
- `GET /departments/<id>`: Retrieve a department by ID
- `POST /departments`: Add a new department
- `PUT /departments/<id>`: Update a department by ID
- `DELETE /departments/<id>`: Delete a department by ID

### Medical History Endpoints

- `GET /medical_histories`: Retrieve all medical histories
- `GET /medical_histories/<id>`: Retrieve a medical history by ID
- `GET /medical_histories/patient/<patient_id>`: Retrieve medical histories by patient ID
- `POST /medical_histories`: Add a new medical history
- `PUT /medical_histories/<id>`: Update a medical history by ID
- `DELETE /medical_histories/<id>`: Delete a medical history by ID

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or issues, please contact [yourname](mailto:yourname@example.com).
