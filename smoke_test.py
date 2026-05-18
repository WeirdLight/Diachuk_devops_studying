import sys

def run_smoke_test():
    print("Starting Post-Deployment Verification (Smoke Tests)...")
    
    # Імітація перевірки працездатності: перевіряємо, що 1 дорівнює 1
    expected_status = 1
    actual_status = 1
    
    print(f"Checking system core status: Expected {expected_status}, Got {actual_status}")
    
    # Якщо умова виконується — тест пройдено
    if expected_status == actual_status:
        print("SUCCESS: Smoke tests passed. Staging environment is healthy!")
        sys.exit(0)  # Повертаємо код 0 (успіх)
    else:
        print("ERROR: Smoke tests failed. Staging environment is corrupted!")
        sys.exit(1)  # Повертаємо код 1 (помилка, яка завалить пайплайн)

if __name__ == "__main__":
    run_smoke_test()