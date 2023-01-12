import uvicorn
from fastapi import FastAPI,status,HTTPException
from fastapialchemycollector import setup, MetisInstrumentor, PlanCollectType
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
from database import engine 
import models
import os

app=FastAPI()

class Item(BaseModel): #serializer
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:

        orm_mode=True


db=SessionLocal()

METIS_API_KEY = os.environ.get("METIS_API_KEY")
METIS_SERVICE_NAME = os.environ.get("METIS_SERVICE_NAME")

instrumentation: MetisInstrumentor = setup(METIS_SERVICE_NAME,
                      api_key=METIS_API_KEY,
                      service_version=METIS_SERVICE_NAME
                      )

instrumentation.instrument_app(app, engine)

@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")



    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )


    

    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.description=item.description
    item_to_update.on_offer=item.on_offer

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete

if __name__ == "__main__":
    port = int(os.environ.get("PORT")) or 8080
    uvicorn.run(app, host="0.0.0.0", port=port)
