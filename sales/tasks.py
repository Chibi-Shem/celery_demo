from celery.task.schedules import crontab
from celery.decorators import periodic_task
import requests
from bs4 import BeautifulSoup
import unidecode
import re
from .models import Sales

from celery.contrib import rdb


# @periodic_task(run_every=60)
@periodic_task(run_every=(crontab(hour=0, day_of_week=0)))
def scrape_data():
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1wr_SrGLev-SZvCFEABqo_PWQlmpi9HynO9iJ9T-qIUM/edit#gid=0'
    page = requests.get(spreadsheet_url)

    soup = BeautifulSoup(page.content, 'html5lib')
    table = soup.find_all("table")[0]
    scraped_data = ([[td.text for td in row.find_all("td")] for row in table.find_all("tr")][1])[0]
    decoded_data = unidecode.unidecode(scraped_data)
    listed_data = re.split(';"|""|";"',decoded_data)
    fields = ['date',
            'sales_organic',
            'sales_ppc',
            'units_organic',
            'units_ppc',
            'orders',
            'refunds',
            'promo_value',
            'sponsored_products',
            'headline_search',
            'giftwrap',
            'shipping',
            'refund_cost',
            'commission',
            'compensated_clawback',
            'coupon_redemption_fee',
            'fba_inbound_transportation_fee',
            'fba_per_unit_fulfillment_fee',
            'fba_removal_fee',
            'fba_transportation_fee',
            'reversal_reimbursement',
            'sales_tax_collection_fee',
            'variable_closing_fee',
            'warehouse_damage',
            'warehouse_lost',
            'estimated_payout',
            'product_cost_sales',
            'product_cost_refunds',
            'product_cost_unsellable_refunds',
            'product_cost_non_amazon',
            'product_cost_missing_from_inbound',
            'gross_profit',
            'net_profit',
            'margin']
    finalized_data = {}
    index = 0
    for item in listed_data[34:]:
        finalized_data[fields[index]] = item
        index += 1
        if index == 34:
            Sales.objects.create(**finalized_data)
            index = 0
