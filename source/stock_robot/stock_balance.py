# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class StockBalance(osv.osv):
    """
    资金状况
    """

    _name = "stock.balance"

    _columns = {
        'asset_balance': fields.float(u"资产总值", size=32, required=True),
        'current_balance': fields.float(u"当前余额", size=32, required=True),
        'enable_balance': fields.float(u"可用金额", size=32, required=True),
        'market_value': fields.float(u"证券市值", size=32, required=True),
        'money_type': fields.char(u"币种", size=10, required=True),
        'pre_interest': fields.float(u"预计利息", size=32, required=True),
    }