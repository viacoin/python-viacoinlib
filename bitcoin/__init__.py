# Copyright (C) 2012-2016 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.7.1-SNAPSHOT'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\x0f\x68\xc6\xcb'
    DEFAULT_PORT = 5223
    RPC_PORT = 5222
    DNS_SEEDS = (('viacoin.net', 'seed.viacoin.net'),
                 ('barbatos.fr', 'viaseeder.barbatos.fr'),
                 ('bootstap.viacoin.net', 'mainnet.viacoin.net'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':71,
                       'SCRIPT_ADDR':33,
                       'SECRET_KEY' :199}

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\xa9\xc5\xef\x92'
    DEFAULT_PORT = 25223
    RPC_PORT = 25222
    DNS_SEEDS = (('bootstrap-testnet.viacoin.net', 'testnet.viacoin.net'),
                 ('viacoin.net', 'seed-testnet.viacoin.net'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':127,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :255}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\x2d\x97\x7b5\x37'
    DEFAULT_PORT = 15224
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
