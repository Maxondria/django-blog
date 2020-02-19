class TestFunctionMixin(object):
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
 