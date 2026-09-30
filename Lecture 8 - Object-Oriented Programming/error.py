class MyError(BaseException):
    def __init__(self):
        super().__init__('hello world')

raise MyError