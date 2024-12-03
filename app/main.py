import os
import grpc
from app.services.OTPService import OTPService
from concurrent import futures
from fastapi import FastAPI
from app.redis.redisConfig import get_redis_database
from app.gRPC import otp_pb2, otp_pb2_grpc
from dotenv import load_dotenv
import time
import logging

load_dotenv()

redis = get_redis_database()


port = os.getenv("RUN_SERVER")


# print('printing the port',port)
def serve():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        otp_pb2_grpc.add_OTPServiceServicer_to_server(OTPService(), server=server)
        server.add_insecure_port(port)
        print("Starting Auth Server on port: 3004")
        server.start()
        server.wait_for_termination()
    except Exception as e:
        print(f"Server crashed with error: {e}. Restarting in 5 seconds...")
        time.sleep(5)

    finally:
        logging.info("Cleaning up resources...")


serve()
