# CSV Uploader Web Application

A modern web application that allows users to upload CSV files containing student data and stores them in an SQLite database. The application features a beautiful, responsive UI with drag-and-drop file upload functionality.

## Features

- **File Upload**: Drag-and-drop or click-to-upload CSV files
- **Flexible CSV Format**: Supports two CSV formats:
  - Separate name fields: First Name, Middle Name, Last Name, State/Location, School, Class
  - Combined name field: Name, State/Location, School, Class
- **Data Storage**: SQLite database for persistent storage
- **Data Display**: Beautiful table view of uploaded records
- **Statistics**: Real-time statistics showing record counts
- **Data Export**: Export uploaded data back to CSV format
- **Data Management**: Clear all data functionality
- **Responsive Design**: Works on desktop and mobile devices

## Quick Start with Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd csv_uploader
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   
   **Or use the Makefile for easier commands**:
   ```bash
   make up    # Start the application
   make logs  # View logs
   make down  # Stop the application
   make help  # See all available commands
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

The application will be running in a Docker container with persistent data storage.

## Manual Installation (Alternative)

1. **Clone or download the project**:
   ```bash
   cd csv_uploader
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Upload CSV files**:
   - Drag and drop a CSV file onto the upload area, or
   - Click the upload area to browse and select a file
   - Click "Upload File" to process the data

## CSV Format

The application supports two CSV formats:

### Format 1: Separate Name Fields
```csv
First Name,Middle Name,Last Name,State/Location,School,Class
John,Michael,Smith,California,Harvard University,Grade 10
Jane,,Doe,Texas,Stanford University,Grade 11
```

### Format 2: Combined Name Field
```csv
Name,State/Location,School,Class
John Michael Smith,California,Harvard University,Grade 10
Jane Doe,Texas,Stanford University,Grade 11
```

## Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    full_name TEXT,
    state_location TEXT,
    school TEXT,
    class_name TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## API Endpoints

- `GET /` - Main page with upload form and data display
- `POST /upload` - Handle CSV file upload
- `POST /clear` - Clear all data from database
- `GET /api/students` - JSON API to get all student data

## Features in Detail

### Upload Interface
- Modern drag-and-drop interface
- File validation (CSV files only)
- Real-time file preview
- Progress indication

### Data Management
- Automatic parsing of different CSV formats
- Data validation and cleaning
- Duplicate handling
- Batch processing

### User Interface
- Bootstrap 5 responsive design
- Font Awesome icons
- Real-time statistics
- Data export functionality
- Mobile-friendly design

### Data Display
- Sortable table view
- Statistics dashboard
- Export to CSV functionality
- Clear all data option

## File Structure

```
csv_uploader/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Docker ignore file
├── .gitignore           # Git ignore file
├── Makefile             # Convenient Docker commands
├── test-docker.sh       # Docker setup test script
├── sample_data.csv      # Sample CSV file for testing
├── templates/
│   └── index.html        # Main HTML template
├── data/                # Persistent data directory (Docker)
└── csv_data.db          # SQLite database (created automatically)
```

## Docker Deployment

### Using Docker Compose (Recommended)

The easiest way to run the application is using Docker Compose:

```bash
# Build and start the application
docker-compose up --build

# Run in detached mode (background)
docker-compose up -d --build

# Stop the application
docker-compose down

# View logs
docker-compose logs -f

# Rebuild after code changes
docker-compose up --build --force-recreate
```

### Using Docker directly

```bash
# Build the image
docker build -t csv-uploader .

# Run the container
docker run -p 5000:5000 -v $(pwd)/data:/app/data csv-uploader

# Run in detached mode
docker run -d -p 5000:5000 -v $(pwd)/data:/app/data --name csv-uploader-app csv-uploader
```

### Docker Features

- **Persistent Storage**: SQLite database is stored in the `./data` directory
- **Health Checks**: Built-in health monitoring
- **Security**: Runs as non-root user
- **Sample Data**: Includes sample CSV file for testing
- **Production Ready**: Optimized for production deployment

### Environment Variables

You can customize the application using environment variables:

```bash
# In docker-compose.yml or docker run command
environment:
  - FLASK_ENV=production
  - PORT=5000
```

## Development

To run in development mode:

```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

## Requirements

- Python 3.7+
- Flask 2.3.3
- Modern web browser

## Browser Support

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## License

This project is open source and available under the MIT License.
