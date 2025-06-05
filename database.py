import sqlite3
from datetime import date

def init_db():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS surveys
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  full_name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  dob DATE NOT NULL,
                  contact TEXT NOT NULL,
                  pizza INTEGER DEFAULT 0,
                  pasta INTEGER DEFAULT 0,
                  pap_wors INTEGER DEFAULT 0,
                  other_food TEXT,
                  movies_rating INTEGER,
                  radio_rating INTEGER,
                  eat_out_rating INTEGER,
                  tv_rating INTEGER,
                  submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_survey(full_name, email, dob, contact, pizza, pasta, pap_wors, other_food, movies, radio, eat_out, tv):
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''INSERT INTO surveys 
                 (full_name, email, dob, contact, pizza, pasta, pap_wors, other_food, 
                  movies_rating, radio_rating, eat_out_rating, tv_rating)
                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
              (full_name, email, dob, contact, int(pizza), int(pasta), int(pap_wors), other_food,
               movies, radio, eat_out, tv))
    conn.commit()
    conn.close()

def get_survey_stats():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    
    stats = {}
    c.execute("SELECT COUNT(*) FROM surveys")
    stats['total'] = c.fetchone()[0]
    
    if stats['total'] == 0:
        conn.close()
        return stats

    # Fixed age calculation query
    c.execute("""
        SELECT 
            AVG((julianday('now') - julianday(dob))/365.25),
            MIN((julianday('now') - julianday(dob))/365.25),
            MAX((julianday('now') - julianday(dob))/365.25)
        FROM surveys
    """)
    stats['avg_age'], stats['min_age'], stats['max_age'] = c.fetchone()
    
    c.execute("SELECT SUM(pizza), SUM(pasta), SUM(pap_wors) FROM surveys")
    stats['pizza'], stats['pasta'], stats['pap_wors'] = c.fetchone()
    
    c.execute("SELECT AVG(movies_rating), AVG(radio_rating), AVG(eat_out_rating), AVG(tv_rating) FROM surveys")
    stats['movies'], stats['radio'], stats['eat_out'], stats['tv'] = c.fetchone()
    
    conn.close()
    return stats