from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"  # By default we pass the token to headers authorization as Token {token}, but after this it will be Bearer {token}
