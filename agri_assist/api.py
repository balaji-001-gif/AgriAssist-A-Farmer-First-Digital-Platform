import frappe
from frappe import _

import requests
import json

@frappe.whitelist()
def ask_synth(query=None, image_data=None):
    """
    AI Agronomist logic using local Ollama (LLaVA model).
    """
    if not query and not image_data:
        return {"status": "error", "error": "Query or image is required."}
        
    prompt = query if query else "Please analyze this crop image and identify any visible diseases, pests, or deficiencies."
    
    payload = {
        "model": "llava",
        "prompt": prompt,
        "stream": False
    }
    
    if image_data:
        payload["images"] = [image_data]
        
    try:
        # Call local Ollama API
        response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        ai_text = result.get("response", "I couldn't generate a response.")
        
        return {
            "status": "success",
            "response": ai_text
        }
        
    except requests.exceptions.ConnectionError:
        return {
            "status": "error", 
            "error": "Could not connect to the local AI engine. Please ensure Ollama is running (`ollama serve`)."
        }
    except Exception as e:
        frappe.log_error("Ask Synth API Error", str(e))
        return {
            "status": "error", 
            "error": f"An error occurred during AI analysis: {str(e)}"
        }

@frappe.whitelist()
def get_market_prices():
    """
    Fetch commodity prices and forecasts.
    """
    prices = frappe.get_all("Agri Price Forecast", fields=["commodity", "current_price", "forecasted_price", "trend"])
    return prices
