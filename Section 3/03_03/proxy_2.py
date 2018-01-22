class Blog:
    def read(self):
        print('Read the blog')

    def write(self):
        print('Write the blog')

class Proxy:
    def __init__(self, target):
        self.target = target

    def __getattr__(self, attr):
        return getattr(self.target, attr)

class AnonUserBlogProxy(Proxy):
    def __init__(self, blog):
        super().__init__(blog)
    def write(self):
        print('Only authorized users can write blog posts.')
