from app.brewsite import app

def test_client():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Brewery" in response.data