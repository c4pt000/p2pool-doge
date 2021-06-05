import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 9333
ADDRESS_VERSION = 48
ADDRESS_P2SH_VERSION = 50
HUMAN_READABLE_PART = 'radc'
RPC_PORT = 9332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'radiocoin' in (yield bitcoind.rpc_help()) and # new versions have "radiocoinprivkey" but no "radiocoinaddress"
            (yield helper.check_block_header(bitcoind, '000008f3108b9b62492a71ff55f58f90678baf0ddeb75d11480f9355df6d1204')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'RADC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'RadioCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/RadioCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.radiocoin'), 'radiocoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/block-height/?'
ADDRESS_EXPLORER_URL_PREFIX = ''
TX_EXPLORER_URL_PREFIX = 'http://radioblockchain.info/tx/?'
SANE_TARGET_RANGE = (2**256//1000000000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
