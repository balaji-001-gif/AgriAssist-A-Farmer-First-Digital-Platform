import frappe
from frappe import _

import requests
import json

@frappe.whitelist()
def ask_synth(query=None, image_data=None):
    """
    AI Agronomist logic using OpenAI Vision API (gpt-4o-mini).
    Reads 'openai_api_key' from site_config.json.
    """
    if not query and not image_data:
        return {"status": "error", "error": "Query or image is required."}
        
    api_key = frappe.conf.get("openai_api_key")
    if not api_key:
        return {
            "status": "error", 
            "error": "OpenAI API key is missing. Please ask your administrator to add 'openai_api_key' to the site configuration."
        }

    prompt = query if query else "Please analyze this crop image and identify any visible diseases, pests, or deficiencies. Provide agronomic advice."
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    content = [{"type": "text", "text": prompt}]

    if image_data:
        # Assuming the frontend strips the prefix, we re-attach it for OpenAI
        # If the frontend didn't strip it, we might need to handle it, but standard is base64 string
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{image_data}",
                "detail": "auto"
            }
        })

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are 'Synth', an expert AI Agronomist for the Agri Assist platform. Provide concise, helpful, and highly accurate agricultural advice."
            },
            {
                "role": "user",
                "content": content
            }
        ],
        "max_tokens": 800
    }
    
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=60)
        
        if response.status_code == 401:
            return {"status": "error", "error": "Invalid OpenAI API key. Please check your site configuration."}
            
        response.raise_for_status()
        
        result = response.json()
        ai_text = result["choices"][0]["message"]["content"]
        
        return {
            "status": "success",
            "response": ai_text
        }
        
    except requests.exceptions.ConnectionError:
        return {"status": "error", "error": "Could not connect to OpenAI. Please check your internet connection."}
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
