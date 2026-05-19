import copy

from fastapi.testclient import TestClient
from src.app import activities, app

original_activities = copy.deepcopy(activities)


def pytest_configure(config):
    # Ensure that the application state is reset between test runs.
    activities.clear()
    activities.update(copy.deepcopy(original_activities))


@pytest.fixture(autouse=True)
def restore_activities():
    activities.clear()
    activities.update(copy.deepcopy(original_activities))
    yield
    activities.clear()
    activities.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    return TestClient(app)
