from client import home_get, home_post

if __name__ == "__main__":
    #home_get.handler_name(event={"body":"{\"usuario\":\"brunoartc\"}"}, context = None)
    home_post.handler_name(event={"body":"{\"usuario\":\"brunoartc\", \"nutricional_info\":\"Carboidratos\", \"number\":\"4\"}"}, context = None)