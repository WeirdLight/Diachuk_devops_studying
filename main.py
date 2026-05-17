from validators import is_valid_ipv4
from ping_service import ping_host

def main():
    print("=" * 40)
    print("      МЕРЕЖЕВИЙ МОНІТОР ХОСТІВ      ")
    print("=" * 40)
    
    # ФІКС БАГУ: додаємо .strip() для очищення рядка від випадкових пробілів
    host = input("Введіть IP-адресу для перевірки: ").strip()
    
    if not is_valid_ipv4(host):
        print("\n[ПОМИЛКА] Введено некоректний формат IPv4-адреси!")
        return

    print(f"\nНадсилання запиту до {host}...")
    result = ping_host(host)
    
    print("-" * 40)
    if result["status"] == "Online":
        print(f"Результат: Хост {result['host']} ДОСТУПНИЙ 👍")
    else:
        print(f"Результат: Хост {result['host']} НЕДОСТУПНИЙ ❌ (Код відповіді: {result['code']})")
    print("-" * 40)

if __name__ == "__main__":
    main()

#conflict

#for commit 1