from fastapi import FastAPI
from pydantic import BaseModel

from client import home_get, home_post, kit_post, kits_get, recipe_post, recipies_get, stock_needings
from producer import map_get_areas, map_get_variables, stock_get, stock_needs_get, stock_needs_post, calculator_post
import copy


app = FastAPI()

class Item(BaseModel):
    user: str
    nutricional_info: str
    number: str
    kit: str
    recipe: str

class UserGet(BaseModel):
    user: str

class UserPost(BaseModel):
    user: str
    nutricional_info: str
    number: int

class RecipePost(BaseModel):
    recipe: str

class StockNeedings(BaseModel):
    user: str
    kit: str

class MapAreasGet(BaseModel):
    user: str

class MapVariablesGet(BaseModel):
    user: str
    area: str
    
class StockGet(BaseModel):
    user: str

class StockNeedsGet(BaseModel):
    pass

class StockNeedsPost(BaseModel):
    user: str
    food: str
    selling: int

class Profit(BaseModel):
    user: str
    wheight: int
    sample_area: int
    area: str

# Producer
    
@app.post("/producer/map_areas")
def map_get_areas_fast(item: MapAreasGet):
    event_andre={"body":"{\"usuario\":\""+item.user+"\"}"}
    return map_get_areas.handler_name(copy.deepcopy(event_andre), context = None)


@app.post("/producer/calculator")
def calculator_post_fast(item: Profit):
    event_andre={"body":"{\"usuario\":\""+item.user+"\", \"wheight\":\""+str(item.wheight)+"\", \"sample_area\":\""+str(item.sample_area)+"\", \"area\":\""+str(item.area)+"\"}"}
    return calculator_post.handler_name(copy.deepcopy(event_andre), context = None)


@app.post("/producer/map_variables")
def map_get_variables_fast(item: MapVariablesGet):
    event_andre={"body":"{\"usuario\":\""+item.user+"\", \"area\":\""+item.area+"\"}"}
    return map_get_variables.handler_name(copy.deepcopy(event_andre), context = None)


@app.post("/producer/stock")
def stock_get_fast(item: StockGet):
    event_andre={"body":"{\"usuario\":\""+item.user+"\"}"}
    return stock_get.handler_name(copy.deepcopy(event_andre), context = None)


@app.post("/producer/stock_needs/get")
def stock_needs_get_fast(item: StockNeedsGet):
    event_andre={"body":"[]"}
    return stock_needs_get.handler_name(copy.deepcopy(event_andre), context = None)


@app.post("/producer/stock_needs/post")
def stock_needs_post_fast(item: StockNeedsPost):
    event_andre={"body":"{\"usuario\":\""+item.user+"\", \"food\":\""+item.food+"\", \"selling\":\""+str(item.selling)+"\"}"}
    return stock_needs_post.handler_name(copy.deepcopy(event_andre), context = None)


# Client

@app.post("/client/home/get")
def home_get_fast(item: UserGet):
    event={"body":"{\"usuario\":\""+item.user+"\"}"}
    return home_get.handler_name(copy.deepcopy(event), context = None)



@app.post("/client/home/post") 
def home_post_fast(item: UserPost): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+str(item.number)+"\"}"}
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
def recipe_post_fast(item: RecipePost): #change
    event={"body":"{\"recipe\":\""+item.recipe+"\"}"}
    return recipe_post.handler_name(copy.deepcopy(event), context = None)

@app.post("/client/recipe/get") 
def recipe_get_fast(item: Item): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"nutricional_info\":\""+item.nutricional_info+"\", \"number\":\""+item.number+"\", \"kit_name\":\""+item.kit+"\", \"recipe\":\""+item.recipe+"\"}"}
    return recipies_get.handler_name(copy.deepcopy(event), context = None)


@app.post("/client/stock") 
def stock_needings_fast(item: StockNeedings): #change
    event={"body":"{\"usuario\":\""+item.user+"\", \"kit_name\":\""+item.kit+"\"}"}
    return stock_needings.handler_name(copy.deepcopy(event), context = None)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}