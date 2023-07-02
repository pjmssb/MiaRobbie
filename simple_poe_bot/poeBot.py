from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('POE_API_KEY')
print("POE_API_KEY -->", api_key)