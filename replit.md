# ResuMatch - Automated Resume Relevance Check System

## Overview

ResuMatch is a Streamlit-based web application that automates the evaluation of resume relevance against job descriptions. The system provides recruiters with objective scoring, detailed analysis, and candidate feedback generation capabilities. It combines rule-based matching with AI-powered semantic analysis to deliver comprehensive resume evaluation services.

The application processes resumes in PDF and DOCX formats, extracts structured data using NLP techniques, and generates relevance scores using a weighted formula that considers must-have skills (50%), nice-to-have skills (20%), experience/education fit (20%), and projects/certifications (10%). The system outputs scores on a 0-100 scale with High (80+), Medium (60-79), and Low (<60) verdicts.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
The application uses Streamlit as the web framework with a multi-page architecture organized through component modules. The main application (`app.py`) serves as the entry point with sidebar navigation routing to four core pages: Job Description Management, Resume Upload & Processing, Results Dashboard, and Candidate Feedback. Each page is implemented as a separate component module for maintainability and separation of concerns.

### Backend Architecture
The system follows a modular parser-evaluator architecture:

**Parser Layer**: Separate parsers handle job descriptions (`JDParser`) and resumes (`ResumeParser`). The resume parser supports PDF (PyMuPDF) and DOCX extraction with spaCy integration for NLP processing. The JD parser uses AI-powered extraction to structure job requirements.

**Evaluation Engine**: The `ResumeEvaluator` implements a hybrid scoring approach combining fuzzy string matching for skills assessment with AI-powered semantic analysis. The evaluator applies weighted scoring based on project requirements and generates detailed feedback with missing skills identification.

**Text Processing**: A utility layer provides text cleaning, normalization, and extraction functions for emails, phone numbers, and structured content parsing.

### Data Storage Solutions
The application uses Streamlit's session state as an in-memory database solution for prototyping and development. All data (job descriptions, resumes, evaluations, and processing queues) is stored in session state dictionaries with UUID-based identification. This approach provides immediate functionality without external database dependencies while maintaining data structure for future database migration.

The data models include:
- Job descriptions with structured requirements and metadata
- Resume storage with extracted text and parsed information
- Evaluation results with scores, verdicts, and detailed analysis
- Processing queues for batch operations

### Authentication and Authorization
Currently implements a simple session-based system through Streamlit's built-in session management. No explicit authentication layer is present, making it suitable for internal tools or demo environments.

## External Dependencies

**AI Services**: Google Gemini API (gemini-2.5-flash/gemini-2.5-pro) for intelligent job description parsing, semantic analysis, and candidate feedback generation. The API key is managed through environment variables.

**Document Processing**: 
- PyMuPDF (fitz) for PDF text extraction
- python-docx for DOCX document processing
- spaCy with English language model (en_core_web_sm) for natural language processing

**Text Analysis**: FuzzyWuzzy library for fuzzy string matching and skills comparison with configurable similarity thresholds.

**Data Visualization**: Plotly for interactive charts and graphs in the results dashboard, providing pie charts, bar graphs, and statistical visualizations.

**Core Framework**: Streamlit for the web interface with pandas for data manipulation and analysis operations.

The system is designed to be easily extensible with database backends (the architecture supports future Drizzle/Postgres integration) and additional AI providers for evaluation and feedback generation.