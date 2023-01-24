import json

class TestApiCase():
    def test_api_main(self, api):
        res = api.get('/api')
        assert res.status == '200 OK'
        assert res.json['message'] == "Welcome to the images API"

    def test_get_images(self, api):
        res = api.get('api/images')
        assert res.status == '200 OK'
        assert len(res.json) == 2
    
    def test_get_image(self, api):
        res = api.get('api/images/2')
        assert res.status == '200 OK'
        assert res.json['id'] == 2
        assert res.json['title'] == "Paradise"

    def test_get_image_error(self, api):
        res = api.get('api/images/9999')
        assert res.status == '404 NOT FOUND'
        assert "image with id 9999" in res.json['message']
    
    def test_post_images(self, api):
        mock_data = json.dumps({'title': 'test_image', 'description': 'abc', 'url': '123'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('api/images', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_post_image_error(self, api):
        mock_data = json.dumps({'name': 'wrong_property_test'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('api/images', data=mock_data, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert "Wrong property given" in res.json['message']
    
    def test_put_existing_image(self, api):
        mock_data = json.dumps({'title': 'test_update', 'description': 'abc', 'url': '123'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put('api/images/2', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
        assert res.json['title'] == 'test_update'
        assert res.json['description'] == 'abc'
        assert res.json['url'] == '123'

    def test_put_new_data(self, api):
        mock_data = json.dumps({'title': 'test_update_new', 'description': 'abc', 'url': '123'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put('api/images/9111', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 9111
        assert res.json['title'] == 'test_update_new'
        assert res.json['description'] == 'abc'
        assert res.json['url'] == '123'

    def test_put_error(self, api):
        mock_data = json.dumps({'title': 'test_update_new', 'description': 'abc', 'url': '123', 'name': 'zyx'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put('api/images/1', data=mock_data, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert "Wrong property given" in res.json['message']
        
    def test_delete_image(self, api):
        res = api.delete('api/images/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('api/unknown')
        assert res.status == '404 NOT FOUND'
        assert 'Oops' in res.json['message']