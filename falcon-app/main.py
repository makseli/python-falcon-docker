import falcon


class HelloWorldResource:
    # noinspection PyMethodMayBeStatic
    def on_get(self, request, response):
        print(request)
        response.media = ('Hello World from Falcon Python 3.6 app with' +
                          ' Gunicorn running in a docker container.')


app = falcon.API()
app.add_route('/', HelloWorldResource())
