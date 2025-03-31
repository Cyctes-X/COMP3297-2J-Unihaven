# COMP3297-2J-Unihaven

## **Overview**
UniHaven is a web-based accommodation platform designed specifically for HKU students, CEDARS staff, and property owners. It facilitates streamlined searching, booking, and management of off-campus accommodations. The project is built using **Django** and follows role-based access control to provide tailored features for each user type.

---

## **Features Implemented**
### **1. User Management**
- **Custom User Model**:
  - Roles: `STUDENT` (HKU Member), `CEDARS` (CEDARS Specialist), `OWNER` (Property Owner).
  - Implemented using Django's `AbstractUser`.
- **User Registration and Login**:
  - **Registration**: Allows users to sign up with a role and credentials.
  - **Login**: Authenticates users and returns a personalized welcome message.

### **2. Accommodation Management**
- **Accommodation Model**:
  - Stores information about accommodations, including:
    - `name`, `address`, `price`, `availability`, `number_of_beds`, and `distance_to_hku`.
- **Admin Integration**:
  - CEDARS staff can manage accommodations through the Django admin interface.

### **3. API Endpoints**
- **User APIs**:
  - **Register**: `/users/register/` (POST)
  - **Login**: `/users/login/` (POST)
- **Admin Panel**:
  - Accessible at `/admin/`.

---

## **Project Structure**
```
unihaven_2j/
│
├── accommodations/             # App for managing accommodations
│   ├── admin.py                # Admin integration for accommodations
│   ├── apps.py                 # Configuration for accommodations app
│   ├── models.py               # Accommodation model
│   ├── tests.py                # Placeholder for accommodation tests
│   ├── views.py                # Placeholder for accommodation views
│   └── urls.py                 # Endpoint configurations for accommodations
│
├── users/                      # App for managing users
│   ├── admin.py                # Admin integration for custom users
│   ├── apps.py                 # Configuration for users app
│   ├── models.py               # Custom User model
│   ├── serializers.py          # Serializer for user registration
│   ├── tests.py                # Placeholder for user tests
│   ├── views.py                # User registration and login APIs
│   └── urls.py                 # Endpoint configurations for user APIs
│
├── unihaven_2j/                # Main project folder 
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── __init__.py
│
└── db.sqlite3                  # SQLite database (for development)

```

---

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd COMP3297-2J-Unihaven
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv unihaven_env
source unihaven_env/bin/activate  # On Windows: unihaven_env\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**
```bash
python manage.py createsuperuser
```

### **6. Run the Development Server**
```bash
python manage.py runserver
```

### **7. Access the Application**
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **User APIs**: 
  - Registration: `http://127.0.0.1:8000/users/register/`
  - Login: `http://127.0.0.1:8000/users/login/`

---

## **Next Steps**
1. Implement search functionality for accommodations.
2. Add role-based permissions to restrict access to certain endpoints.
3. Build comprehensive tests for user and accommodation functionality.
4. Enhance UI (if applicable) and start integrating frontend components.

---

