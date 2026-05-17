from validators import is_valid_ipv4
from ping_service import ping_host


def main():
    print("--- Мережевий Пінгер ---")

    host = input("Введіть IP-адресу для перевірки: ")

    # Перевірка валідації IPv4
    if not is_valid_ipv4(host):
        print("Помилка: Введено некоректний формат IPv4!")
        return

    print(f"Пінгуємо {host}...")
    is_alive = ping_host(host)

    if is_alive:
        print(f"Результат: Хост {host} ДОСТУПНИЙ 👍")
    else:
        print(f"Результат: Хост {host} НЕДОСТУПНИЙ ❌")


if __name__ == "__main__":
    main()