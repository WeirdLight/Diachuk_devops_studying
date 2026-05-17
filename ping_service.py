import os
import platform

def ping_host(host: str) -> dict:
    """
    Виконує команду ping для вказаного хоста.
    Автоматично визначає операційну систему.
    Повертає словник із детальним результатом замість голого True/False.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    if platform.system().lower() == 'windows':
        command = f"ping {param} 1 {host} > nul 2>&1"
    else:
        command = f"ping {param} 1 {host} > /dev/null 2>&1"
        
    exit_code = os.system(command)
    
    # РЕФАКТОРИНГ: Тепер повертаємо розширену структуру даних
    return {
        "host": host,
        "status": "Online" if exit_code == 0 else "Offline",
        "code": exit_code
    }