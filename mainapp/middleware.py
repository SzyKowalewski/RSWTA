from .models import Uzytkownicy


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                request.user = Uzytkownicy.objects.get(pk=user_id)
            except Uzytkownicy.DoesNotExist:
                request.user = None
        else:
            request.user = None
        response = self.get_response(request)
        return response
