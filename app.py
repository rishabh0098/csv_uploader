from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3
import csv
import io
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Database configuration
DATABASE = 'csv_data.db'

def init_db():
    """Initialize the database with the required table"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create table for storing CSV data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            full_name TEXT,
            state_location TEXT,
            school TEXT,
            class_name TEXT,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """Main page with upload form and data display"""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY uploaded_at DESC').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV file upload and processing"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    if not file.filename.lower().endswith('.csv'):
        flash('Please upload a CSV file')
        return redirect(url_for('index'))
    
    try:
        # Read CSV content
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_input = csv.reader(stream)
        
        # Get header row
        header = next(csv_input)
        header = [col.strip().lower() for col in header]
        
        conn = get_db_connection()
        
        # Process each row
        rows_processed = 0
        for row in csv_input:
            if not row or all(cell.strip() == '' for cell in row):
                continue
                
            # Initialize variables
            first_name = middle_name = last_name = full_name = ""
            state_location = school = class_name = ""
            
            # Parse data based on available columns
            for i, col in enumerate(header):
                if i >= len(row):
                    break
                    
                value = row[i].strip()
                
                if 'first' in col and 'name' in col:
                    first_name = value
                elif 'middle' in col and 'name' in col:
                    middle_name = value
                elif 'last' in col and 'name' in col:
                    last_name = value
                elif col == 'name' or 'full' in col:
                    full_name = value
                elif 'state' in col or 'location' in col:
                    state_location = value
                elif 'school' in col:
                    school = value
                elif 'class' in col:
                    class_name = value
            
            # If we have separate name parts, combine them
            if first_name or middle_name or last_name:
                name_parts = [part for part in [first_name, middle_name, last_name] if part]
                full_name = ' '.join(name_parts)
            
            # Insert into database
            conn.execute('''
                INSERT INTO students (first_name, middle_name, last_name, full_name, 
                                    state_location, school, class_name)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (first_name, middle_name, last_name, full_name, 
                  state_location, school, class_name))
            
            rows_processed += 1
        
        conn.commit()
        conn.close()
        
        flash(f'Successfully uploaded and processed {rows_processed} records!')
        
    except Exception as e:
        flash(f'Error processing file: {str(e)}')
    
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_data():
    """Clear all data from the database"""
    conn = get_db_connection()
    conn.execute('DELETE FROM students')
    conn.commit()
    conn.close()
    flash('All data cleared successfully!')
    return redirect(url_for('index'))

@app.route('/api/students')
def api_students():
    """API endpoint to get all students data"""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY uploaded_at DESC').fetchall()
    conn.close()
    
    students_list = []
    for student in students:
        students_list.append({
            'id': student['id'],
            'first_name': student['first_name'],
            'middle_name': student['middle_name'],
            'last_name': student['last_name'],
            'full_name': student['full_name'],
            'state_location': student['state_location'],
            'school': student['school'],
            'class_name': student['class_name'],
            'uploaded_at': student['uploaded_at']
        })
    
    return jsonify(students_list)

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
