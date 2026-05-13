# Lua Bytecode String Extractor

A lightweight Python utility for extracting embedded plaintext strings from compiled Lua bytecode files (`.luac`) commonly found in embedded firmware, routers, and IoT devices.

---

# Why this is useful

Many embedded systems ship Lua scripts as compiled bytecode instead of readable source code. Even when full decompilation fails due to:

- custom VM opcodes
- stripped debug info
- modified Lua interpreters
- unsupported Lua versions

the bytecode still often contains readable strings such as:

- API endpoints
- credentials/usernames
- debug messages
- file paths
- command strings
- crypto keys
- HTTP parameters
- router/web panel logic

This script scans raw Lua bytecode and extracts printable UTF-8 strings directly from the binary structure without requiring successful decompilation.

Useful for:

- firmware reverse engineering
- malware analysis
- embedded device auditing
- IoT security research
- quick triage of `.luac` files

---

# Features

- Detects Lua bytecode automatically (`\x1bLua`)
- Handles little/big endian Lua formats
- Supports 32-bit and 64-bit Lua string sizes
- Filters duplicate strings
- Extracts printable UTF-8 strings
- Works directly on extracted SquashFS firmware trees

---

# Requirements

- Python 3.x
- No external dependencies required

---

# Usage

Edit the `base` directory and Lua file paths:

```python
base = os.path.expanduser("~/path/to/squashfs-root")
```

Then run:

```bash
python3 extractor.py
```

Example output:

```text
============================================================
usr/lib/lua/luci/model/crypto.lua
============================================================
AES_ENCRYPT
Invalid password
/tmp/key.bin
admin
session_token
```

---

# Example Workflow

## 1. Extract firmware

```bash
binwalk -Me firmware.bin
```

## 2. Locate Lua bytecode files

```bash
find squashfs-root -type f | xargs file | grep Lua
```

## 3. Run the extractor

```bash
python3 extractor.py
```

---

# Notes

- This does **not** fully decompile Lua bytecode
- It only extracts embedded string constants
- Works best with Lua 5.1 / 5.2 style bytecode layouts
- Some vendor-modified Lua VMs may partially break extraction

---

# Use Cases

- Recover hidden API routes
- Find hardcoded credentials
- Discover undocumented features
- Identify command execution paths
- Analyze router web interfaces
- Extract indicators from malware Lua loaders

---

# Disclaimer

Use only on systems and firmware you are authorized to analyze.
