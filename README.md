# Skill Observatory 🚀

An AI-powered Skills and Job Market Analytics Platform that provides real-time insights into skills demand, job trends, and educational opportunities through an interactive chat interface.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Skill Observatory is a comprehensive analytics platform that leverages AI and machine learning to provide insights into the job market and skills landscape. The system processes natural language queries and generates detailed reports with visualizations to help users understand:

- **Skills in Demand**: Current and trending skills across industries
- **Job Market Trends**: Employment opportunities and requirements
- **Educational Insights**: Course offerings and learning paths
- **Industry Analysis**: Sector-specific skill requirements
- **Geographic Trends**: Regional job and skill patterns

## ✨ Features

### 🤖 AI-Powered Chat Interface
- **Real-time WebSocket Communication**: Instant responses to user queries
- **Intelligent Query Classification**: Automatically categorizes queries into greetings, data-related, or irrelevant
- **Natural Language Processing**: Converts conversational queries to SQL database queries

### 📊 Advanced Analytics
- **Dynamic Visualization**: Automatic generation of bar charts, pie charts, and other visualizations
- **Professional Reports**: HTML-formatted insights with structured data presentation
- **Multi-modal Output**: Text reports combined with interactive visualizations

### 🗄️ Data Integration
- **Multi-source Data**: Integrates data from ESCO, Udacity, EMSI, LinkedIn, and UAE universities
- **Real-time Database Queries**: PostgreSQL-powered analytics engine
- **Cloud Storage**: AWS S3 integration for visualization storage

### 🏗️ Scalable Architecture
- **Microservices Design**: Containerized components for easy scaling
- **Production Ready**: Docker and Docker Compose deployment
- **Load Balancing**: Nginx reverse proxy for optimal performance

## 🏛️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   FastAPI       │    │   PostgreSQL    │
│   (WebSocket)   │◄──►│   Backend       │◄──►│   Database      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   CrewAI        │
                       │   Agents        │
                       └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   AWS S3        │
                       │   Storage       │
                       └─────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **WebSocket**: Real-time bidirectional communication
- **PostgreSQL**: Robust relational database
- **SQLAlchemy**: Database ORM and query building

### AI/ML
- **OpenAI GPT-4**: Advanced language model for natural language processing
- **LangChain**: Framework for developing applications with LLMs
- **CrewAI**: Multi-agent system for complex task orchestration

### Visualization & Reporting
- **Matplotlib**: Data visualization library
- **Pillow**: Image processing for chart generation
- **HTML Report Generation**: Structured insights presentation

### Infrastructure
- **Docker**: Containerization platform
- **Docker Compose**: Multi-container orchestration
- **Nginx**: Reverse proxy and load balancer
- **Gunicorn**: WSGI HTTP Server
- **AWS S3**: Cloud storage for visualizations

### Development Tools
- **Python 3.11**: Programming language
- **Poetry**: Dependency management
- **Pydantic**: Data validation using Python type annotations

## 🚀 Installation

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- PostgreSQL database
- AWS S3 bucket (for visualization storage)
- OpenAI API key

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/skill-observatory.git
   cd skill-observatory
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp all.env.example all.env
   # Edit all.env with your configuration
   ```

4. **Configure database**
   ```bash
   # Set up PostgreSQL database and update connection details in all.env
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - API: http://localhost:8000
   - WebSocket: ws://localhost:8000/ws

## ⚙️ Configuration

### Environment Variables

Create an `all.env` file with the following variables:

```env
# Database Configuration
DATABASE_URI=your_postgres_host
DATABASE_USERNAME=your_username
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_database_name
PORT=5432

# OpenAI Configuration
openai_api_key=your_openai_api_key
api_key=your_openai_api_key

# AWS S3 Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
```

### Database Schema

The application uses two main tables:
- `supply_data_flat`: Skills supply data
- `demand_jobs_data_flat`: Job demand data

## 📖 Usage

### WebSocket Connection

Connect to the WebSocket endpoint and send JSON messages:

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onopen = function() {
    console.log('Connected to Skill Observatory');
};

ws.onmessage = function(event) {
    const response = JSON.parse(event.data);
    console.log('Received:', response);
};

// Send a query
ws.send(JSON.stringify({
    message: "What are the top skills in demand for software development?"
}));
```

### Example Queries

The system can handle various types of queries:

- **Skills Analysis**: "Which skills are most in demand?"
- **Job Trends**: "What are the trending job titles in technology?"
- **Educational Insights**: "What courses are available for data science?"
- **Industry Analysis**: "What skills are required in the healthcare industry?"
- **Geographic Trends**: "What are the job opportunities in Dubai?"

## 📚 API Documentation

### REST Endpoints

#### GET /
Health check endpoint
```bash
curl http://localhost:8000/
```

### WebSocket Endpoints

#### WebSocket /ws
Real-time chat interface for skill analytics

**Message Format:**
```json
{
    "message": "Your query here"
}
```

**Response Format:**
```json
{
    "message": "Response content or HTML report",
    "querry_flag": true/false
}
```

## 🚀 Deployment

### Production Deployment with Docker

1. **Build the Docker image**
   ```bash
   docker build -t skill-observatory .
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Monitor logs**
   ```bash
   docker-compose logs -f skill_observatory
   ```

### Environment-Specific Configurations

#### Development
```bash
docker-compose -f docker-compose.dev.yml up
```

#### Production
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 📊 Data Sources

The platform integrates data from multiple authoritative sources:

- **ESCO**: European Skills/Competences, qualifications and Occupations
- **Udacity**: Online learning platform and course data
- **EMSI**: Economic Modeling Specialists International
- **LinkedIn**: Job posting and employment data
- **UAE Universities**: Local educational institution data

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting PR





**Made with ❤️ for the future of work and skills development**
