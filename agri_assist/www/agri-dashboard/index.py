import frappe

def get_context(context):
    context.no_cache = 1
    context.farmer = frappe.get_doc("Agri Farmer", {"email": frappe.session.user}) if frappe.session.user != "Guest" else None
    context.market_prices = frappe.get_all("Agri Price Forecast", fields=["*"], limit=5)
    context.marketplace_items = frappe.get_all("Agri Marketplace Item", fields=["*"], limit=4)
    return context
