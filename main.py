from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from passlib.context import CryptContext
from pymongo import MongoClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum
import string
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORSMiddleware to the application instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,  # Allows credentials (such as cookies, authorization headers, etc.) to be sent in cross-origin requests
    allow_methods=["*"],  # Allows all methods (such as GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"]
)

# Load environment variables
load_dotenv()

EMAIL_ADDRESS="snipe.upl@gmail.com"
EMAIL_PASSWORD="ljzz hsqx qvwc fbdr"
MONGO_DETAILS="mongodb+srv://shreyasraohmohite:Shreyas111@aicodedisha.wqjv1yv.mongodb.net/?retryWrites=true&w=majority"
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

client = MongoClient(MONGO_DETAILS)
db = client.Login_Register
users_collection = db.Login_Register_Auth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Role(str, Enum):
    organization = "Organization"
    student = "Student"

class UserSchema(BaseModel):
    email: EmailStr
    role: Role  # Use the Role enum here
    name: str
    mobile_number: str
    password: str
    confirm_password: str
    # organization_id: Optional[str] = None  # New field for organization ID


class OTPVerificationSchema(BaseModel):
    email: EmailStr
    otp: int

class Token(BaseModel):
    access_token: str
    token_type: str
    organization_id: Optional[str] = None
    name: str
    role: Role
    email: EmailStr

class TokenData(BaseModel):
    email: Optional[str] = None

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def send_email_otp(email: str, otp: int):
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = email
    message['Subject'] = 'Your OTP'
    
    body = f'Your OTP is: {otp}'
    message.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = message.as_string()
    server.sendmail(EMAIL_ADDRESS, email, text)
    server.quit()


def save_user(user_data: UserSchema, hashed_password: str, otp: int):
    user_dict = user_data.dict()
    user_dict.pop('confirm_password')  # Remove confirm_password before saving
    user_dict['password'] = hashed_password
    user_dict['otp'] = otp
    user_dict['otp_expiry'] = datetime.utcnow() + timedelta(minutes=10)  # OTP expires in 10 minutes
    users_collection.insert_one(user_dict)

def generate_unique_organization_id(length=10):
    characters = string.ascii_uppercase + string.digits
    while True:
        organization_id = ''.join(random.choice(characters) for _ in range(length))
        if not users_collection.find_one({"organization_id": organization_id}):
            return organization_id
        
 
def send_password_reset_confirmation_email(email: str, name: str):
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = email
    message['Subject'] = 'Password Reset Confirmation'

    body = f'Hi {name},\n\nYour password has been successfully reset. If you did not initiate this change, please contact our support immediately.\n\nBest Regards,\nAI- Disha'
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = message.as_string()
    server.sendmail(EMAIL_ADDRESS, email, text)
    server.quit()


 
        
def send_welcome_email(email: str, name: str):
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = email
    message['Subject'] = 'Welcome to Our AI - Disha!'
    
    body = f'Hi {name},\n\nWelcome to AI- Disha!\nCongratulations you have Registered Successfully!!! \nWe are excited to have you on board.\n\nWe are glad you have registered to our platform. \nVisit: www.aidisha.com \n\nThanks & Regards,\nAI - Disha'
    message.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = message.as_string()
    server.sendmail(EMAIL_ADDRESS, email, text)
    server.quit()
    
def get_client_ip(request: Request):
    client_host = request.client.host
    return client_host

def get_client_ip(request: Request):
    if "X-Forwarded-For" in request.headers:
        # In case there are multiple proxies, take the first one.
        return request.headers["X-Forwarded-For"].split(",")[0]
    return request.client.host


def send_new_device_login_email(email: str, ip: str, name: str):
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = email
    message['Subject'] = 'New Device Login Detected'

    body = f"""Hi {name},
    
A new login to your account was detected from a device using IP address {ip}.
If this was you, you can safely ignore this email. \nIf you do not recognize this login, we strongly recommend that you change your password immediately as your account may be compromised.

Best Regards,
AI- Disha"""
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = message.as_string()
    server.sendmail(EMAIL_ADDRESS, email, text)
    server.quit()  

