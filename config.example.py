# Copie este arquivo para config.py e preencha com as suas credenciais.
# O config.py não é versionado (veja .gitignore).

# MongoDB Atlas -> Connect -> Drivers
MONGO_URI = (
    "mongodb+srv://<db_username>:<db_password>"
    "@<cluster>.mongodb.net/?appName=<app>"
)

# Neon -> Connect to your branch
NEON = {
    "host": "<host-do-neon>.neon.tech",
    "database": "neondb",
    "user": "neondb_owner",
    "password": "SUA_SENHA",
    "port": 5432,
    "sslmode": "require",
}
