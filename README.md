# 📚 DSC Bookstore – Students Digital Library

A modern and responsive digital library web application built with **Django**. DSC Bookstore allows students to explore and access digital books with a simple, intuitive interface.

---

## 🚀 Features

- 🧾 User login (no password required)
- 🔍 Search books by title (real-time filtering)
- 📥 PDF download access
- 🖼️ Book cover image previews
- 📱 Fully responsive UI with animated gradient backgrounds
- 🔐 Session-based login and logout
- 📂 Admin panel to manage book uploads (PDFs and cover images)

---

## 💻 Tech Stack

- **Backend**: Django 5.1.6
- **Frontend**: HTML5, CSS3 (custom), JavaScript (vanilla)
- **Database**: SQLite3 (default for dev)
- **Storage**: Media upload handling for book images & PDFs

---

## 📁 Project Structure

```bash
DSC_Bookstore_Django/
├── bookstore/               # Main app
│   ├── templates/
│   │   └── bookstore/
│   │       ├── login.html
│   │       └── home.html
│   ├── static/              # (optional for future assets)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── DSCBookstore/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
└── manage.py
````

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Avnish-web/DSC_Bookstore_Django.git
cd DSC_Bookstore_Django
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:

```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)



---

🔐 Admin Login (For Testing)
You can log in to the admin panel at:

📍 http://127.0.0.1:8000/admin

Credentials:

Username: avnish

Password: avnish

⚠️ For production, change this to a strong, secure password.



## 📤 Uploading Books (Admin Panel)

1. Login to the Django admin 
2. Add a new `Book` entry with:

   * Title
   * Author
   * PDF file
   * Cover image
3. Save and preview it on the home page

---

## 📷 Screenshots
<img width="1440" height="900" alt="image" src="https://github.com/user-attachments/assets/d1c1f95d-0a99-4068-a0f3-a5221ededa3d" />
<img width="1440" height="900" alt="image" src="https://github.com/user-attachments/assets/c6904df0-8ea6-4937-85ef-be663b5787bc" />

---

## 🧪 Future Improvements

* Category-based book filtering
* Book rating system
* Email-based registration (optional)
* Advanced PDF preview (in-browser)
* Deployment (e.g., on Heroku or Vercel + PostgreSQL)

---

## 🤝 Contributing

Pull requests and issues are welcome!
If you find a bug or want to request a feature, feel free to open an issue.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Avnish Sharma**
GitHub: [@Avnish-web](https://github.com/Avnish-web)
