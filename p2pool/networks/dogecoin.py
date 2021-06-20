from p2pool.bitcoin import networks

PARENT = networks.nets['dogecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9335
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = [
'95.85.29.144',
'162.243.113.110',
'146.185.181.114',
'188.165.19.28',
'166.78.155.36',
'78.46.57.132'
        ]
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: None if 1140300 <= v else 'dogecoin version too old. Upgrade to 3.0.0 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv' ])
MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
