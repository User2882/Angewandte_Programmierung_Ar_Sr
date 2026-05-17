import requests

# alles hat funktioniert 6 passed, 1 warning


BASE_URL = "http://127.0.0.1:8000"

def test_create_note_rejects_short_title():
    response = requests.post(
        f"{BASE_URL}/notes",
        json={
            "title": "a",
            "content": "content",
            "category": "work",
            "tags": ["work"]
        }
    )
    assert response.status_code == 422

def test_create_note_rejects_unknown_category():
    response = requests.post(
        f"{BASE_URL}/notes",
        json={
            "title": "Valid title",
            "content": "content",
            "category": "banana",
            "tags": ["banana"]
        }
    )
    assert response.status_code == 422


def test_create_note_forbids_extra_fields():
    response = requests.post(
        f"{BASE_URL}/notes",
        json={
            "title": "Valid title",
            "content": "content",
            "category": "work",
            "tags": ["work"],
            "tagz": ["oops"]
        }
    )
    assert response.status_code == 422


def test_work_note_requires_work_tag():
    response = requests.post(
        f"{BASE_URL}/notes",
        json={
            "title": "Work note",
            "content": "content",
            "category": "work",
            "tags": ["urgent"]
        }
    )
    assert response.status_code == 422

def test_patch_with_empty_body_succeeds():
    create_resp = requests.post(
        f"{BASE_URL}/notes",
        json={
            "title": "Patch test",
            "content": "content",
            "category": "work",
            "tags": ["work"]
        }
    )
    note_id = create_resp.json()["id"]

    patch_resp = requests.patch(
        f"{BASE_URL}/notes/{note_id}",
        json={}
    )
    assert patch_resp.status_code == 200

def test_patch_with_invalid_title_fails():
    create_resp = requests.post(
        f"{BASE_URL}/notes",
        json={
            "title": "Patch test 2",
            "content": "content",
            "category": "work",
            "tags": ["work"]
        }
    )
    note_id = create_resp.json()["id"]

    patch_resp = requests.patch(
        f"{BASE_URL}/notes/{note_id}",
        json={"title": ""}
    )
    assert patch_resp.status_code == 422

