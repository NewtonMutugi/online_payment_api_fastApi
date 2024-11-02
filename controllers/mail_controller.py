from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from api.mail_api import mail_api

router = APIRouter()


class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str


@router.post("/contact")
async def send_email(contact_form: ContactForm):
    try:
        # Create message
        message = "Subject: New Contact Us Message\n\n"
        message += f"Name: {contact_form.name}\n"
        message += f"Email: {contact_form.email}\n"
        message += f"Message:\n{contact_form.message}"

        # Connect to the server and send the email
        mail_api.send_email(contact_form)

        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to send email") from e
