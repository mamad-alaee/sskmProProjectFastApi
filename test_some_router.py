from fastapi.testclient import TestClient
from app import originalApp



client = TestClient(originalApp)


def test_get_some_endpoint():
    res = client.get("/some_endpoint")
    assert res.status_code == 200
    assert res.json() == "ok"

def test_delete_some_endpoint():
    res = client.delete("/some_endpoint")
    assert res.status_code == 405
    assert res.json() == {"detail": "Method Not Allowed"}

    res = client.delete("/some_endpoint/ten")
    assert res.status_code == 422

    res = client.delete("/some_endpoint/10")
    assert res.status_code == 403
    assert res.json() == {"detail":"You are not allowed to delete this resource"}

    res = client.delete("/some_endpoint/21")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_post_some_endpoint():
    res = client.post("/some_endpoint")
    assert res.status_code == 400
    assert res.json() == {
                    "detail": [
                        " نام نمیتواند خالی باشد",
                        " سن باید عددی باشد"
                            ]
                    }
    res = client.post("/some_endpoint",data={"name": "ali", "age": "0"})
    assert res.status_code == 400
    assert res.json() == {
                            "detail": [
                                " سن باید بزرگتر از 0 باشد"
                            ]
                        }
    
