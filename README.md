# Linkeds

Crossplatform Python messenger with async client-server architecture.

This is a new version of my old messenger project that is also was
based on my old messenger project made for school

---

## Requirements

* python3
* pymysql
* pyqt6
* mariadb

To run server you need to have runned database and db user with name that  
satisfies to config in `CONFIG/database_config.py`

Default database config is created automatically in `CONFIG/database_config.py`:
```python
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'userdatabase'
DB_USER = 'mysql'
DB_PASSWORD = 'mysql'
DB_CHARSET = 'utf8mb4'
```

---

## Linux install

### 1. Install dependencies
```bash
sudo apt install python3 python-pymysql python-pyqt6 pyqt6 mariadb-server
```

### 2. Start mariadb
```bash
sudo systemctl enable --now mariadb
sudo systemctl status mariadb
```

### 3. Clone project
```bash
git clone https://github.com/grannev/Linkeds.git
cd Linkeds
```

### 4. Create db user for linkeds
```bash
sudo mariadb
```
Run from mariadb:
```sql
CREATE USER IF NOT EXISTS 'mysql'@'%' IDENTIFIED BY 'mysql';
GRANT ALL PRIVILEGES ON *.* TO 'mysql'@'%';
FLUSH PRIVILEGES;
EXIT;
```

### 5. Start Linkeds server

```bash
python3 SERVER/runserver.py
```

### 6. Start Linkeds Client
```bash
python3 LinkedsMain/linkeds.py
```

---

## Windows install

### 1. Install python to PATH
```text
https://www.python.org/downloads/windows/
```

### 2. Clone project
```powershell
git clone https://github.com/grannev/Linkeds.git
cd Linkeds
```

### 3. Install dependencies
```powershell
pip install pyqt6 pymysql
```

### 4. Install open server panel (or other db client that support mariadb)
```text
https://ospanel.io/
```

### 5. Start Open Server Panel
1. Run osp 
2. Open the modules/settings section
3. Enable one database module: mariadb or mysql
4. Use port `3306`
5. Press `Start` / `Run` to start the server

be sure that you have user that satisfies db config
if u are not - check how to do this on the internet

### 6. Start Linkeds server
```powershell
python3 SERVER\runserver.py
```

### 7. Start Linkeds client
```powershell
python3 LinkedsMain\linkeds.py
```

## Screenshots

![image](LinkedsScreenshots/scr1.jpg)
![image](LinkedsScreenshots/scr2.jpg)
![image](LinkedsScreenshots/scr3.jpg)
![image](LinkedsScreenshots/scr4.jpg)
![image](LinkedsScreenshots/scr5.jpg)
![image](LinkedsScreenshots/scr6.jpg)
![image](LinkedsScreenshots/scr7.jpg)
![image](LinkedsScreenshots/scr8.jpg)
![image](LinkedsScreenshots/scr9.jpg)
![image](LinkedsScreenshots/scr10.jpg)
![image](LinkedsScreenshots/scr11.jpg)
![image](LinkedsScreenshots/scr12.jpg)
![image](LinkedsScreenshots/scr13.jpg)
