import pprint

def corsmiddleware(get_response):

    def middleware(request):
        response = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Request-Headers"] = "Content-Type"
        response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
        response["Access-Control-Allow-Methods"] = "POST"
        response["Allow"] = "POST"
        
        # print(response.META)

        return response
 
    return middleware