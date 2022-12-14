
def main_context(request):
   
    return {
        'domain' : request.META['HTTP_HOST'],
        
    }