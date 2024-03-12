import time
from queue import Queue

queue = Queue()

def generate_request():
    request = time.time()
    queue.put(request)
    print(f"Added request {request} to queue")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processed request #{request}")
    else:
        print("No requests to process")

while True:
    try:
      generate_request()
      process_request()
    except KeyboardInterrupt:
      print("Emulation stopped by user")
      break