from .models import Uzytkownicy

class UserMiddleware:
    """
    Middleware that attaches the user object to the request if a user_id is found in the session.

    Attributes:
        get_response (callable): The next middleware or view in the request chain.

    Methods:
        __init__(get_response): Initializes the middleware with the next middleware or view.
        __call__(request): Processes the request and attaches the user to it if a user_id is found in the session.
    """

    def __init__(self, get_response):
        """
        Initializes the middleware.

        Args:
            get_response (callable): The next middleware or view in the request chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Processes the request and attaches the user to it if a user_id is found in the session.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = Uzytkownicy.objects.get(pk=user_id)
                request.user = user
            except Uzytkownicy.DoesNotExist:
                pass

        response = self.get_response(request)
        return response
