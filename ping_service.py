import os
import platform

def ping_host(host: str) -> bool:
    """Ping a host once and return True if it is reachable."""
    system = platform.system().lower()
    param = '-n' if system == 'windows' else '-c'

    if system == 'windows':
        command = f"ping {param} 1 {host} > nul 2>&1"
    else:
        command = f"ping {param} 1 {host} > /dev/null 2>&1"

    return os.system(command) == 0
