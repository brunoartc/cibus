from client import home_get, home_post, kit_post, kits_get, recipe_post, recipies_get, stock_needings
import copy

if __name__ == "__main__":
    event={"body":"{\"usuario\":\"brunoartc\", \"nutricional_info\":\"Carboidratos\", \"number\":\"4\", \"kit_name\":\"kit-foo\", \"recipe\":\"bananada\"}"}
    home_get.handler_name(copy.deepcopy(event), context = None)
    home_post.handler_name(copy.deepcopy(event), context = None)
    kit_post.handler_name(copy.deepcopy(event), context = None)
    kits_get.handler_name(copy.deepcopy(event), context = None)
    recipe_post.handler_name(copy.deepcopy(event), context = None)
    recipies_get.handler_name(copy.deepcopy(event), context = None)
    stock_needings.handler_name(copy.deepcopy(event), context = None)