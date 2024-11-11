from config.database import initiate_database
from strawberry.fastapi import GraphQLRouter
from contextlib import asynccontextmanager
from mutations import Mutation
from fastapi import FastAPI
from queries import Query
import strawberry


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = await initiate_database()
    try:
        yield
    finally:
        client.close()


app = FastAPI(lifespan=lifespan)


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
