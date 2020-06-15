def aceleradev_middleware(get_response):

    def middleware(request):
        if request.method == 'GET':
            print('Metodo da requisicao é GET')
        print('=============================================')
        print('AceleraDev')
        response = get_response(request)
        print('Online na codenation')
        return response

    return middleware