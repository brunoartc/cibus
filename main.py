from fastapi import FastAPI
from pydantic import BaseModel

from client import home_get, home_post, kit_post, kits_get, recipe_post, recipies_get, stock_needings
from producer import map_get_areas, map_get_variables, stock_get, stock_needs_get, stock_needs_post
import copy


app = FastAPI()

class Item(BaseModel):
    user: str
    nutricional_info: str
    number: int
    kit: str
    recipe: str

class NutriInfo(BaseModel):
    user: str
    

@app.post("/client/home/get")
def home_get_fast(item: Item):
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return home_get.handler_name(copy.deepcopy(event), context = None)



@app.post("/client/home/post") 
def home_post_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return home_post.handler_name(copy.deepcopy(event), context = None)


@app.post("/client/kit/post") 
def kit_post_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return kit_post.handler_name(copy.deepcopy(event), context = None)


@app.post("/client/kit/get") 
def kit_get_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return kits_get.handler_name(copy.deepcopy(event), context = None)

@app.post("/client/recipe/post") 
def recipe_post_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return recipe_post.handler_name(copy.deepcopy(event), context = None)

@app.post("/client/recipe/get") 
def recipe_get_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return recipies_get.handler_name(copy.deepcopy(event), context = None)


@app.post("/client/recipe/get") 
def stock_needings_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return stock_needings.handler_name(copy.deepcopy(event), context = None)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}