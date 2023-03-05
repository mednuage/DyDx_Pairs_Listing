from func_messaging import send_message
with open('cointegrated_pairs.csv','r') as file:
    msg = file.read()
send_message(msg)