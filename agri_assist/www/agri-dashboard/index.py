import frappe

def get_context(context):
    context.no_cache = 1
    context.farmer = None
    if frappe.session.user and frappe.session.user != "Guest":
        farmers = frappe.get_all("Agri Farmer", filters={"email": frappe.session.user}, limit=1)
        if farmers:
            context.farmer = frappe.get_doc("Agri Farmer", farmers[0].name)
    context.market_prices = frappe.get_all("Agri Price Forecast", fields=["*"], limit=5)
    context.marketplace_items = frappe.get_all("Agri Marketplace Item", fields=["*"], limit=4)
    return context
