# HA Tag 4 - Test Cases for Notes API

import requests

BASE_URL = "http://127.0.0.1:8000"


def create_sample_note(payload=None):
    if payload is None:
        payload = {
            "title": "Test Note",
            "content": "Test content",
            "category": "Work",
            "tags": ["urgent", "meeting"]
        }
    return requests.post(f"{BASE_URL}/notes", json=payload)



# CRUD Tests alle =================================================


def test_create_note():
    response = create_sample_note()
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Note"
    assert "created_at" in data


def test_list_notes():
    response = requests.get(f"{BASE_URL}/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_note_by_id():
    create_resp = create_sample_note()
    note_id = create_resp.json()["id"]

    response = requests.get(f"{BASE_URL}/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["id"] == note_id


def test_update_note():
    create_resp = create_sample_note()
    note_id = create_resp.json()["id"]

    updated_data = {
        "title": "Updated Title",
        "content": "Updated content",
        "category": "Updated",
        "tags": ["updated"]
    }

    response = requests.put(f"{BASE_URL}/notes/{note_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_note():
    create_resp = create_sample_note()
    note_id = create_resp.json()["id"]

    delete_resp = requests.delete(f"{BASE_URL}/notes/{note_id}")
    assert delete_resp.status_code in [200, 204]

    get_resp = requests.get(f"{BASE_URL}/notes/{note_id}")
    assert get_resp.status_code == 404



# Filter Tests =================================================


def test_filter_by_category():
    create_sample_note({
        "title": "Work Note",
        "content": "Content",
        "category": "Work",
        "tags": []
    })

    response = requests.get(f"{BASE_URL}/notes?category=Work")
    assert response.status_code == 200

    for note in response.json():
        assert note["category"] == "Work"


def test_filter_by_search():
    create_sample_note({
        "title": "Meeting Note",
        "content": "Discuss project",
        "category": "Work",
        "tags": []
    })

    response = requests.get(f"{BASE_URL}/notes?search=meeting")
    assert response.status_code == 200


def test_filter_by_tag():
    response = requests.get(f"{BASE_URL}/notes?tag=urgent")
    assert response.status_code == 200


def test_combined_filters():
    response = requests.get(
        f"{BASE_URL}/notes?category=Work&tag=urgent&search=meeting"
    )
    assert response.status_code == 200


def test_date_filtering():
    response = requests.get(f"{BASE_URL}/notes?created_after=2000-01-01")
    assert response.status_code == 200



# Error Cases =================================================


def test_create_note_missing_fields():
    response = requests.post(f"{BASE_URL}/notes", json={
        "title": "Incomplete"
    })
    assert response.status_code == 422


def test_get_nonexistent_note():
    response = requests.get(f"{BASE_URL}/notes/99999")
    assert response.status_code == 404


def test_update_nonexistent_note():
    response = requests.put(f"{BASE_URL}/notes/99999", json={
        "title": "X",
        "content": "Y",
        "category": "Z",
        "tags": []
    })
    assert response.status_code == 404


def test_delete_nonexistent_note():
    response = requests.delete(f"{BASE_URL}/notes/99999")
    assert response.status_code == 404



# Tag 3 Hausaufgabe Features =======================================


def test_notes_statistics():
    response = requests.get(f"{BASE_URL}/notes/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_notes" in data
    assert "by_category" in data
    assert "top_tags" in data


def test_list_categories():
    response = requests.get(f"{BASE_URL}/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_notes_by_category():
    response = requests.get(f"{BASE_URL}/categories/Work/notes")
    assert response.status_code == 200



# PATCH Tests =================================================


def test_patch_note_title_only():
    create_resp = create_sample_note()
    note_id = create_resp.json()["id"]

    patch_resp = requests.patch(
        f"{BASE_URL}/notes/{note_id}",
        json={"title": "Only Title Changed"}
    )

    assert patch_resp.status_code == 200
    assert patch_resp.json()["title"] == "Only Title Changed"


def test_patch_multiple_fields():
    create_resp = create_sample_note()
    note_id = create_resp.json()["id"]

    patch_resp = requests.patch(
        f"{BASE_URL}/notes/{note_id}",
        json={
            "title": "Changed",
            "content": "Changed Content"
        }
    )

    assert patch_resp.status_code == 200