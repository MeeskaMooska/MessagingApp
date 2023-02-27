# Server promts client sign in info
# if client has local config file, it will be parsed and pass and user will be sent to server
# if not client will prompt the user to create new sign in information

# Server will locally store its own config

from cryptography.fernet import Fernet

key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='

message = "75RJM202y299U8a34fYGjojPAlP3nfzb"
encoded = message.encode()

f = Fernet(key)
encoded = f.encrypt(encoded)
print(encoded)

print(f.decrypt(b'gAAAAABj-8wQJdDy2y_QD-Q_zHv98h_lhVgEcdnIbWf3tGqY2j035sIOuy-SuAwq4TvTgccvNLrWPrPlMMe-6G024rDYYt1vqJ_Pj_9xHJWkGnC-sDDCYyBZ2Opocr36jJNHbh6O4MDH').decode('utf-8'))
