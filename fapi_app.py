from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

with open('data.json', 'r+') as data_file:
    data = json.load(data_file)


class item(BaseModel):
    item_name: str


class new_store(BaseModel):
    store_name: str
    items: list


## For Getting All Store
## URL eg. /getstores
## Type : GET
@app.get('/get_all_stores')
def get_all_stores():
    '''
    :return: all stores data
    '''
    return data


## For Getting All Items From Store
## URL eg. /getitemsofstore/store-1
## Type : GET
@app.get('/get_store/{store_name}')
def get_store(store_name):
    '''
    :param store_name:
    :return: store data
    '''
    for store in data:
        if store['name'] == store_name:
            return store
    return {'failed': 'store not found'}


## For Creating Item In Store
## URL eg. /createiteminstore/store-1
## Type : POST
## {"item_name": "cone" }
@app.post('/create_item_in_store/{store_name}')
def create_item(store_name, item: item):
    '''
    :param store_name:
    :param item:
    :return: item creation status
    '''
    for store in data:
        if store['name'] == store_name:
            if not item.item_name in store['items']:
                store['items'].append(item.item_name)
                with open('data.json', 'w') as file:
                    json.dump(data, file)
                return {'success': 'item created successfully'}
            else:
                return {'failed': 'item already exists'}
    return {'failed': 'store not found'}


## For Creating Store
## URL eg. /createstore
## Type : POST
## { "store_name":" ","items":[] }
@app.post('/create_store')
def create_store(new_store: new_store):
    '''
    :param new_store:
    :return: store creation status
    '''
    list_of_store_names = []
    for store in data:
        list_of_store_names.append(store['name'])
    if new_store.store_name not in list_of_store_names:
        new_store = {
            "name": new_store.store_name,
            "items": new_store.items
        }
        data.append(new_store)
        with open('data.json', 'w') as file:
            json.dump(data, file)
        return {'success': 'store created successfully'}
    else:
        return {'failed': 'store already exists'}



## For Creating Store
## URL eg. /delete_item_in_store/store_name
## Type : DELETE
## { "store_name":" ","items":[] }
@app.delete('/delete_item_in_store/{store_name}')
def delete_item(store_name, item: item):
    '''
    :param store_name:
    :param item:
    :return: item deletion status
    '''
    for store in data:
        if store['name'] == store_name:
            if item.item_name in store['items']:
                store['items'].remove(item.item_name)
                with open('data.json', 'w') as file:
                    json.dump(data, file)
                return {'success': 'item deleted successfully'}
            else:
                return {'failed': 'item not exists'}
    return {'failed': 'store not found'}
