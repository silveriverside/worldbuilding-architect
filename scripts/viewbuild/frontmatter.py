"""Minimal zero-dependency YAML front-matter parser.

Supports exactly the subset the worldbuilding codex uses:
  - scalars: `key: value`, quoted strings, integers, `null`
  - inline lists: `key: ["a", "b"]`
  - block lists of dicts:
        relations:
          - to: x
            type: y

This is NOT a general YAML parser. It is intentionally narrow and
deterministic so view generation needs no third-party packages.
"""


def parse_frontmatter(text):
    """Return (meta: dict, body: str, had_frontmatter: bool)."""
    if not text.startswith("---"):
        return {}, text, False
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text, False
    meta = _parse_block(lines[1:end])
    body = "\n".join(lines[end + 1:])
    return meta, body, True


def _split_top_commas(s):
    out, buf, quote = [], "", None
    for ch in s:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in ("'", '"'):
            quote = ch
            buf += ch
        elif ch == ",":
            out.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        out.append(buf)
    return out


def _scalar(v):
    v = v.strip()
    if v == "" or v.lower() == "null":
        return None
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_scalar(x) for x in _split_top_commas(inner)]
    try:
        return int(v)
    except ValueError:
        return v


def _collect_block(lines, start):
    """Parse an indented block list of dicts starting at `start`.

    Returns (items, consumed) or (None, 0) if it is not a `- ` list.
    """
    items, cur, found, i, n = [], None, False, start, len(lines)
    while i < n:
        raw = lines[i]
        if not raw.strip():
            i += 1
            continue
        if not raw.startswith(" "):
            break
        stripped = raw.strip()
        if stripped.startswith("- "):
            found = True
            if cur is not None:
                items.append(cur)
            cur = {}
            rest = stripped[2:].strip()
            if rest:
                k, _, val = rest.partition(":")
                cur[k.strip()] = _scalar(val)
        elif cur is not None:
            k, _, val = stripped.partition(":")
            cur[k.strip()] = _scalar(val)
        i += 1
    if cur is not None:
        items.append(cur)
    if not found:
        return None, 0
    return items, i - start


def _parse_block(lines):
    meta, i, n = {}, 0, len(lines)
    while i < n:
        raw = lines[i]
        if not raw.strip() or raw.lstrip().startswith("#"):
            i += 1
            continue
        if raw.startswith(" "):
            i += 1
            continue
        key, _, val = raw.partition(":")
        key, val = key.strip(), val.strip()
        if val == "":
            block, consumed = _collect_block(lines, i + 1)
            if block is not None:
                meta[key] = block
                i = i + 1 + consumed
                continue
            meta[key] = None
        else:
            meta[key] = _scalar(val)
        i += 1
    return meta
