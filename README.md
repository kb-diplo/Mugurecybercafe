# Mugure Cyber Services - Professional Website

**Location**: Kamwangi Town, Gatundu North, Kiambu County, Kenya  
**Contact**: 0728 031 274 | tingzlarry@gmail.com

A comprehensive Django-powered website for Mugure Cyber Services, the premier cyber cafe in Gatundu North. This professional web application provides complete business management capabilities with a modern, responsive Bootstrap interface.

## ✨ Features

### Core Functionality
| Feature | Status | Description |
|---------|--------|-------------|
| ✅ **Website Content Management** | **COMPLETED** | Full Django admin interface for editing all website content |
| ✅ **Services Management** | **COMPLETED** | Add/edit cyber cafe services (KRA, eCitizen, printing, etc.) |
| ✅ **Blog System** | **COMPLETED** | Create announcements, tips, and updates |

- **Backend**: Django 4.2.23
- **Frontend**: Bootstrap 5.3.3, HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Static Files**: WhiteNoise for production
- **Security**: Django-axes for brute force protection
- **Python Version**: 3.8+ (Recommended: 3.11)

## 📋 Services Offered

### Online Services
- Government platform services (KRA, eCitizen, NTSA)
- Online applications and registrations
- Digital certificate downloads
- Tax filing assistance

### Cyber Services  
- Internet access and browsing
- Email setup and management
- Social media assistance
- Online shopping guidance

### Document Services
- Professional printing and scanning
- Document typing and formatting
- CV and resume creation
- Business card design

### Educational Support
- Research assistance
- Online course enrollment
- Digital literacy training
- Student portal access

## 🏗️ Project Architecture

```
mugurecyber/
├── cafee83/                 # Main project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── core/                   # Core app (home, about, contact)
│   ├── models.py          # Site settings model
│   ├── views.py           # Core page views
│   └── context_processors/ # Global template context
├── services/               # Services management app
│   ├── models.py          # Service and category models
│   ├── views.py           # Service listing views
│   └── admin.py           # Admin interface
├── blog/                   # Blog and news app
│   ├── models.py          # Blog post model
│   ├── views.py           # Blog views
│   └── admin.py           # Blog admin
├── users/                  # Custom user management
│   ├── models.py          # Custom user model
│   └── admin.py           # User admin
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── core/              # Core app templates
│   ├── services/          # Service templates
│   └── blog/              # Blog templates
├── static/                 # Static files
│   ├── css/               # Custom stylesheets
│   └── mugurecyberserviceslogo.png
├── requirements.txt        # Python dependencies
└── manage.py              # Django management script
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (Recommended: Python 3.11)
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/kb-diplo/Mugurecybercafe.git
cd Mugurecybercafe
```

2. **Create virtual environment:**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Load sample data (optional):**
```bash
python manage.py shell < sample_data.py
```

7. **Collect static files:**
```bash
python manage.py collectstatic
```

8. **Run development server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 🎨 Key Features Implemented

### Enhanced UI/UX
- **Fixed Navigation**: Stays visible while scrolling
- **Service Cards**: Beautiful gradient headers with large icons
- **Back-to-Top Button**: Smooth scroll functionality
- **Service Icons Preview**: Shows service icons beside category titles
- **Social Sharing**: Functional sharing buttons for blog posts

### Admin Features
- **Content Management**: Easy-to-use admin interface
- **Service Categories**: Organize services by category
- **Blog Management**: Draft/publish workflow
- **User Management**: Custom user profiles

### Mobile Optimization
- **Responsive Design**: Works perfectly on all devices
- **Mobile-First**: Optimized for mobile users
- **Touch-Friendly**: Large buttons and easy navigation

## 🌍 Deployment

### PythonAnywhere Deployment

**Python Version Required**: Python 3.11 (recommended for PythonAnywhere)

#### Step-by-Step Deployment Guide:

1. **Create PythonAnywhere Account**
   - Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
   - Choose appropriate plan (Beginner plan supports custom domains)

2. **Upload Code**
   ```bash
   # In PythonAnywhere console
   git clone https://github.com/kb-diplo/Mugurecybercafe.git
   cd Mugurecybercafe
   ```

3. **Create Virtual Environment**
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Configure Database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic
   ```

5. **Configure Web App**
   - Go to Web tab in PythonAnywhere dashboard
   - Create new web app
   - Choose Manual configuration
   - Select Python 3.11
   - Set source code directory: `/home/yourusername/Mugurecybercafe`
   - Set working directory: `/home/yourusername/Mugurecybercafe`

6. **Configure WSGI File**
   ```python
   import os
   import sys
   
   path = '/home/yourusername/Mugurecybercafe'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'cafee83.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

7. **Configure Static Files**
   - URL: `/static/`
   - Directory: `/home/yourusername/Mugurecybercafe/staticfiles/`

8. **Environment Variables**
   - Set `DEBUG=False` in production
   - Configure `ALLOWED_HOSTS`
   - Set up database credentials if using PostgreSQL

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL (optional)
- [ ] Configure email backend
- [ ] Set up SSL certificate
- [ ] Configure domain name
- [ ] Set up monitoring

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Code Quality
```bash
# Format code
black .

# Sort imports
isort .

# Check code style
flake8 .
```

### Creating Sample Data
```bash
python manage.py shell < sample_data.py
```

## 📞 Contact Information
- **Social Media**: WhatsApp integration, social media links
- **Contact Forms**: Professional inquiry handling system

## Security Features

- **User Authentication**: Secure login/logout system
- **CSRF Protection**: Built-in Django security
- **Input Validation**: Form validation and sanitization
- **Admin Access Control**: Role-based permissions

## Support

For technical support or business inquiries:
- **Phone**: 0728 031 274
- **Email**: tingzlarry@gmail.com
- **WhatsApp**: Available via website floating button

---

** 2025 Mugure Cyber Services. All rights reserved.**  
*This software is proprietary and confidential. Unauthorized copying, distribution, or modification is strictly prohibited.*


## 🚫 **IMPORTANT: This is NOT Open Source Software**

**PROPRIETARY & CONFIDENTIAL - ALL RIGHTS RESERVED**

This is a **commercial proprietary software** developed exclusively for Mugure Cyber Services. This project is **NOT open source** and is protected under strict copyright laws.

**UNAUTHORIZED USE PROHIBITED** - Copying, distribution, modification, or use without explicit written permission is strictly forbidden and may result in legal action.

For licensing or business inquiries only: tingzlarry@gmail.com

---

## 👨‍💻 **Built By**

**Lawrence Mbugua Njuguna**  
Full-Stack Developer & Software Engineer  
Portfolio: Available on request

*Professional web development services for businesses in Kenya and beyond.*
