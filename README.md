# Skill Observatory 🚀

A **Multi-Agent Chatbot Framework** for Skills and Job Market Analytics that leverages CrewAI, WebSocket technology, and OpenAI's GPT models to provide real-time insights into skills demand, job trends, and educational opportunities through an intelligent conversational interface.

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

Skill Observatory is a **production-ready Multi-Agent Chatbot Framework** designed, built, and deployed as a complete workflow POC using CrewAI with WebSocket support for real-time interactions. The system leverages OpenAI's GPT models for advanced NLP tasks and provides comprehensive insights into the job market and skills landscape.

### 🏗️ **Core Architecture Highlights**

- **Multi-Agent Workflow**: Orchestrated agent collaboration using CrewAI framework
- **Real-time WebSocket Communication**: Instant bidirectional chat interactions
- **LangChain SQL Agent**: Natural language to SQL translation for database queries
- **Custom Visualization Tools**: Real-time chart generation (bar charts, pie charts)
- **Intelligent Reporting System**: Automated PDF report generation with visual insights
- **AWS Cloud Deployment**: Production-ready infrastructure with scalability

### 📊 **Key Capabilities**

- **Skills in Demand**: Current and trending skills across industries
- **Job Market Trends**: Employment opportunities and requirements
- **Educational Insights**: Course offerings and learning paths
- **Industry Analysis**: Sector-specific skill requirements
- **Geographic Trends**: Regional job and skill patterns
- **Real-time Visualizations**: Dynamic chart generation embedded in chat
- **Professional Reports**: Downloadable PDF reports with insights and visuals

## ✨ Features

### 🤖 **Multi-Agent Chatbot Framework**
- **CrewAI Orchestration**: Coordinated multi-agent workflow for complex task processing
- **Real-time WebSocket Communication**: Instant bidirectional responses to user queries
- **Intelligent Query Classification**: Automatically categorizes queries into greetings, data-related, or irrelevant
- **Natural Language Processing**: Advanced NLP using OpenAI's GPT models for query understanding

### 🔍 **LangChain SQL Agent Integration**
- **Natural Language to SQL Translation**: Converts conversational queries to precise SQL statements
- **Structured Data Retrieval**: Efficient querying of skills demand and supply data from relational databases
- **Dynamic Query Generation**: Context-aware SQL generation based on user intent

### 📊 **Real-time Visualization System**
- **Custom CrewAI Tools**: Specialized agents for chart generation and data visualization
- **Dynamic Chart Creation**: Automatic generation of bar charts, pie charts, and other visualizations
- **Embedded Visualizations**: Charts seamlessly integrated within the chatbot interface
- **Real-time Rendering**: Instant visual feedback based on query results

### 📋 **Intelligent Reporting Engine**
- **Automated Report Generation**: Compiles chatbot responses and visual insights into comprehensive reports
- **PDF Export Capability**: Downloadable professional reports for end-users
- **Multi-modal Content**: Text analysis combined with embedded visualizations
- **Structured Insights**: Organized presentation of data findings and recommendations

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
                       │   Multi-Agent   │
                       │   Workflow      │
                       └─────────────────┘
                                │
                                ▼
                ┌─────────────────────────────────┐
                │         Agent Specialists       │
                ├─────────────────────────────────┤
                │ • Query Classification Agent    │
                │ • SQL Generation Agent          │
                │ • Visualization Agent           │
                │ • Report Generation Agent       │
                └─────────────────────────────────┘
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

### AI/ML & Multi-Agent Framework
- **OpenAI GPT-4**: Advanced language model for natural language processing
- **LangChain**: Framework for developing applications with LLMs
- **CrewAI**: Multi-agent system for complex task orchestration and workflow management
- **LangChain SQL Agent**: Specialized agent for natural language to SQL translation
- **Custom CrewAI Tools**: Specialized tools for visualization and reporting tasks

### Visualization & Reporting
- **Matplotlib**: Data visualization library for chart generation
- **Pillow**: Image processing for chart generation and optimization
- **HTML Report Generation**: Structured insights presentation with embedded visualizations
- **PDF Report Export**: Professional report generation with visual insights
- **Real-time Chart Rendering**: Dynamic visualization generation within chat interface

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

### Multi-Agent Chatbot Interaction

The system uses a sophisticated multi-agent workflow where different specialized agents handle various aspects of your query:

1. **Query Classification Agent**: Determines the type and intent of your message
2. **SQL Generation Agent**: Converts natural language to database queries
3. **Visualization Agent**: Creates charts and visual representations
4. **Report Generation Agent**: Compiles comprehensive reports with insights



### Example Queries

The multi-agent system can handle various types of queries and automatically route them to the appropriate specialized agents:

- **Skills Analysis**: "Which skills are most in demand?" → SQL Agent + Visualization Agent
- **Job Trends**: "What are the trending job titles in technology?" → SQL Agent + Chart Generation
- **Educational Insights**: "What courses are available for data science?" → SQL Agent + Report Agent
- **Industry Analysis**: "What skills are required in the healthcare industry?" → Multi-agent workflow
- **Geographic Trends**: "What are the job opportunities in Dubai?" → SQL Agent + Visualization + Report
- **Complex Analytics**: "Compare demand for Python vs Java skills across different industries" → Full workflow

### Agent Workflow Example

```
User Query → Query Classification Agent → SQL Generation Agent → Database Query → 
Visualization Agent → Chart Generation → Report Generation Agent → Final Response
```

## 📚 API Documentation

### REST Endpoints

#### GET /
Health check endpoint for the multi-agent system
```bash
curl http://localhost:8000/
```

### Agent Communication Flow

```
1. User sends query via WebSocket
2. Query Classification Agent processes intent
3. SQL Generation Agent creates database queries
4. Visualization Agent generates charts (if applicable)
5. Report Generation Agent compiles final response
6. Response sent back via WebSocket with embedded visualizations
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


```

## 📊 Data Sources & Multi-Agent Processing

The platform integrates data from multiple authoritative sources and processes them through specialized agents:

### **Data Sources**
- **ESCO**: European Skills/Competences, qualifications and Occupations
- **Udacity**: Online learning platform and course data
- **EMSI**: Economic Modeling Specialists International
- **LinkedIn**: Job posting and employment data
- **UAE Universities**: Local educational institution data

### **Agent-Enhanced Data Processing**
- **Query Classification Agent**: Routes queries to appropriate data sources
- **SQL Generation Agent**: Creates optimized queries for relational databases
- **Visualization Agent**: Transforms raw data into meaningful charts and graphs
- **Report Generation Agent**: Synthesizes data from multiple sources into comprehensive insights



## 🏆 **Project Highlights**

This project demonstrates advanced implementation of:
- **Multi-Agent AI Systems** using CrewAI framework
- **Real-time WebSocket Communication** for interactive chatbot experiences
- **Natural Language to SQL Translation** using LangChain agents
- **Dynamic Visualization Generation** with embedded chart creation
- **Professional Report Generation** with PDF export capabilities
- **Production-Ready Deployment** on AWS infrastructure

---

**Made with ❤️ for the future of work and skills development**
