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
			"fieldname": "subscription_tier",
			"label": _("Subscription Tier"),
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"fieldname": "farmer_count",
			"label": _("Number of Farmers"),
			"fieldtype": "Int",
			"width": 180,
		},
		{
			"fieldname": "percentage",
			"label": _("Percentage (%)"),
			"fieldtype": "Float",
			"width": 150,
			"precision": 2,
		},
	]


def get_data(filters):
	tiers = frappe.db.sql(
		"""
		SELECT
			IFNULL(subscription_tier, 'Free') AS subscription_tier,
			COUNT(*) AS farmer_count
		FROM `tabAgri Farmer`
		GROUP BY subscription_tier
		ORDER BY farmer_count DESC
		""",
		as_dict=True,
	)

	total = sum(row.farmer_count for row in tiers)
	for row in tiers:
		row["percentage"] = (row.farmer_count / total * 100) if total else 0

	return tiers


def get_chart(data):
	if not data:
		return None

	return {
		"data": {
			"labels": [row.get("subscription_tier") for row in data],
			"datasets": [
				{
					"name": _("Farmer Count"),
					"values": [row.get("farmer_count") for row in data],
				}
			],
		},
		"type": "donut",
		"height": 300,
	}
