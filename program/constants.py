from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

# !!!! SELECT MODE !!!!
MODE = "PRODUCTION"

# Close all open positions and orders

ABORT_ALL_POSITIONS = False

# Find cointegrated pairs

FIND_COINTEGRATED = True

# Place Trades
MANAGE_EXITS = False

# Place Trades
PLACE_TRADES = False

# Resolution
RESOLUTION = "1HOUR"


# Stats Window
WINDOW = 21

# Tresholds - Opening
MAX_HALF_LIFE = 24 # Le temps moyen qu'il faut au Spread pour revenir à l'équilibre. Il faut chercher une valeur faible mais pas négative. idélamenet entre 0 et 24
ZSCORE_THRESH = 1.5 # 0 est l'équilibre, 1.5 est la valeur qui fonctionne le mieux (en valeur absolue). Il ouvre à +-1,5 et ferme au prochain +- 1,5. Sinon à 0
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880

# Tresholds - Closing
CLOSE_AT_ZSCORE_CROSS = False

# Ethereum Address
ETHEREUM_ADDRESS ="0x96478F27cB3172e60C151f21D3AC11f3f35C6411"


# KEYS - Proudction
# Must to be on Mainet on DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINET")
DYDX_API_PASSPHRASE_MAINNET  = config("DYDX_API_PASSPHRASE")

# KEYS - Developpement
# Must to be on Testnet on DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config ("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config ("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET  if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET  if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

# Host - Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/Oe1_tdwB3ySsO3GF0xDu37-jdAicCKkP"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/50boc9BBgwF9-Y4SNaJNnEJau8P0OgbA" 

HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET

