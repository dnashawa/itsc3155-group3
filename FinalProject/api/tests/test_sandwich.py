from fastapi.testclient import TestClient
from ..controllers import sandwiches as controller
from ..main import app
import pytest
from ..models import sandwiches as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_sandwiches(db_session):
    # Create a sample order
    sandwich_data = {
        "sandwich_name": "PBJ",
        "price": 2.50,
        "calories": 200,
        "tags": "kid-friendly, vegetarian"
    }

    sandwich_object = model.Sandwich(**sandwich_data)

    # Call the create function
    created_sandwich = controller.create(db_session, sandwich_object)

    # Assertions
    assert created_sandwich is not None
    assert created_sandwich.sandwich_name == "PBJ"
    assert created_sandwich.price == 2.50
    assert created_sandwich.calories == 200
