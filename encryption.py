# Server promts client sign in info
# if client has local config file, it will be parsed and pass and user will be sent to server
# if not client will prompt the user to create new sign in information

# Server will locally store its own config

from cryptography.fernet import Fernet

key = b'e9iRDX8f-2GiHwWi_toavUnscTwWz6AwVwdAf53y6wY='

message = "g195IkAfHvMi9KrgOCXCP3ixpuERKmW0XtDoR0asxL4or3gM0g972jJKTSwCw8hGBbqUQdTrj7FINUHDfGWGpePgiuoaYp6OImAyvGEdZY1ACYB2Z9OEUb64L0DoyOskBtS6suKW9BTJUNJbCbIf4nfEcX3VNVrCd3G5vDVyCRif4RJlcMiDhR1AjRETfyvdLfiKzuUoEtLflD4dWIulLPP2DGutm0tSe5Vh8QZytlRJHPS6NMvOhL9ZXOPEVDbOu3MG3cS0MgEJOKNWHrvEiu3x4NuJVd6Ab0Kgmi5W9OiiBbtXkweQ8SA0X4gLHzWwQWzrT9gG4YOy4HNNhF5QnyWd61ud2ZT0EKZMDgSqeWRdCQlGkZWtniwLcJ5DDcyyu5iq2letbjmlUOqNcavbJhai0z16tyxHCHoE6dsrhN4Q22yN2H0ozuDtz2E6LVrTVcZYvgE4pE0HhywQ8L24U0aeXiZM50uAZovOExUfMF8nAkFshvCNYD4tXZb3Dyfp23NJSVWmfrOsR8Itw7BUTofWK3CQN64omDcvNUKBo9WcdqagMoDmNsADKloCymzbAuHFYcLZpCwI0EKjnRXtc3T1bMKwOfM8A5tVEpdddga9TyYqdv1Q9MpTvjTpyaCT7wMUaDhLj5vaXT2M59y4mrUZjZC1eCRn4xMsG4giAWWRCKev7nueNMxuEMLOOWJJenNDlBskTmGT4oyLAZhSSLWa68poLWnRdriIKrzrlykTWVh7zGCnaGwm2kVJkiU6dZqsZxghQJsifHaeiXXOBU1wjmnhKl3BVL6BZDH1nWLptg0NdcSx9SMozTIJqbCWueysHyJn1doPuvrxakAyTiHKdu5TwzF0ZNEJf36nSxrLziIKuh53oxLlBy4otWgj5y8MsXFAWK6NQkT6ylARYI186bIZIBr9l8R6JNFOPBpy1tG1wZI5JJQfYCupZCIgbtManBwhbT4DicpSkFaLifxMGkp6BL1sedVdYsbIg195IkAfHvMi9KrgOCXCP3ixpuERKmW0XtDoR0asxL4or3gM0g972jJKTSwCw8hGBbqUQdTrj7FINUHDfGWGpePgiuoaYp6OImAyvGEdZY1ACYB2Z9OEUb64L0DoyOskBtS6suKW9BTJUNJbCbIf4nfEcX3VNVrCd3G5vDVyCRif4RJlcMiDhR1AjRETfyvdLfiKzuUoEtLflD4dWIulLPP2DGutm0tSe5Vh8QZytlRJHPS6NMvOhL9ZXOPEVDbOu3MG3cS0MgEJOKNWHrvEiu3x4NuJVd6Ab0Kgmi5W9OiiBbtXkweQ8SA0X4gLHzWwQWzrT9gG4YOy4HNNhF5QnyWd61ud2ZT0EKZMDgSqeWRdCQlGkZWtniwLcsdfsdsdfsdfsdsdfsdfsdfssdfsdBwhbT4DicpSkFaLifxMGkp6BL1sedVdYsbI"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)

print(len(encrypted), '\n', encrypted)
#print(f.decrypt(encrypted).decode('utf-8'))
