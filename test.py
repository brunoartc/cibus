from client import home_get, home_post, kit_post, kits_get, recipe_post, recipies_get, stock_needings
from producer import map_get_areas, map_get_variables, stock_get, stock_needs_get, stock_needs_post
import copy

if __name__ == "__main__":
    event={"body":"{\"usuario\":\"brunoartc\", \"nutricional_info\":\"Carboidratos\", \"number\":\"4\", \"kit_name\":\"kit-foo\", \"recipe\":\"bananada\"}"}
    event_andre={"body":"{\"usuario\":\"andre\", \"food\":\"tomato\", \"area\":\"AreaTomato\", \"selling\":\"1\"}"}
    home_get.handler_name(copy.deepcopy(event), context = None)
    home_post.handler_name(copy.deepcopy(event), context = None)
    kit_post.handler_name(copy.deepcopy(event), context = None)
    kits_get.handler_name(copy.deepcopy(event), context = None)
    recipe_post.handler_name(copy.deepcopy(event), context = None)
    recipies_get.handler_name(copy.deepcopy(event), context = None)
    stock_needings.handler_name(copy.deepcopy(event), context = None)
    map_get_areas.handler_name(copy.deepcopy(event_andre), context = None)
    map_get_variables.handler_name(copy.deepcopy(event_andre), context = None)
    stock_get.handler_name(copy.deepcopy(event_andre), context = None)
    stock_needs_get.handler_name(copy.deepcopy(event_andre), context = None)
    stock_needs_post.handler_name(copy.deepcopy(event_andre), context = None)