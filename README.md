# Agri Assist Frappe App

A comprehensive, AI-powered digital platform for farmers, converted from the AgriAssist Next.js platform.

## Features
- **Farmer Dashboard**: Real-time overview of farm activities and market trends.
- **Market Price Forecast**: AI-powered commodity price forecasting.
- **Ask Synth**: AI Agronomist for crop disease diagnosis and advice.
- **Agri Marketplace**: Buy farm inputs and sell produce.
- **Knowledge Hub**: Expert guides and educational content.

## Conversion Details
This app was converted to follow Frappe/ERPNext v15 standards. 
- **Backend**: Python (Frappe Framework)
- **Frontend**: Frappe Portal (HTML/CSS/JS)
- **AI**: Integrated via `api.py` (planned for Google Gemini)

## Installation
1. Install Frappe Bench v15.
2. Get the app:
   ```bash
   bench get-app https://github.com/balaji-001-gif/AgriAssist-A-Farmer-First-Digital-Platform.git --branch frappe-conversion
   ```
3. Install on site:
   ```bash
   bench --site [your-site] install-app agri_assist
   ```
