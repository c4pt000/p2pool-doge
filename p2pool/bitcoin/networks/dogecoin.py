import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

	      
P2P_PREFIX = 'c0c0c0c0'.decode('hex')
P2P_PORT = 22555
ADDRESS_VERSION = 30
ADDRESS_P2SH_VERSION = 50
HUMAN_READABLE_PART = 'doge'
RPC_PORT = 22556
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'radiocoin' in (yield bitcoind.rpc_help()) and # new versions have "radiocoinprivkey" but no "radiocoinaddress"
            (yield helper.check_block_header(bitcoind, '1a91e3dace36e2be3bf030a65679fe821aa1d6ef92e7c9902eb318182c355691')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'DOGE'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Dogecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dogecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dogecoin'), 'dogecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://live.blockcypher.com/doge/?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://live.blockcypher.com/doge/address/?'
TX_EXPLORER_URL_PREFIX = 'https://live.blockcypher.com/doge/tx/?'
SANE_TARGET_RANGE = (2**256//1000000000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
