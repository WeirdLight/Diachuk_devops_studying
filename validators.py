def is_valid_ipv4(ip_str: str) -> bool:
    """
    Перевіряє, чи є рядок валідною IPv4-адресою.
    Приймає рядок, розбиває його по крапках і перевіряє кожен октет.
    """
    parts = ip_str.split('.')
    
    # В IPv4 має бути рівно 4 частини (октети)
    if len(parts) != 4:
        return False
        
    for part in parts:
        # Перевіряємо, чи складається частина лише з цифр
        if not part.isdigit():
            return False
            
        num = int(part)
        # Кожне число має бути в діапазоні від 0 до 255
        if num < 0 or num > 255:
            return False
            
    return True