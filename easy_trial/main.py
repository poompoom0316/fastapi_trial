from fastapi import FastAPI, status, Body, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello world"}


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    '''
    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code just enables
    the GitHub Actions to rollback to the last version the project was
    found in a "working condition". It acts as a last line of defense in
    case something goes south.
    Additionally, it also returns a JSON response in the form of:
    {
        'healtcheck': 'Everything OK!'
    }
    '''
    return {'healthcheck': 'Everything OK!'}


# redirect
@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")


class Item(BaseModel):
    p1: float
    p2: float
    p3: float


# add
@app.get("/add")
async def add(item: Item = Depends()):
    add_result = add_func(**item.dict())
    return {"add_result": add_result}

# square
@app.get("/square")
async def add(item: float):
    add_result = item**2
    return {"add_result": add_result}

# square_add
@app.get("/square_add")
async def add(item1: float, item2: float):
    add_result = item1**2 + item2**2
    return {"add_result": add_result}

def add_func(p1, p2, p3):
    return p1 + p2 + p3
