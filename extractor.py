import struct, os

def extract_lua_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:4] != b'\x1bLua':
        return
    endian = data[6]
    szt_sz = data[8]
    fmt = "<" if endian == 1 else ">"
    seen = set()
    i = 0
    while i < len(data) - szt_sz:
        sz = struct.unpack_from(fmt + ("I" if szt_sz == 4 else "Q"), data, i)[0]
        if 2 <= sz <= 512:
            candidate = data[i+szt_sz : i+szt_sz+sz-1]
            try:
                s = candidate.decode("utf-8")
                if s not in seen and len(s) > 3 and all(32 <= ord(c) < 127 or c in '\n\r\t' for c in s):
                    seen.add(s)
                    print(f"  {s}")
            except:
                pass
        i += 1

base = os.path.expanduser("~/path/to/squashfs-root")
files = [ #edit these paths according to location of your LUA files, example path:
    "usr/lib/lua/luci/model/tmp_decrypt.lua",
    "usr/lib/lua/luci/controller/discover.lua",
    "usr/lib/lua/luci/model/sync.lua",
    "usr/lib/lua/luci/model/crypto.lua",
    "usr/lib/lua/luci/model/accountmgnt.lua",
    "usr/lib/lua/luci/sgi/tmp.lua",
]

for f in files:
    print(f"\n{'='*60}\n{f}\n{'='*60}")
    extract_lua_strings(f"{base}/{f}")
