from fastapi.testclient import TestClient
import my_first_fastapi

client = TestClient(my_first_fastapi.app)

def test_first_fast_api():
    url = "/user/1002"
    resp = client.get(url)
    assert resp.text == '{"id":1002,"name":"name2","age":25,"gender":"female"}'