# %%
import requests
import pandas as pd
import json
ACCESS_TOKEN = ''
# 
r=requests.get("https://api-qa.belcorp.biz/countries/", 
headers={"x-access-token":
ACCESS_TOKEN
})
# %%
dc = json.loads(r.content)
df_countries = pd.DataFrame(dc)

# %%
ls_campaigns=[]
for index, row in df_countries.iterrows():
    print(row["country_code"])
    url=f'https://api-qa.belcorp.biz/campaigns/{row["country_code"]}'
    print(url)
    r=requests.get(url, 
        headers={"x-access-token":
        ACCESS_TOKEN
        },
        params={"limit":"10"}
    )
    dc = json.loads(r.content)
    if dc.get("id"):
        ls_campaigns.append(dc)
df_campaigns = pd.DataFrame(ls_campaigns)

# %%
ls_catalog=[]
for index, row in df_countries.iterrows():
    print(row["country_code"])
    url=f'https://api-qa.belcorp.biz/catalogs/{row["country_code"]}'
    print(url)
    r=requests.get(url, 
        headers={"x-access-token":
        ACCESS_TOKEN
    })
    dc = json.loads(r.content)
    if dc.get("totalDocs"):
        ls_catalog.extend(dc["results"])
# %%
[cat["results"] for cat in ls_catalog]

# %%
df_catalog = pd.DataFrame(ls_catalog)
# %%
df_catalog.shape
# %%
df_catalog["country_iso"].value_counts()
# %%
df_catalog[df_catalog["country_iso"]=="PE"]["cover_image"]
# %%
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# %%
df_catalog.head()
# %%
url=f'https://api-qa.belcorp.biz/catalogs/BO/62dbf5fce8b97100205d4486/pages'
print(url)
r=requests.get(url, 
    headers={"x-access-token":
    ACCESS_TOKEN
})
# %%
dc =json.loads(r.content)
# %%
dc.keys()
# %%
dc
# %%
url=f'https://api-qa.belcorp.biz/campaigns/PE'
print(url)
r=requests.get(url, 
    headers={"x-access-token":
    ACCESS_TOKEN
    }
)
dc = json.loads(r.content)
dc
# %%
dc
# %%
url=f'https://api-qa.belcorp.biz/catalogs/PE?limit=100'
print(url)
r=requests.get(url, 
    headers={"x-access-token":
    ACCESS_TOKEN
})
dc =json.loads(r.content)
dc
# %%
622e5bd369c0950021e9b04c

#%%
url=f'https://api-qa.belcorp.biz/catalogs/PE/622e5bd369c0950021e9b04b'
print(url)
r=requests.get(url, 
    headers={"x-access-token":
    ACCESS_TOKEN
})
dc =json.loads(r.content)
dc
# %%
'brand_code': 'E'
'campaign_code': 202214,
'id': '62dc122821aed40022d2a0b0'