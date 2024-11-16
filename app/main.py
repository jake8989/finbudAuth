import os
import grpc
from app.services.OTPService import OTPService
from concurrent import futures
from fastapi import FastAPI
from app.redis.redisConfig import get_redis_database
from app.gRPC import otp_pb2,otp_pb2_grpc
from dotenv import load_dotenv

redis=get_redis_database()
load_dotenv()

port=os.getenv('RUN_SERVER')
# print('printing the port',port)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    otp_pb2_grpc.add_OTPServiceServicer_to_server(OTPService(),server=server)
    server.add_insecure_port(port)
    print('Starting Auth Server on port: 3004')
    server.start()
    server.wait_for_termination()
    


serve()