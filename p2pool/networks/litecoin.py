from p2pool.bitcoin import networks

PARENT = networks.nets['litecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9326
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9327
BOOTSTRAP_ADDRS = [
        'crypto.office-on-the.net',
        'ltc.p2pool.leblancnet.us',
        '51.148.43.34',
        '68.131.29.131',
        '87.102.46.100',
        '89.237.60.231',
        '95.79.35.133',
        '96.255.61.32',
        '174.56.93.93',
        '178.238.236.130',
        '194.190.93.235',
        ]
ANNOUNCE_CHANNEL = '#p2pool-ltc'
VERSION_CHECK = lambda v: None if 100400 <= v else 'Litecoin version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
