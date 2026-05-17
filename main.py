from ping_service import ping_host

def main():
    print("--- Мережевий Пінгер ---")
    
    # Приймаємо ввід від користувача через консоль
    host = input("Введіть IP-адресу для перевірки: ")
    
    print(f"Пінгуємо {host}...")
    
    # Викликаємо нашу core-логіку
    is_alive = ping_host(host)
    
    # Виводимо результат на екран
    if is_alive:
        print(f"Результат: Хост {host} ДОСТУПНИЙ 👍")
    else:
        print(f"Результат: Хост {host} НЕДОСТУПНИЙ ❌")

if __name__ == "__main__":
    main()