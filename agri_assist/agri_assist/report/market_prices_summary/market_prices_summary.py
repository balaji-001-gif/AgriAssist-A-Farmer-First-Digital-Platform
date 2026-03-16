# Copyright (c) 2024, Antigravity and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart(data)
	return columns, data, None, chart


def get_columns():
	return [
		{
			"fieldname": "commodity",
			"label": _("Commodity"),
			"fieldtype": "Link",
			"options": "Agri Commodity",
			"width": 200,
		},
		{
			"fieldname": "current_price",
			"label": _("Current Price"),
			"fieldtype": "Currency",
			"width": 150,
		},
		{
			"fieldname": "forecasted_price",
			"label": _("Forecasted Price"),
			"fieldtype": "Currency",
			"width": 150,
		},
		{
			"fieldname": "price_change",
			"label": _("Price Change"),
			"fieldtype": "Currency",
			"width": 150,
		},
		{
			"fieldname": "trend",
			"label": _("Trend"),
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname": "last_updated",
			"label": _("Last Updated"),
			"fieldtype": "Datetime",
			"width": 180,
		},
	]


def get_data(filters):
	data = frappe.db.sql(
		"""
		SELECT
			pf.commodity,
			pf.current_price,
			pf.forecasted_price,
			(pf.forecasted_price - pf.current_price) AS price_change,
			pf.trend,
			pf.last_updated
		FROM `tabAgri Price Forecast` pf
		ORDER BY pf.last_updated DESC
		""",
		as_dict=True,
	)

	return data


def get_chart(data):
	if not data:
		return None

	labels = [row.get("commodity") for row in data]
	current_prices = [row.get("current_price") or 0 for row in data]
	forecasted_prices = [row.get("forecasted_price") or 0 for row in data]

	return {
		"data": {
			"labels": labels,
			"datasets": [
				{
					"name": _("Current Price"),
					"values": current_prices,
				},
				{
					"name": _("Forecasted Price"),
					"values": forecasted_prices,
				},
			],
		},
		"type": "bar",
		"height": 300,
	}
