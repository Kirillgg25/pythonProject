# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     filename="logs.log", filemode="w",
#                     format="We have next logging message: "
#                            "%(asctime)s:%(levelname)s-%(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
#
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")
#
# assert 2+2 == 5, "Wrong assert"

# """
# >>> assrtion
# result
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# """
# >>> 2+2
# 5
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result