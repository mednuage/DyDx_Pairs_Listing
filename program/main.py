from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_dydx
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_messaging import send_message


# MAIN FUNCTION
if __name__ == "__main__":

  # Message on start
  send_message("Bot launch successful")

  # Connect to client
  try:
    print("Connecting to Client...")
    client = connect_dydx()
  except Exception as e:
    print("Error connecting to client: ", e)
    send_message(f"Failed to connect to client {e}")
    exit(1)


  # Find Cointegrated Pairs
  if FIND_COINTEGRATED:

    # Construct Market Prices
    try:
      print("Fetching market prices, please allow 3 mins...")
      df_market_prices = construct_market_prices(client)
    except Exception as e:
      print("Error constructing market prices: ", e)
      send_message(f"Error constructing market prices {e}")
      exit(1)

    # Store Cointegrated Pairs
    try:
      print("Storing cointegrated pairs...")
      stores_result = store_cointegration_results(df_market_prices)
      with open('cointegrated_pairs.csv','r') as file:
         msg = file.read()
      send_message(msg)
      
      if stores_result != "saved":
        print("Error saving cointegrated pairs")
        exit(1)
    except Exception as e:
      print("Error saving cointegrated pairs: ", e)
      send_message(f"Error saving cointegrated pairs {e}")
      exit(1)

  