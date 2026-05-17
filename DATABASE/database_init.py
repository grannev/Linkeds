import pymysql

from CONFIG.config_init import ensure_database_config

ensure_database_config()

from CONFIG.database_config import DB_CHARSET, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


TABLE_SCHEMAS = (
    """
    CREATE TABLE IF NOT EXISTS `user` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `ip` VARCHAR(64) DEFAULT NULL,
        `online` VARCHAR(5) NOT NULL DEFAULT 'False',
        `login` VARCHAR(255) NOT NULL,
        `password` VARCHAR(255) NOT NULL,
        `email` VARCHAR(255) NOT NULL DEFAULT 'Не указано',
        `gender` VARCHAR(64) NOT NULL DEFAULT 'Не указано',
        `name` VARCHAR(255) NOT NULL DEFAULT 'Не указано',
        `status` TEXT,
        `deleted_status` VARCHAR(5) NOT NULL DEFAULT 'False',
        PRIMARY KEY (`id`),
        UNIQUE KEY `user_login_unique` (`login`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """,
    """
    CREATE TABLE IF NOT EXISTS `social` (
        `id` INT NOT NULL,
        `pfp` TEXT,
        `posts` LONGBLOB,
        `friends` LONGBLOB,
        `messages` LONGBLOB,
        `request_friends` LONGBLOB,
        `black_list_friends` LONGBLOB,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """,
    """
    CREATE TABLE IF NOT EXISTS `connection` (
        `ip` VARCHAR(64) NOT NULL,
        `id` INT NOT NULL,
        `user_data` LONGBLOB,
        PRIMARY KEY (`ip`),
        KEY `connection_user_id` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """,
    """
    CREATE TABLE IF NOT EXISTS `message` (
        `from_` INT NOT NULL,
        `to_` INT NOT NULL,
        `id` INT NOT NULL,
        `status` VARCHAR(64),
        `text` TEXT,
        `time` VARCHAR(64),
        `image` LONGBLOB,
        KEY `message_from_id` (`from_`),
        KEY `message_to_id` (`to_`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
    """,
)


def initialize_database() -> None:
    """
    create the configured database and all required tables
    mariadb server must already be running
    """
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        charset=DB_CHARSET,
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
                f"CHARACTER SET {DB_CHARSET} COLLATE {DB_CHARSET}_unicode_ci"
            )
            cursor.execute(f"USE `{DB_NAME}`")
            for schema in TABLE_SCHEMAS:
                cursor.execute(schema)
        connection.commit()
    finally:
        connection.close()
