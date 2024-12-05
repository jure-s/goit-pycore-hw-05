import json
import os

# Шлях до файлу з контактами
CONTACTS_FOLDER = "contacts"
CONTACTS_FILE = os.path.join(CONTACTS_FOLDER, "contacts.json")

def ensure_storage_directory():
    """Створює папку для збереження контактів, якщо її немає."""
    if not os.path.exists(CONTACTS_FOLDER):
        os.makedirs(CONTACTS_FOLDER)

def load_contacts():
    """Завантажує контакти з файлу."""
    ensure_storage_directory()
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Зберігає контакти у файл."""
    ensure_storage_directory()
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
