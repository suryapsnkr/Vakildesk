import time
from collections import defaultdict
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests=5, window_size=60):
        self.max_requests = max_requests
        self.window_size = window_size
        self.user_requests = defaultdict(list)
        self.lock = Lock()

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()

            # Clean up old requests
            self.user_requests[user_id] = [
                request_time for request_time in self.user_requests[user_id]
                if current_time - request_time < self.window_size
            ]

            # Check if the user can make a new request
            if len(self.user_requests[user_id]) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            
            return False

# Example Usage
if __name__ == "__main__":
    rate_limiter = RateLimiter()

    user_id = '1591'

    # Simulate requests
    for i in range(10):
        if rate_limiter.allow_request(user_id):
            print(f"Request {i + 1} allowed for {user_id}.")
        else:
            print(f"Request {i + 1} denied for {user_id}.")
        time.sleep(5)  # Wait for 5 seconds between requests
