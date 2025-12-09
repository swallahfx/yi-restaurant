from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path
import os
import secrets
import json
from datetime import datetime
from typing import Optional
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./restaurant.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="Yí Restaurant", description="Authentic Seafood & Paella Experience")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String)
    date = Column(String)
    time = Column(String)
    guests = Column(Integer)
    message = Column(Text, nullable=True)
    lang = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

security = HTTPBasic()


# Reservation handler that saves to the database
@app.post("/reservation")
async def make_reservation(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    date: str = Form(...),
    time: str = Form(...),
    guests: int = Form(...),
    message: Optional[str] = Form(None),
    lang: str = Form("en")
):
    # Save to database
    db = SessionLocal()
    reservation = Reservation(
        name=name,
        email=email,
        phone=phone,
        date=date,
        time=time,
        guests=guests,
        message=message,
        lang=lang
    )
    db.add(reservation)
    db.commit()
    db.close()

    return RedirectResponse(
        url=f"/?lang={lang}&reservation=success",
        status_code=303
    )



# Setup templates
templates = Jinja2Templates(directory="templates")

# Restaurant data
RESTAURANT_DATA = {
    "name": "Yí Restaurant",
    "tagline": {
        "en": "Authentic Seafood & Paella Experience",
        "de": "Authentische Meeresfrüchte & Paella Erlebnis"
    },
    "description": {
        "en": "Discover the finest seafood cuisine with our signature paellas, fresh fish, and traditional Spanish flavors in an elegant atmosphere.",
        "de": "Entdecken Sie die feinste Meeresfrüchteküche mit unseren charakteristischen Paellas, frischem Fisch und traditionellen spanischen Aromen in eleganter Atmosphäre."
    },
    "address": "Yí Restaurant Cerca de Jorge Ramírez de Arellano, 9 C. Félix Arce Lugos San German, 00683",
    "phone": "+34 (787) 413-0224",
    "email": "info@yirestaurant.com",
    "hours": {
        "en": {
            "monday": "Closed",
            "tuesday": "6:00 PM - 11:00 PM",
            "wednesday": "6:00 PM - 11:00 PM", 
            "thursday": "6:00 PM - 11:00 PM",
            "friday": "6:00 PM - 11:30 PM",
            "saturday": "1:00 PM - 11:30 PM",
            "sunday": "1:00 PM - 10:00 PM"
        },
        "de": {
            "monday": "Geschlossen",
            "tuesday": "18:00 - 23:00",
            "wednesday": "18:00 - 23:00",
            "thursday": "18:00 - 23:00", 
            "friday": "18:00 - 23:30",
            "saturday": "13:00 - 23:30",
            "sunday": "13:00 - 22:00"
        }
    }
}

MENU_DATA = {
    "main_dishes": {
        "en": [
            {
                "name": "Salmon",
                "price": 28,
                "description": "8oz salmon fillet sautéed with olive oil, Caribbean spices and lemon zest",
                "availability": "Available"
            },
            {
                "name": "Sea Bream",
                "price": 28,
                "description": "10oz fish fillet sautéed with olive oil and fresh herbs",
                "availability": "Subject to availability"
            },
            {
                "name": "Cod Fillet",
                "price": 28,
                "description": "8oz cod fillet sautéed with fresh herbs and aromatics",
                "availability": "Subject to availability"
            },
            {
                "name": "Sea Bass (per pound)",
                "price": 0,
                "description": "Sea bass fillets",
                "availability": "Subject to availability"
            },
            {
                "name": "Louisianna Paella",
                "price": 28,
                "description": "Haitian paella with chicken, sausage, shrimp, prawns",
                "availability": "Available"
            }
        ],
        "de": [
            {
                "name": "Lachs",
                "price": 28,
                "description": "220g Lachsfilet sautiert mit Olivenöl, karibischen Gewürzen und Zitronenschale",
                "availability": "Verfügbar"
            },
            {
                "name": "Goldbrasse",
                "price": 28,
                "description": "280g Fischfilet sautiert mit Olivenöl und frischen Kräutern",
                "availability": "Nach Verfügbarkeit"
            },
            {
                "name": "Kabeljaufilet",
                "price": 28,
                "description": "220g Kabeljaufilet sautiert mit frischen Kräutern und Aromaten",
                "availability": "Nach Verfügbarkeit"
            },
            {
                "name": "Seebarsch (pro Pfund)",
                "price": 0,
                "description": "Seebarschfilets",
                "availability": "Nach Verfügbarkeit"
            },
            {
                "name": "Louisiana Paella",
                "price": 28,
                "description": "Haitianische Paella mit Hähnchen, Wurst, Garnelen, Langustinen",
                "availability": "Verfügbar"
            }
        ]
    },
    "sides": {
        "en": [
            {"name": "Jasmine Rice", "price": 6, "description": "With cranberry & almonds"},
            {"name": "Djon Djon Rice", "price": 6, "description": "Haitian rice"},
            {"name": "Creamy Vegetables", "price": 6, "description": "Seasonal vegetables"},
            {"name": "Mashed Potatoes", "price": 6, "description": "Creamy mashed potatoes"},
            {"name": "Sautéed Vegetables", "price": 7, "description": "Fresh seasonal vegetables"},
            {"name": "Tostones", "price": 5, "description": "Fried plantains"},
            {"name": "Almonds in Syrup", "price": 5, "description": "Sweet almond dessert"},
            {"name": "French Fries", "price": 5, "description": "Classic french fries"}
        ],
        "de": [
            {"name": "Jasminreis", "price": 6, "description": "Mit Cranberry & Mandeln"},
            {"name": "Djon Djon Reis", "price": 6, "description": "Haitianischer Reis"},
            {"name": "Cremiges Gemüse", "price": 6, "description": "Saisonales Gemüse"},
            {"name": "Kartoffelpüree", "price": 6, "description": "Cremiges Kartoffelpüree"},
            {"name": "Sautiertes Gemüse", "price": 7, "description": "Frisches saisonales Gemüse"},
            {"name": "Tostones", "price": 5, "description": "Gebratene Kochbananen"},
            {"name": "Mandeln in Sirup", "price": 5, "description": "Süße Mandelnachspeise"},
            {"name": "Pommes Frites", "price": 5, "description": "Klassische Pommes Frites"}
        ]
    }
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, lang: str = "en"):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "lang": lang,
        "restaurant": RESTAURANT_DATA,
        "current_year": datetime.now().year,
        "query_params": dict(request.query_params)
    })

