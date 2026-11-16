def test_create_order(client):
    response = client.post(
        "/orders/",
        json={"customer_name": "Rahul", "product_name": "Laptop", "quantity": 2},
    )

    assert response.status_code == 201

    data = response.json()
    assert data["customer_name"] == "Rahul"
    assert data["product_name"] == "Laptop"
    assert data["quantity"] == 2
    assert data["status"] == "pending"


def test_get_all_orders(client):
    client.post(
        "/orders/",
        json={"customer_name": "Amit", "product_name": "Keyboard", "quantity": 3},
    )

    response = client.get("/orders/")

    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_single_order(client):
    created = client.post(
        "/orders/",
        json={"customer_name": "Neha", "product_name": "Mouse", "quantity": 1},
    ).json()

    response = client.get(f"/orders/{created['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_update_order_status(client):
    created = client.post(
        "/orders/",
        json={"customer_name": "Ravi", "product_name": "Monitor", "quantity": 2},
    ).json()

    response = client.patch(
        f"/orders/{created['id']}/status", json={"status": "processing"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "processing"


def test_delete_order(client):
    created = client.post(
        "/orders/",
        json={"customer_name": "Karan", "product_name": "Tablet", "quantity": 1},
    ).json()

    order_id = created["id"]

    response = client.delete(f"/orders/{order_id}")

    assert response.status_code == 200

    verify = client.get(f"/orders/{order_id}")
    assert verify.status_code == 404


def test_invalid_quantity(client):
    response = client.post(
        "/orders/",
        json={"customer_name": "Rahul", "product_name": "Laptop", "quantity": 0},
    )

    assert response.status_code == 422


def test_invalid_order_status(client):
    created = client.post(
        "/orders/",
        json={"customer_name": "Amit", "product_name": "Keyboard", "quantity": 1},
    ).json()

    response = client.patch(
        f"/orders/{created['id']}/status", json={"status": "unknown"}
    )

    assert response.status_code == 422


def test_nonexistent_order(client):
    response = client.get("/orders/999999")

    assert response.status_code == 404
