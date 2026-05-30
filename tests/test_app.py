def test_get_activities(client):
    """Test GET /activities returns all activities with correct structure."""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()

    # Check that all expected activities are present
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data

    # Check structure of one activity
    chess_club = data["Chess Club"]
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_signup_for_activity(client):
    """Test POST /activities/{activity_name}/signup successfully registers a participant."""
    response = client.post("/activities/Chess%20Club/signup?email=newstudent@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "Signed up newstudent@mergington.edu for Chess Club" in data["message"]

    # Verify the participant was added
    response = client.get("/activities")
    activities = response.json()
    assert "newstudent@mergington.edu" in activities["Chess Club"]["participants"]


def test_duplicate_signup_returns_400(client):
    """Test POST /activities/{activity_name}/signup returns 400 for duplicate email."""
    # First signup
    client.post("/activities/Chess%20Club/signup?email=duplicate@mergington.edu")

    # Second signup with same email
    response = client.post("/activities/Chess%20Club/signup?email=duplicate@mergington.edu")
    assert response.status_code == 400
    data = response.json()
    assert "Participant already registered" in data["detail"]

    # Verify only one instance in participants
    response = client.get("/activities")
    activities = response.json()
    assert activities["Chess Club"]["participants"].count("duplicate@mergington.edu") == 1


def test_signup_nonexistent_activity_returns_404(client):
    """Test POST /activities/{activity_name}/signup returns 404 for invalid activity."""
    response = client.post("/activities/Nonexistent%20Activity/signup?email=test@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]


def test_unregister_participant(client):
    """Test DELETE /activities/{activity_name}/participants successfully removes a participant."""
    # First, add a participant
    client.post("/activities/Programming%20Class/signup?email=removeme@mergington.edu")

    # Now remove them
    response = client.delete("/activities/Programming%20Class/participants?email=removeme@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "Unregistered removeme@mergington.edu from Programming Class" in data["message"]

    # Verify they were removed
    response = client.get("/activities")
    activities = response.json()
    assert "removeme@mergington.edu" not in activities["Programming Class"]["participants"]


def test_unregister_nonexistent_participant_returns_404(client):
    """Test DELETE /activities/{activity_name}/participants returns 404 for missing participant."""
    response = client.delete("/activities/Chess%20Club/participants?email=notregistered@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Participant not found" in data["detail"]


def test_unregister_from_nonexistent_activity_returns_404(client):
    """Test DELETE /activities/{activity_name}/participants returns 404 for invalid activity."""
    response = client.delete("/activities/Nonexistent%20Activity/participants?email=test@mergington.edu")
    assert response.status_code == 404
    data = response.json()
    assert "Activity not found" in data["detail"]