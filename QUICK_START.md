# 🍽️ Yí Restaurant Website - Quick Setup Guide

## What's Included
✅ Complete restaurant website with German/English support
✅ Beautiful, responsive design
✅ Menu system with ordering functionality  
✅ Online reservation system
✅ Gallery, about, and contact pages
✅ FastAPI backend with Jinja2 templates

## 🚀 Quick Start (3 Steps)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python main.py
```
OR on Unix/Mac/Linux:
```bash
./start.sh
```

### Step 3: Open Your Website
Visit: **http://localhost:8000**

## 🌐 Language Support
- English: `http://localhost:8000?lang=en`  
- German: `http://localhost:8000?lang=de`

## 📁 File Structure
```
yi-restaurant/
├── main.py              # FastAPI app
├── requirements.txt     # Dependencies
├── start.sh            # Launch script
├── README.md           # Full documentation
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   ├── index.html     # Homepage
│   ├── menu.html      # Menu page
│   ├── about.html     # About page
│   ├── gallery.html   # Gallery page
│   └── contact.html   # Contact page
└── static/            # CSS, JS, Images
    ├── css/main.css   # Main stylesheet
    └── js/main.js     # JavaScript
```

## 🎨 Customization
- **Restaurant Info**: Edit `RESTAURANT_DATA` in `main.py`
- **Menu Items**: Edit `MENU_DATA` in `main.py`  
- **Styling**: Modify `static/css/main.css`
- **Images**: Add photos to `static/images/`

## ☁️ Production Deployment
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 🆘 Need Help?
Check `README.md` for complete documentation and troubleshooting.

---
**Ready to launch your beautiful restaurant website!** 🚀
