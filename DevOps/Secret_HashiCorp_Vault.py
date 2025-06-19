''' 
Utilisation de l'outil HashiCorp Vault via python
'''

import hvac

def get_secret(vault_url, token, secret_path):
    client = hvac.Client(url=vault_url, token=token)
    secret = client.secrets.kv.read_secret_version(path=secret_path)
    return secret['data']['data']

vault_url = 'http://127.0.0.1:8200'
token = input('Enter your HashiCorp Vault Token : ')
secret_path = input('Enter your HashiCorp secret_path : ')
secret = get_secret(vault_url, token, secret_path)
print(secret)
