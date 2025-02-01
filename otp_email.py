# this is library
import smtplib
import random

# Directly include your email credentials here
EMAIL_ADDRESS = "s1t2g0@gmail.com"
EMAIL_PASSWORD = "edfvuerbdjjjobqe"  # App Password for Gmail

# Generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send OTP to email
def send_otp(email, otp):
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Start TLS encryption
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Email content
        subject = "Your OTP for Login"
        body = f"Your One-Time Password (OTP) is: {otp}"
        message = f"Subject: {subject}\n\n{body}"

        # Send email
        server.sendmail(EMAIL_ADDRESS, email, message)
        print(f"OTP sent to {email}")
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function
def main():
    print("Welcome to the OTP-based 2FA system!")
    
    # Step 1: Generate OTP
    otp = generate_otp()
    print("OTP generated.")

    # Step 2: Get user email and send OTP
    recipient_email = input("Enter your email address: ")
    send_otp(recipient_email, otp)

    # Step 3: Ask user to enter the OTP
    user_input = input("Enter the OTP you received: ")

    # Step 4: Verify OTP
    if user_input == otp:
        print("OTP verified successfully! Access granted.")
    else:
        print("Invalid OTP. Access denied.")

if __name__ == "__main__":
    main()
