app_name = "agri_assist"
app_title = "Agri Assist"
app_publisher = "Antigravity"
app_description = "A comprehensive, AI-powered digital platform for farmers"
app_email = "agri@assist.app"
app_license = "mit"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/agri_assist/css/agri_assist.css"
# app_include_js = "/assets/agri_assist/js/agri_assist.js"

# include js, css files in header of web template
# web_include_css = "/assets/agri_assist/css/agri_assist.css"
# web_include_js = "/assets/agri_assist/js/agri_assist.js"

# include js in page
# page_js = {"page" : ["public/js/file.js"]}

# include js in doctype views
# doctype_js = {"doctype" : ["public/js/doctype.js"]}
# doctype_list_js = {"doctype" : ["public/js/doctype_list.js"]}
# doctype_tree_js = {"doctype" : ["public/js/doctype_tree.js"]}
# doctype_calendar_js = {"doctype" : ["public/js/doctype_calendar.js"]}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "agri_assist.install.before_install"
# after_install = "agri_assist.install.after_install"

# Uninstallation
# --------------

# before_uninstall = "agri_assist.uninstall.before_uninstall"
# after_uninstall = "agri_assist.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To setup dependencies during app install
# setup_wizard_requires = ["erpnext"]

# Website
# -------

portal_menu_items = [
	{"title": "Dashboard", "route": "/agri-dashboard", "role": "Farmer"},
	{"title": "Marketplace", "route": "/marketplace", "role": "Farmer"},
	{"title": "Ask Synth", "route": "/ask-synth", "role": "Farmer"},
	{"title": "Community", "route": "/community", "role": "Farmer"},
]

# Permissions
# -----------
# Permissions evaluated in Python
# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"agri_assist.tasks.all"
#	],
#	"daily": [
#		"agri_assist.tasks.daily"
#	],
#	"hourly": [
#		"agri_assist.tasks.hourly"
#	],
#	"weekly": [
#		"agri_assist.tasks.weekly"
#	],
#	"monthly": [
#		"agri_assist.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "agri_assist.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "agri_assist.event.get_events"
# }
#
# each method should have one argument to carry the dependencies
# auth_hooks = [
#	"agri_assist.auth.validate"
# ]

# Default (uncomment to enable)
# website_route_rules = [
# 	{"from_route": "/agri-dashboard", "to_route": "agri_assist/www/agri-dashboard"},
# ]
