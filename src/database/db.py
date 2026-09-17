import psycopg2
import bcrypt
import json
import os

import os


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "attendance_system"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "12345"),
    "port": os.getenv("DB_PORT", "5432")
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            name TEXT
        )
    ''')
    
    # Create students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            name TEXT,
            face_embedding TEXT,
            voice_embedding TEXT
        )
    ''')
    
    # Create subjects table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_id SERIAL PRIMARY KEY,
            subject_code TEXT UNIQUE,
            name TEXT,
            section TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        )
    ''')
    
    # Create subject_students (enrollment)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subject_students (
            student_id INTEGER,
            subject_id INTEGER,
            PRIMARY KEY (student_id, subject_id),
            FOREIGN KEY (student_id) REFERENCES students (student_id),
            FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )
    ''')
    
    # Create attendance_logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance_logs (
            log_id SERIAL PRIMARY KEY,
            student_id INTEGER,
            subject_id INTEGER,
            timestamp TEXT,
            is_present INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (student_id),
            FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Ensure DB is created on import
setup_database()

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM teachers WHERE username = %s", (username,))
    row = cursor.fetchone()
    conn.close()
    return row is not None


def create_teacher(username, password, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (username, password, name) VALUES (?, ?, ?)",
                   (username, hash_pass(password), name))
    conn.commit()
    conn.close()
    return True

def teacher_login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password, name FROM teachers WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        teacher = {'id': row[0], 'username': row[1], 'password': row[2], 'name': row[3]}
        if check_pass(password, teacher['password']):
            return teacher
    return None


def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT student_id, name, face_embedding, voice_embedding FROM students")
    rows = cursor.fetchall()
    conn.close()
    
    students = []
    for r in rows:
        students.append({
            'student_id': r[0],
            'name': r[1],
            'face_embedding': json.loads(r[2]) if r[2] else None,
            'voice_embedding': json.loads(r[3]) if r[3] else None
        })
    return students

def create_student(new_name, face_embedding=None, voice_embedding=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    f_emb = json.dumps(face_embedding) if face_embedding else None
    v_emb = json.dumps(voice_embedding) if voice_embedding else None
    
    cursor.execute("INSERT INTO students (name, face_embedding, voice_embedding) VALUES (?, ?, ?)",
                   (new_name, f_emb, v_emb))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return [{'student_id': student_id, 'name': new_name}]


def create_subject(subject_code, name, section, teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subjects (subject_code, name, section, teacher_id) VALUES (?, ?, ?, ?)",
                       (subject_code, name, section, teacher_id))
        conn.commit()
    except psycopg2.IntegrityError:
        pass # Handle unique constraint for subject code
    conn.close()
    return True

def get_teacher_subjects(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT subject_id, subject_code, name, section, teacher_id FROM subjects WHERE teacher_id = ?", (teacher_id,))
    rows = cursor.fetchall()
    
    subjects = []
    for r in rows:
        subject_id = r[0]
        sub = {
            'subject_id': subject_id,
            'subject_code': r[1],
            'name': r[2],
            'section': r[3],
            'teacher_id': r[4]
        }
        
        # Count students
        cursor.execute("SELECT COUNT(*) FROM subject_students WHERE subject_id = ?", (subject_id,))
        sub['total_students'] = cursor.fetchone()[0]
        
        # Count unique sessions (classes)
        cursor.execute("SELECT COUNT(DISTINCT timestamp) FROM attendance_logs WHERE subject_id = ?", (subject_id,))
        sub['total_classes'] = cursor.fetchone()[0]
        
        subjects.append(sub)
    conn.close()
    return subjects

def enroll_student_to_subject(student_id, subject_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subject_students (student_id, subject_id) VALUES (?, ?)", (student_id, subject_id))
        conn.commit()
    except sqlite3.IntegrityError:
        pass # Already enrolled
    conn.close()
    return True

def unenroll_student_to_subject(student_id, subject_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM subject_students WHERE student_id = ? AND subject_id = ?", (student_id, subject_id))
    conn.commit()
    conn.close()
    return True

def get_student_subjects(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.subject_id, s.subject_code, s.name, s.section, s.teacher_id
        FROM subject_students ss
        JOIN subjects s ON ss.subject_id = s.subject_id
        WHERE ss.student_id = ?
    ''', (student_id,))
    rows = cursor.fetchall()
    conn.close()
    
    subjects = []
    for r in rows:
        subjects.append({
            'subjects': {
                'subject_id': r[0],
                'subject_code': r[1],
                'name': r[2],
                'section': r[3],
                'teacher_id': r[4]
            }
        })
    return subjects

def get_student_attendance(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT a.log_id, a.student_id, a.subject_id, a.timestamp, a.is_present,
               s.subject_id, s.subject_code, s.name, s.section, s.teacher_id
        FROM attendance_logs a
        JOIN subjects s ON a.subject_id = s.subject_id
        WHERE a.student_id = ?
    ''', (student_id,))
    rows = cursor.fetchall()
    conn.close()
    
    logs = []
    for r in rows:
        logs.append({
            'log_id': r[0],
            'student_id': r[1],
            'subject_id': r[2],
            'timestamp': r[3],
            'is_present': bool(r[4]),
            'subjects': {
                'subject_id': r[5],
                'subject_code': r[6],
                'name': r[7],
                'section': r[8],
                'teacher_id': r[9]
            }
        })
    return logs

def create_attendance(logs):
    conn = get_connection()
    cursor = conn.cursor()
    for log in logs:
        cursor.execute('''
            INSERT INTO attendance_logs (student_id, subject_id, timestamp, is_present)
            VALUES (?, ?, ?, ?)
        ''', (log['student_id'], log['subject_id'], log['timestamp'], 1 if log['is_present'] else 0))
    conn.commit()
    conn.close()
    return True

def get_attendance_for_teacher(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT a.log_id, a.student_id, a.subject_id, a.timestamp, a.is_present,
               s.subject_id, s.subject_code, s.name, s.section, s.teacher_id
        FROM attendance_logs a
        JOIN subjects s ON a.subject_id = s.subject_id
        WHERE s.teacher_id = ?
    ''', (teacher_id,))
    rows = cursor.fetchall()
    conn.close()
    
    logs = []
    for r in rows:
        logs.append({
            'log_id': r[0],
            'student_id': r[1],
            'subject_id': r[2],
            'timestamp': r[3],
            'is_present': bool(r[4]),
            'subjects': {
                'subject_id': r[5],
                'subject_code': r[6],
                'name': r[7],
                'section': r[8],
                'teacher_id': r[9]
            }
        })
    return logs

# --- NEW HELPER FUNCTIONS REPLACING DIRECT SUPABASE CALLS IN UI COMPONENTS ---

def get_subject_by_code(subject_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT subject_id, name, subject_code FROM subjects WHERE subject_code = ?", (subject_code,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {'subject_id': row[0], 'name': row[1], 'subject_code': row[2]}
    return None

def check_enrollment(student_id, subject_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subject_students WHERE student_id = ? AND subject_id = ?", (student_id, subject_id))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def get_enrolled_students(subject_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.student_id, s.name, s.face_embedding, s.voice_embedding
        FROM subject_students ss
        JOIN students s ON ss.student_id = s.student_id
        WHERE ss.subject_id = ?
    ''', (subject_id,))
    rows = cursor.fetchall()
    conn.close()
    
    students = []
    for r in rows:
        students.append({
            'students': {
                'student_id': r[0],
                'name': r[1],
                'face_embedding': json.loads(r[2]) if r[2] else None,
                'voice_embedding': json.loads(r[3]) if r[3] else None
            }
        })
    return students