@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request, lang: str = "en"):
    return templates.TemplateResponse("menu.html", {
        "request": request,
        "lang": lang, 
        "restaurant": RESTAURANT_DATA,
        "menu": MENU_DATA,
        "current_year": datetime.now().year
    })

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request, lang: str = "en"):
    return templates.TemplateResponse("about.html", {
        "request": request,
        "lang": lang,
        "restaurant": RESTAURANT_DATA,
        "current_year": datetime.now().year
    })

@app.get("/contact", response_class=HTMLResponse) 
async def contact(request: Request, lang: str = "en"):
    return templates.TemplateResponse("contact.html", {
        "request": request,
        "lang": lang,
        "restaurant": RESTAURANT_DATA,
        "current_year": datetime.now().year
    })

@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request, lang: str = "en"):
    return templates.TemplateResponse("gallery.html", {
        "request": request,
        "lang": lang,
        "restaurant": RESTAURANT_DATA,
        "current_year": datetime.now().year
    })

# --- Admin routes: basic HTTP auth to view reservations ---
def verify_admin(credentials: HTTPBasicCredentials):
    """Verify provided HTTP Basic credentials against env vars.

    Uses ADMIN_USERNAME and ADMIN_PASSWORD environment variables.
    Defaults to admin/password when not set (development only).
    """
    correct_username = os.environ.get("ADMIN_USERNAME", "admin")
    correct_password = os.environ.get("ADMIN_PASSWORD", "password")
    valid = (
        secrets.compare_digest(credentials.username, correct_username)
        and secrets.compare_digest(credentials.password, correct_password)
    )
    if not valid:
        raise HTTPException(status_code=401, detail="Unauthorized", headers={"WWW-Authenticate": "Basic"})
    return credentials.username


@app.get("/admin/reservations", response_class=HTMLResponse)
def admin_reservations(request: Request, credentials: HTTPBasicCredentials = Depends(security), lang: str = "en"):
    # Verify admin credentials
    verify_admin(credentials)

    db = SessionLocal()
    reservations = db.query(Reservation).order_by(Reservation.created_at.desc()).all()
    db.close()

    return templates.TemplateResponse("admin_reservations.html", {
        "request": request,
        "reservations": reservations,
        "current_year": datetime.now().year,
        "restaurant": RESTAURANT_DATA,
        "lang": lang,
        "query_params": dict(request.query_params)
    })


@app.get("/admin")
def admin_index():
    # simple redirect to reservations page
    return RedirectResponse(url="/admin/reservations", status_code=302)


@app.get("/admin/reservation/{res_id}/edit", response_class=HTMLResponse)
def admin_edit_reservation(request: Request, res_id: int, credentials: HTTPBasicCredentials = Depends(security), lang: str = "en"):
    verify_admin(credentials)
    db = SessionLocal()
    reservation = db.query(Reservation).filter(Reservation.id == res_id).first()
    db.close()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    return templates.TemplateResponse("admin_edit_reservation.html", {
        "request": request,
        "reservation": reservation,
        "restaurant": RESTAURANT_DATA,
        "lang": lang,
        "current_year": datetime.now().year,
        "query_params": dict(request.query_params)
    })


@app.post("/admin/reservation/{res_id}/edit")
async def admin_update_reservation(request: Request, res_id: int,
                                   name: str = Form(...),
                                   email: str = Form(...),
                                   phone: str = Form(...),
                                   date: str = Form(...),
                                   time: str = Form(...),
                                   guests: int = Form(...),
                                   message: Optional[str] = Form(None),
                                   lang: str = Form("en"),
                                   credentials: HTTPBasicCredentials = Depends(security)):
    verify_admin(credentials)
    db = SessionLocal()
    reservation = db.query(Reservation).filter(Reservation.id == res_id).first()
    if not reservation:
        db.close()
        raise HTTPException(status_code=404, detail="Reservation not found")

    reservation.name = name
    reservation.email = email
    reservation.phone = phone
    reservation.date = date
    reservation.time = time
    reservation.guests = guests
    reservation.message = message
    reservation.lang = lang

    db.add(reservation)
    db.commit()
    db.close()

    return RedirectResponse(url="/admin/reservations", status_code=303)


@app.post("/admin/reservation/{res_id}/delete")
def admin_delete_reservation(request: Request, res_id: int, credentials: HTTPBasicCredentials = Depends(security)):
    verify_admin(credentials)
    db = SessionLocal()
    reservation = db.query(Reservation).filter(Reservation.id == res_id).first()
    if not reservation:
        db.close()
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(reservation)
    db.commit()
    db.close()
    return RedirectResponse(url="/admin/reservations", status_code=303)

@app.post("/contact-form")
async def contact_form(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    lang: str = Form("en")
):
    # Here you would typically process the contact form
    return RedirectResponse(
        url=f"/contact?lang={lang}&message=sent",
        status_code=303
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8800)
