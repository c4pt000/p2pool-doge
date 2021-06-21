from p2pool.bitcoin import networks

PARENT = networks.nets['radiocoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 10 # blocks
IDENTIFIER = 'ff37d5b8c6923410'.decode('hex')
PREFIX = 'dd08c1a53ef629b0'.decode('hex')
P2P_PORT = 9334
MIN_TARGET = 2**256//50 - 1
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 9555
BOOTSTRAP_ADDRS = [
	'194.195.117.160',
	'172.105.77.251',
	'194.195.250.123',
	'172.104.167.106',
	'139.162.80.22'
        ]
ANNOUNCE_CHANNEL = ''
VERSION_CHECK = lambda v: None if 1140300 <= v else 'radiocoin version too old. Upgrade to 5.0.2 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65','csv','segwit' ])
MINIMUM_PROTOCOL_VERSION = 70015
SEGWIT_ACTIVATION_VERSION = 0
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