@app.post("/Register/")
async def send_otp(user_data: UserSchema):
    if user_data.password != user_data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match.")
    
    # Check if the email is already registered
    if users_collection.find_one({"email": user_data.email}):
        raise HTTPException(status_code=400, detail="Email already registered.")
    
    hashed_password = get_password_hash(user_data.password)
    otp = random.randint(100000, 999999)
    save_user(user_data, hashed_password, otp)
    send_email_otp(user_data.email, otp)
    
    return {"message": "OTP sent to the email. Please verify to complete registration."}



@app.post("/Register-Verify-OTP/")
async def verify_otp(otp_data: OTPVerificationSchema):
    user = users_collection.find_one({"email": otp_data.email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    current_time = datetime.utcnow()
    if user.get('otp') == otp_data.otp and current_time < user.get('otp_expiry'):
        update_data = {"is_verified": True}
        if user.get('role') == Role.organization:
            organization_id = generate_unique_organization_id()
            update_data["organization_id"] = organization_id
        users_collection.update_one({"email": otp_data.email}, {"$set": update_data})
        
        # Send welcome email
        send_welcome_email(otp_data.email, user['name'])
        
        return {"message": "OTP verified successfully. Registration complete."}
    else:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP.")

@app.post("/Login", response_model=Token)
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):   
    email = form_data.username  # Treat the 'username' field as the user's email
    password = form_data.password

    user = authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Continue with your existing logic...


    # Example function to get client IP - implement this based on your requirements
    client_ip = get_client_ip(request)
    
    # Check if IP is new
    if client_ip not in user.get('known_ips', []):
        # If new, update known IPs and send email
        users_collection.update_one({"email": user['email']}, {"$addToSet": {"known_ips": client_ip}})
        send_new_device_login_email(user['email'], client_ip, user['name'])

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['email']}, expires_delta=access_token_expires
    )

    # Extract additional information from the user object
    organization_id = user.get('organization_id')
    name = user.get('name')
    role = user.get('role')
    email = user['email']

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "organization_id": organization_id,
        "name": name,
        "role": role,
        "email": email
    }

@app.post("/Forget-Password-Email/")
async def password_reset_send_otp(email: EmailStr):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="Email not found.")
    
    # Generate and save OTP
    otp = random.randint(100000, 999999)
    otp_expiry = datetime.utcnow() + timedelta(minutes=10)  # OTP expires in 10 minutes
    users_collection.update_one({"email": email}, {"$set": {"reset_otp": otp, "reset_otp_expiry": otp_expiry}})
    
    # Send OTP to user's email
    send_email_otp(email, otp)
    
    return {"message": "OTP sent to the email. Please verify to proceed with password reset."}



@app.post("/Forget-Password/Verify-OTP/")
async def password_reset_verify_otp(otp_data: OTPVerificationSchema):
    user = users_collection.find_one({"email": otp_data.email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    current_time = datetime.utcnow()
    if user.get('reset_otp') == otp_data.otp and current_time < user.get('reset_otp_expiry'):
        # Optionally, you could mark the OTP as used here to prevent reuse
        return {"message": "OTP verified successfully. You may now reset your password."}
    else:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP.")

@app.post("/Password-Reset/")
async def password_reset(otp_data: OTPVerificationSchema, new_password: str, confirm_password: str):
    if new_password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match.")
    
    user = users_collection.find_one({"email": otp_data.email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    current_time = datetime.utcnow()
    if user.get('reset_otp') == otp_data.otp and current_time < user.get('reset_otp_expiry'):
        hashed_password = get_password_hash(new_password)
        users_collection.update_one({"email": otp_data.email}, {"$set": {"password": hashed_password}})
        # Optionally, clear the OTP fields here to prevent reuse

        # Send password reset confirmation email
        send_password_reset_confirmation_email(otp_data.email, user['name'])

        return {"message": "Password reset successfully."}
    else:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP.")
