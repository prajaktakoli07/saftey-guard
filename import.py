import sqlite3
import requests

# Connect to SQLite database
conn = sqlite3.connect('website_safety.db')
cursor = conn.cursor()

# Create a table to store website safety information if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS website_safety (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT,
                    safe BOOLEAN,
                    message TEXT
                )''')
conn.commit()

def is_safe(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            safe = True
            message = 'Website is safe to shop from.'
        else:
            safe = False
            message = 'Website may not be safe to shop from.'
    except Exception as e:
        safe = False
        message = f'Error checking website safety: {str(e)}'

    # Save result to database
    cursor.execute("INSERT INTO website_safety (url, safe, message) VALUES (?, ?, ?)", (url, safe, message))
    conn.commit()

    return {'safe': safe, 'message': message}

# Example usage:
result = is_safe("http://example.com")
print(result)

# Close database connection
conn.close()
