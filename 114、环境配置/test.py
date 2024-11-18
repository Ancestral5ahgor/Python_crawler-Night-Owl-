import execjs

with open(
    r"D:\Code\DarkCatPython\JS_reverse\环境配置\test.js", "r", encoding="utf-8"
) as f:
    js_code = f.read()


ctx = execjs.compile(js_code).call("get_sign")
print(ctx)
