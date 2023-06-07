from deta import Deta 
import os
import platform

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

current_platform = platform.system()
if  current_platform == 'Darwin' or current_platform == 'Windows' :
    DETA_KEY = os.getenv("DETA_KEY")
else:
    KVUri = "https://kv-deta-key.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    DETA_KEY = client.get_secret("DETA-KEY")

deta = Deta(DETA_KEY)

db = deta.Base("monthly_reports")

def insert_period(period, incomes, expenses, comment):
    return db.put({"key":period, "incomes":incomes, "expenses":expenses, "comment": comment})

def fetch_all_periods():
    res = db.fetch()

    return res.items


def get_period(period):
    return db.get(period)

