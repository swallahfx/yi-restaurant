# Yí Restaurant Website

A beautiful, modern restaurant website built with FastAPI and elegant frontend design. Features multilingual support (English/German), online reservations, menu showcase, and responsive design.

## Features

✨ **Elegant Design**: Modern, sophisticated design with ocean and seafood-inspired color palette
🌐 **Multilingual**: Complete English/German language support
📱 **Responsive**: Optimized for desktop, tablet, and mobile devices
🍽️ **Menu System**: Beautiful menu display with ordering functionality
📅 **Reservations**: Online reservation system with form validation
🖼️ **Gallery**: Interactive photo gallery with lightbox
📞 **Contact**: Contact forms and business information
⚡ **Performance**: Optimized for speed and accessibility

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Templates**: Jinja2
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Playfair Display, Crimson Text, Cormorant Garamond)

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone/Download the project files**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Open your browser**
   Visit `http://localhost:8000`

## Project Structure

```
yí-restaurant/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── templates/             # Jinja2 templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── menu.html         # Menu page
│   ├── about.html        # About page
│   ├── gallery.html      # Gallery page
│   └── contact.html      # Contact page
└── static/               # Static assets
    ├── css/
    │   └── main.css      # Main stylesheet
    ├── js/
    │   └── main.js       # Main JavaScript
    └── images/           # Image assets (placeholder)
```

## Language Support

The website supports English and German languages. Switch between languages using the language toggle in the navigation bar.

**Supported Languages:**
- English (en)
- German (de)

## Customization

### Restaurant Information
Edit the `RESTAURANT_DATA` dictionary in `main.py` to update:
- Restaurant name and description
- Contact information
- Opening hours
- Address

### Menu Items
Modify the `MENU_DATA` dictionary in `main.py` to update:
- Main dishes
- Side dishes
- Prices and descriptions
- Availability status

### Styling
- **Colors**: Edit CSS custom properties in `static/css/main.css`
- **Fonts**: Update font imports in `templates/base.html`
- **Layout**: Modify CSS Grid and Flexbox layouts

### Adding Images
Replace image placeholders by:
1. Adding real images to `static/images/`
2. Updating image sources in templates
3. Removing `.image-placeholder` classes

## Deployment

### Production Setup

1. **Install production server**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**
   ```bash
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

3. **Environment Variables** (Optional)
   ```bash
   export HOST=0.0.0.0
   export PORT=8000
   export DEBUG=False
   ```

### Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t yi-restaurant .
docker run -p 8000:8000 yi-restaurant
```

## Browser Support

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance Features

- Optimized CSS with custom properties
- Lazy loading for images
- Efficient animations with CSS transforms
- Minimal JavaScript bundle
- Responsive images
- Compressed assets ready

## Accessibility Features

- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatible
- High contrast ratios
- Focus indicators

## SEO Features

- Semantic HTML5 structure
- Meta tags for social sharing
- Structured data ready
- Fast loading times
- Mobile-friendly design
- Clean URLs

## Contributing

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is created for demonstration purposes. Please customize and use according to your needs.

## Support

For technical support or questions about customization, please refer to:
- FastAPI documentation: https://fastapi.tiangolo.com/
- Jinja2 documentation: https://jinja.palletsprojects.com/

---

**Yí Restaurant** - Authentic Seafood & Paella Experience
