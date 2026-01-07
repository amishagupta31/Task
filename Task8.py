url_map = {}
counter = 1

def shorten(long_url):
    global counter
    if long_url in url_map.values():
        return [k for k, v in url_map.items() if v == long_url][0]
    short = f"url{counter}"
    url_map[short] = long_url
    counter += 1
    return short

def expand(short_url):
    return url_map.get(short_url, "Not found")

s = shorten("https://example.com/page/123")
print(s)
print(expand(s))
