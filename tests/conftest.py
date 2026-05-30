import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

# Initial state of activities for resetting between tests
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Team-based soccer practice and weekend matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["laura@mergington.edu", "nolan@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Skill drills, scrimmages, and friendly basketball competitions",
        "schedule": "Wednesdays and Fridays, 4:30 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["zach@mergington.edu", "ava@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and mixed media artistic projects",
        "schedule": "Mondays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["mia@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Practice acting, perform scenes, and prepare stage productions",
        "schedule": "Tuesdays and Fridays, 3:45 PM - 5:15 PM",
        "max_participants": 20,
        "participants": ["chloe@mergington.edu", "ethan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills for debate tournaments",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Design, build, and program robots for competitions and demonstrations",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["grace@mergington.edu", "henry@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """Test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities state before each test."""
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)