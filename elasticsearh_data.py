import requests
import json
import datetime
import logging
from threading import Thread
from queue import Queue
import glob
import os
import functools
headers = {"Content-Type":"application/json"}
path = r'C:\Users\Manikindi_shaik_Noor\Desktop\batool\esx-localhost-2020-07-16--10.31-2355077.tgz'


elastic_url = "http://%s/%s/%s" % (
    1.1.1.1:8080",
    "new_index_blob",
    "_doc/execution-b9aaa19c-c3b7-4925-94fc-bad39d0b1b91sosreport-MX5108N-A1-20200927083834.tar.xz"
)
import base64

try:
    with open(path, "rb") as f:
        bytes = f.read()
        encoded = str(base64.b64encode(bytes).decode("utf-8") )

    upload_data = {}
    upload_data["name"] = "esx-localhost-2020-07-16--10.31-2355077.tgz"
    upload_data["blob"] = encoded
except Exception as e:
    print(str(e))

try:
    # print(upload_data)
    resp_elastic = requests.put(
        elastic_url,
        headers=headers,
        data=json.dumps(upload_data),
        verify=False
    )
    print("ES Entry completed for {}".format(path))
except Exception as e:
    print(e)
