# 🚌 Bus Booking Management System

A web-based **Bus Booking Management System** developed using Django and Python. This application allows users to search for available buses, enter passenger details, book tickets, and download booking tickets in PDF format.

The main objective of this project is to simplify the bus booking process through a user-friendly web application.

## 🚀 Features

- **User Authentication** – User registration and login functionality.
- **Bus Search** – Search for available buses based on source and destination.
- **Bus Availability** – View available buses based on search details.
- **Ticket Booking** – Enter passenger details and book bus tickets.
- **PDF Ticket Download** – Generate and download booking tickets in PDF format.
- **User-Friendly Interface** – Simple and responsive web interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite3 | Database |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap | UI Design |

## 📂 Project Structure

```text
Django_Project/
│
├── manage.py
├── db.sqlite3
│
├── busbooking/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── login.html
│   ├── create_user.html
│   ├── busbooking.html
│   └── ticket.html
│
├── static/
│   └── css/
│
└── requirements.txt
```

*Note: Adjust the folder structure above to match your actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git https://github.com/rohithrohith11/Bus_Booking_Management_System.git
```

### 2. Navigate to the Project Folder

```bash
cd [change the working directory according to your work space]
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔮 Future Enhancements

The following features are planned for future development:

- **Online Payment Gateway** – Integrate secure online payment functionality.
- **AI Chatbot Integration** – Implement an intelligent chatbot to assist users with booking-related queries.
- **Admin Dashboard** – Provide administrative features for managing buses, bookings, and users.
- **Seat Selection** – Allow passengers to select their preferred seats.
- **Booking History** – Enable users to view their previous bookings.

## 🎯 Project Objectives

- To develop a web-based bus booking application.
- To understand Django's MVT architecture.
- To implement database operations using SQLite3.
- To gain practical experience in backend and frontend development.
- To develop a real-world application using Python and Django.

## 👨‍💻 Developer

**ROHITH S**

- GitHub: https://github.com/rohithrohith11
- LinkedIn: [Connect with ME!!!] (linkedin.com/in/rohith-s-183382289)

---

⭐ If you find this project interesting, feel free to explore the repository!

**Thank you for visiting my project!**
