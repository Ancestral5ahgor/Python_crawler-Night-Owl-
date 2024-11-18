# def test():
#     print("hello world")


# def learn():
#     print("learn python")


# a = [test, learn]

# # for i in a:
# #     i()


# def teach(m):
#     m()


# teach(learn)
# print(test)


def test():
    def learn():
        print("learn python")

    return learn


# a = test()
# a()

test()()
