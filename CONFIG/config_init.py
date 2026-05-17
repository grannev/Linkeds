from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATABASE_CONFIG = """DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'userdatabase'
DB_USER = 'mysql'
DB_PASSWORD = 'mysql'
DB_CHARSET = 'utf8mb4'
"""

SERVER_CONFIG = """SERVER_IP = '127.0.0.1'
SERVER_PORT = 25565
"""

CLIENT_CONFIG = SERVER_CONFIG


def ensure_config(relative_path: str, content: str) -> None:
    config_path = PROJECT_ROOT / relative_path
    if config_path.exists():
        return
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(content, encoding='utf-8')


def ensure_database_config() -> None:
    ensure_config('CONFIG/database_config.py', DATABASE_CONFIG)


def ensure_server_config() -> None:
    ensure_config('CONFIG/server_config.py', SERVER_CONFIG)


def ensure_client_config() -> None:
    ensure_config('LinkedsMain/CLIENT/client_config.py', CLIENT_CONFIG)
