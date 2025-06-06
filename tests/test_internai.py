from fastapi.testclient import TestClient
from internai.app import app, candidates

client = TestClient(app)

def test_apply_and_list_candidates():
    candidates.clear()
    files = {'cv': ('cv.txt', 'python flask docker')}
    data = {'name': 'Alice', 'mission_id': 1}
    response = client.post('/apply', data=data, files=files)
    assert response.status_code == 200
    body = response.json()
    assert body['score'] == 100.0

    resp = client.get('/candidates')
    assert resp.status_code == 200
    all_candidates = resp.json()
    assert len(all_candidates) == 1
    assert all_candidates[0]['name'] == 'Alice'
