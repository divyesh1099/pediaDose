# PediaDose

## Overview

This project consists of a Medicines Management Application with a Django-powered backend hosted at [medicines.pythonanywhere.com](http://medicines.pythonanywhere.com) and a Flutter-based frontend. The application is designed to streamline the process of managing medicine-related data, offering an intuitive interface for users to interact with the system.

## Screenshots

![windowsOutput](https://github.com/divyesh1099/pediaDose/assets/65925922/11f0ab62-9f6a-46cb-82dc-ad1014f28ff9)

## Features

- **Backend (Django)**
  - RESTful API endpoints to manage medicine data.
  - Secure user authentication.
  - Database integration for storing medicine and related data.

- **Frontend (Flutter)**
  - Cross-platform app support (iOS and Android).
  - User-friendly interface for viewing and managing medicines.
  - Seamless integration with the Django backend.

## Getting Started

### Prerequisites

- Python 3.10 or above
- Pip (Python package manager)
- Flutter SDK

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/divyesh1099/pediaDose.git
   cd pediaDose
   ```

2. **Backend Setup**

   Navigate to the backend directory:

   ```bash
   cd pediaDose_backend
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Run migrations and start the Django server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup**

   Navigate to the frontend directory:

   ```bash
   cd ../pediaDose_frontend
   ```

   Run the Flutter application:

   ```bash
   flutter run
   ```

## Usage

- The backend API can be accessed via [medicines.pythonanywhere.com](http://medicines.pythonanywhere.com).
- The Flutter app can be used to interact with the backend through a graphical interface.

## Contributing

You can see the `CONTRIBUTING.md`

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Divyesh Vishwakarma - divyesh1099@gmail.com

Project Link: [https://github.com/divyesh1099/pediaDose](https://github.com/divyesh1099/pediaDose)
