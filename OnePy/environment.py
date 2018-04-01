from OnePy.event import EventBus
from OnePy.sys_model.containers import UsefulDict


class Environment(object):

    """全局要素"""
    tickers = []

    event_bus = EventBus()
    mod_dict = None
    readers = UsefulDict('Readers')
    feeds = UsefulDict('Feeds')
    cleaners = UsefulDict('Cleaners')
    strategies = UsefulDict('Strategies')
    brokers = UsefulDict('Brokers')
    risk_managers = UsefulDict('Risk_Managers')
    recorders = UsefulDict('Recorders')
    recorder = None

    signals_normal: list = []
    signals_trigger: list = []
    signals_current: list = []

    orders_mkt_original: list = []  # 保存最原始的所有market order
    orders_mkt_normal: list = []  # 动态的临时order
    orders_mkt_absolute: list = []
    orders_mkt_submitted: list = []

    orders_pending: list = []   # 保存动态挂单的pending
    orders_pending_mkt_dict: dict = {}  # 保存都动态的跟随已有market order 的pending

    logger = None
    buffer_days = None
    execute_on_close_or_next_open = 'open'

    hedge_mode = False
    live_mode = False

    _config = None

    event_loop = None

    gvar = None

    def refresh(self):

        self.signals_normal: list = []
        self.signals_trigger: list = []
        self.signals_current: list = []
        self.orders_mkt_original: list = []
        self.orders_mkt_normal: list = []
        self.orders_mkt_absolute: list = []
        self.orders_mkt_submitted: list = []
        self.orders_pending: list = []
        self.orders_pending_mkt_dict: dict = {}
