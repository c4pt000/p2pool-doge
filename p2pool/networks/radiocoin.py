from p2pool.bitcoin import networks

PARENT = networks.nets['radiocoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 9333
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = [
	'104.237.145.126',
	'194.195.117.160',
	'172.105.77.251',
	'194.195.250.123',
	'172.104.167.106',
	'139.162.80.22'
        ]
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: None if 1140300 <= v else 'radiocoin version too old. Upgrade to 3.0.0 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv' ])
MINIMUM_PROTOCOL_VERSION = 3301
SEGWIT_ACTIVATION_VERSION = 17
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
