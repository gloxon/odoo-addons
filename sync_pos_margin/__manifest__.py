# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'POS Margin & Rate',
    'version': '1.0',
    'summary': """Margins in Point of Sale
    This module adds the 'Margin' and 'Margin Rate' on Point Of Sale. This gives the profitability by calculating the difference between the Unit Price and Cost Price.
        Margin
        Sales
        
        POS
Point of Sale
POS product
Point of sale product
POS product margin
POS product rate
Sales product margin
Sales product rate
Inventory margin
Margin on pos
Margin on Point of Sales
Margin on product
Margin on rate
Sales margin
sales rate
Point of sales rate
point of sales margin
product sales margin
product sales rate
product margin
product categories margin
product categories rate

website
seller
product
seller product
best product
ecommerce product
ecommerce best seller
ecommerce best seller product
top selling product
top product
top selling ecommerce product
top selling website product
point of sale top selling product
point of sale top selling item
point of sale top product
point of sale top product selling
pos top selling product
post top selling item
pos top product
pos excel report
pos excel export
POS coupon
POS promotion
POS reward
point of sale coupon
point of sale promotion
point of sale reward
pos invoice
sale coupon
promotion
coupon
sale
product promotion
discount
sales discount
product discount
sales order discount
manufacturing
retailer
retail store
promo code
promotion code
coupon code
customer
customer discount
Reward
shipping
free shipping
fix price discount
percentage discount
promotion validity
minimum purchase
purchase
shoppers
Free product
Free item
free
coupon code validity
POS discount
special offer
festival
christmas
redemption
claim
expire
redeem
sale promotion
pos receipt
POS Promotional programm 
All in one
all in one coupon
all in one promo code
company logo
POS receipt
POS session
POS logo on session
POS logo on receipt
POS receipt company logo
POS receipt company address
POS session company logo
POS session company address
Point of sale company logo
point of sale receipt company logo
point of sale receipt logo
point of sale receipt address
point of sale session logo
    """,
    'description': """This module adds the 'Margin' and 'Margin Rate' on Point Of Sale. This gives the profitability by calculating the difference between the Unit Price and Cost Price.
        POS
        Margin
        Sales
    """,
    'author': 'Synconics Technologies Pvt. Ltd.',
    'website': 'http://www.synconics.com',
    'category': 'Point Of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'security/pos_security.xml',
        'views/res_config_settings_view.xml',
        'views/pos_order_view.xml',
        'reports/pos_report_view.xml',
    ],
    'demo': [],
    'images': ['static/description/main_screen.png'],
    'price': 15.0,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1'
}
