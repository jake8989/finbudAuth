from app.gRPC import otp_pb2,otp_pb2_grpc
from app.redis.redisConfig import get_redis_database
from app.mailgun.index import send_otp_email
import random
import asyncio
redis = get_redis_database()


class OTPService(otp_pb2_grpc.OTPServiceServicer):
    def GenerateOTP(self,request,context):
        loop=asyncio.new_event_loop()
        asyncio.set_event_loop(loop=loop)
        
        return loop.run_until_complete(self._GenerateOTP(request,context))
    
    async def _GenerateOTP(self, request, context):
        email=request.email
        
        user_otp=str(random.randint(100000,999999))
        subject = "Your OTP Code"
        text = f"Hello,\n\nYour OTP code is {user_otp}. Please use this to authenticate. \n\n FinBud"
        print(user_otp)
        
        try:
            #Send Email from Here
            reponse= await send_otp_email(to_email=email,subject=subject,text=text)
             
            if reponse.status_code!=200:
                return otp_pb2.GenerateOTPResponse(
                   success=False,
                   message='Failed to send email'
                )
            #set otp in redis for 2 minutes
            redis.setex(f"otp:{email}", 120, user_otp)
            return otp_pb2.GenerateOTPResponse(success=True, message="OTP sent successfully to email.")
            
        except Exception as e:
            print(e)    
            return otp_pb2.GenerateOTPResponse(success=False, message=f"Error Occured: {e}.")
        