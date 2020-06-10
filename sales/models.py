from django.db import models

# Create your models here.
class Sales(models.Model):

    date = models.CharField(max_length=200, default='')
    sales_organic = models.CharField(max_length=200, default='')
    sales_ppc = models.CharField(max_length=200, default='')
    units_organic = models.CharField(max_length=200, default='')
    units_ppc = models.CharField(max_length=200, default='')
    orders = models.CharField(max_length=200, default='')
    refunds = models.CharField(max_length=200, default='')
    promo_value = models.CharField(max_length=200, default='')
    sponsored_products = models.CharField(max_length=200, default='')
    headline_search = models.CharField(max_length=200, default='')
    giftwrap = models.CharField(max_length=200, default='')
    shipping = models.CharField(max_length=200, default='')
    refund_cost = models.CharField(max_length=200, default='')
    commission = models.CharField(max_length=200, default='')
    compensated_clawback = models.CharField(max_length=200, default='')
    coupon_redemption_fee = models.CharField(max_length=200, default='')
    fba_inbound_transportation_fee = models.CharField(max_length=200, default='')
    fba_per_unit_fulfillment_fee = models.CharField(max_length=200, default='')
    fba_removal_fee = models.CharField(max_length=200, default='')
    fba_transportation_fee = models.CharField(max_length=200, default='')
    reversal_reimbursement = models.CharField(max_length=200, default='')
    sales_tax_collection_fee = models.CharField(max_length=200, default='')
    variable_closing_fee = models.CharField(max_length=200, default='')
    warehouse_damage = models.CharField(max_length=200, default='')
    warehouse_lost = models.CharField(max_length=200, default='')
    estimated_payout = models.CharField(max_length=200, default='')
    product_cost_sales = models.CharField(max_length=200, default='')
    product_cost_refunds = models.CharField(max_length=200, default='')
    product_cost_unsellable_refunds = models.CharField(max_length=200, default='')
    product_cost_non_amazon = models.CharField(max_length=200, default='')
    product_cost_missing_from_inbound = models.CharField(max_length=200, default='')
    gross_profit = models.CharField(max_length=200, default='')
    net_profit = models.CharField(max_length=200, default='')
    margin = models.CharField(max_length=200, default='')
