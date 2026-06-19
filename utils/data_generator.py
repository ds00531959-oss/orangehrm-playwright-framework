import random
import time


def generate_employee():
    timestamp = int(time.time())

    return {
        "first_name": f"Auto{timestamp}",
        "last_name": f"User{timestamp}",
        "employee_id": str(random.randint(100000, 999999))
    }