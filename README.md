# PediaDose

## Overview

PediaDose is a comprehensive Flutter application that facilitates the management and dosing of medicines. It is primarily designed for pediatric use, allowing healthcare professionals and caregivers to search for medicines, check dosing information, and calculate dosages based on weight. The application is backed by a Django RESTful API, ensuring real-time data management and a reliable backend.

## Screenshots

![windowsOutput](https://github.com/divyesh1099/pediaDose/assets/65925922/11f0ab62-9f6a-46cb-82dc-ad1014f28ff9)

_The screenshot above may not be accessible directly if the URL is incorrect. Ensure that the image path in the GitHub repository is valid._

## Features

- **Backend (Django):**
  - Provides RESTful API endpoints for CRUD operations on medicine data.
  - Implements secure user authentication to protect sensitive information.
  - Utilizes a robust database for persistent storage of medicine records and types.

- **Frontend (Flutter):**
  - Offers cross-platform compatibility, running seamlessly on iOS, Android, Windows, and Web platforms.
  - Delivers a clean and intuitive user interface for easy navigation and medicine management.
  - Facilitates smooth communication with the Django backend for data retrieval and manipulation.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or later
- Pip (Python package manager)
- Flutter SDK for developing cross-platform applications

### Installation

1. **Clone the Repository**

   To get started with PediaDose, clone the repository to your local machine using the following command:

   ```sh
   git clone https://github.com/divyesh1099/pediaDose.git
   cd pediaDose
   ```

2. **Backend Setup**

   Move to the backend directory within the cloned repository:

   ```sh
   cd backend
   ```

   Here, install the necessary Python dependencies:

   ```sh
   pip install -r requirements.txt
   ```

   Once the dependencies are installed, apply the database migrations and start the Django development server:

   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

   Your backend should now be running locally and accessible for API requests.

3. **Frontend Setup**

   Open a new terminal window and navigate to the frontend directory:

   ```sh
   cd ../frontend
   ```

   Fetch the required Flutter packages:

   ```sh
   flutter pub get
   ```

   Now you can run the Flutter application with the following command:

   ```sh
   flutter run
   ```

   This will launch the app on any connected device or available emulator.

## Usage

The backend API is accessible at [medicines.pythonanywhere.com](http://medicines.pythonanywhere.com), where you can interact with the medicine database programmatically.

The Flutter application provides a graphical interface for all the backend functionality, allowing you to manage the medicine data more intuitively.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See the `CONTRIBUTING.md` for more detailed information on how to contribute.

## License

This project is licensed under the MIT License - see the `LICENSE` file in the repository for details.

## Contact

For any queries or further information, you may reach out to the maintainer:

Divyesh Vishwakarma - divyesh1099@gmail.com

Project Link: [https://github.com/divyesh1099/pediaDose](https://github.com/divyesh1099/pediaDose)

## Acknowledgements

- To all contributors and users of PediaDose, thank you for your support!
- Special thanks to all the healthcare professionals making informed decisions using PediaDose.
