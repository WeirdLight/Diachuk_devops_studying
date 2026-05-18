import sys

def run_smoke_test():
    print("Starting Post-Deployment Verification (Smoke Tests)...")
    
    expected_status = 1
    actual_status = 0  # Змінюємо з 1 на 0, щоб зламати перевірку
    
    print(f"Checking system core status: Expected {expected_status}, Got {actual_status}")
    
    if expected_status == actual_status:
        print("SUCCESS: Smoke tests passed.")
        sys.exit(0)
    else:
        print("ERROR: Smoke tests failed!")
        sys.exit(1)  # Пайплайн побачить цей код і зупиниться

if __name__ == "__main__":
    run_smoke_test()