import subprocess
import platform

# Используем пинг для проверки доступности хоста с учетом особенностей операционной системы
host = ("yandex.ru")

def ping_host(host):
    try:
        # Выставляем параметр под операционной систему
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        # Выполняем команду ping
        command = ['ping', parameter, '1', host]
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Если код возврата 0, хост доступен
        if output.returncode == 0:
            print(f"Хост {host} доступен.")
        else:
            print(f"Хост {host} недоступен.")

    except Exception as e:
        print(f"Ошибка при выполнении ping: {e}")


# Пример использования
ping_host(host)
