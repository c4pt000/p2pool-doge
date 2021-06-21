import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

	      
P2P_PREFIX = 'd1d1d1d1'.decode('hex')
P2P_PORT = 9333
ADDRESS_VERSION = 60
ADDRESS_P2SH_VERSION = 22
HUMAN_READABLE_PART = 'radc'
RPC_PORT = 9332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
	    (yield helper.check_block_header(bitcoind, '000006ac2bd84266d6064bc8c47a222b9c68eb25c70aa6f13320fc7ed7f9e996')) and # genesis block
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))		         
#SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//100000
SUBSIDY_FUNC = lambda height: 50*1000000000000 >> (height + 1)//100000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'RADC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'RadioCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/RadioCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.radiocoin'), 'radiocoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/block/'
TX_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/tx/'
SANE_TARGET_RANGE = (2**256//1000000000000000 - 1, 2**256//1000 - 1)
#SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//500000 - 1)



DUMB_SCRYPT_DIFF = 2**15
DUST_THRESHOLD = 0.03e8
