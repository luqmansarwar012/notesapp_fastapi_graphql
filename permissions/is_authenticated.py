from resolvers.user_resolvers import verify_token
from strawberry.permission import BasePermission
from strawberry.types import Info
import typing


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context["request"]
        authorization_header = request.headers.get("Authorization")

        if authorization_header and authorization_header.startswith("Bearer "):
            token = authorization_header[len("Bearer ") :].strip()
            user_id = verify_token(token)
            if user_id:
                info.context["request"].user_id = user_id
                return True

        return False
