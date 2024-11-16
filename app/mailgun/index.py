import os
import httpx

mailgun_api_key=os.getenv("MAILGUN_API_KEY")
mailgun_api_url=os.getenv("MAILGUN_API_URL")



async def send_otp_email(to_email: str, subject: str, text: str):
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                mailgun_api_url,
                auth=("api", mailgun_api_key),
                data={
                    "from": "FinBud <services@finbud.kumarjayant.tech>", 
                    "to": [to_email],
                    "subject": subject,
                    "text": text
                })

            # For debugging
            print("Response Object:", type(response))
            print("Status Code:", response.status_code)
            print("Response Body:", response.text)

            return response

    except httpx.RequestError as e:
        print(f"An error occurred while requesting: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
