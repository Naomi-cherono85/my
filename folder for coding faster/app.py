with app.test_request_context('path', method='POST'):
        assert request.path == 'path'
        assert.method == 'POST'


 

