from typing import Annotated
from fastapi import FastAPI, Form, Query, Path
from fastapi.testclient import TestClient

app=FastAPI()

@app.post("/form-test")
async def form_test(
    str_data: Annotated[str, Form(example="prova", examples=["HELLO"])],
    query_data: Annotated[int, Query(examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])],
    path_data: Annotated[int, Path(examples=[1,1,3])],

):
    print("stop")
    return

client = TestClient(app)

def test_form_test_example_appear_in_openapi_json():
    print("markup-placeholder")
    client
    #TODO try to change the openapi.json file to see if the example is there
    # add a field with visible example value