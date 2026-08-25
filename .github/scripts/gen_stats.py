#!/usr/bin/env python3
"""Generate assets/stats.svg from the GitHub API. Stdlib only, no dependencies."""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

USER = os.environ.get("STATS_USER", "Nikhiljai03")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.path.join("assets", "stats.svg")

LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178C6", "JavaScript": "#F1E05A",
    "HTML": "#E34C26", "CSS": "#663399", "Java": "#B07219", "C++": "#F34B7D",
    "C": "#555555", "Shell": "#89E051", "Dockerfile": "#384D54",
    "Makefile": "#427819", "Batchfile": "#C1F12E", "Jupyter Notebook": "#DA5B0B",
    "Go": "#00ADD8", "Rust": "#DEA584", "SCSS": "#C6538C", "Vue": "#41B883",
}
FALLBACK = ["#22D3EE", "#A78BFA", "#34D399", "#FBBF24", "#F472B6", "#60A5FA"]

MONO = 'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"'
SANS = 'font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"'


def api(path):
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-stats")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body)
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "profile-stats")
    req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect():
    user = api("/users/" + USER)

    repos, page = [], 1
    while True:
        chunk = api("/users/%s/repos?per_page=100&page=%d&type=owner" % (USER, page))
        repos.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1

    stars = sum(r["stargazers_count"] for r in repos if not r["fork"])

    langs = {}
    for r in repos:
        if r["fork"] or r["size"] == 0:
            continue
        try:
            for name, count in api("/repos/%s/%s/languages" % (USER, r["name"])).items():
                langs[name] = langs.get(name, 0) + count
        except urllib.error.HTTPError:
            continue

    contributions = 0
    if TOKEN:
        query = (
            "query($login:String!){user(login:$login){contributionsCollection"
            "{contributionCalendar{totalContributions}}}}"
        )
        try:
            res = graphql(query, {"login": USER})
            contributions = (res["data"]["user"]["contributionsCollection"]
                             ["contributionCalendar"]["totalContributions"])
        except Exception as err:  # stats are best-effort; never fail the build
            print("contributions lookup failed: %s" % err, file=sys.stderr)

    return {
        "repos": user["public_repos"],
        "followers": user["followers"],
        "stars": stars,
        "contributions": contributions,
        "code_bytes": sum(langs.values()),
        "langs": sorted(langs.items(), key=lambda kv: kv[1], reverse=True),
    }


def human_bytes(n):
    for unit, size in (("MB", 1024 ** 2), ("KB", 1024)):
        if n >= size:
            return "%.1f %s" % (n / float(size), unit)
    return "%d B" % n


def esc(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(data):
    top = data["langs"][:6]
    total = sum(n for _, n in top) or 1
    shares = [(name, n * 100.0 / total) for name, n in top]
    colors = [LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
              for i, (name, _) in enumerate(shares)]

    # Fourth tile adapts: vanity metrics only earn a slot once they say something.
    if data["stars"] >= 5:
        fourth = (data["stars"], "STARS EARNED", "#FBBF24")
    elif data["followers"] >= 25:
        fourth = (data["followers"], "FOLLOWERS", "#FBBF24")
    else:
        fourth = (human_bytes(data["code_bytes"]), "CODE SHIPPED", "#FBBF24")

    tiles = [
        (data["contributions"], "CONTRIBUTIONS / YR", "#22D3EE"),
        (data["repos"], "PUBLIC REPOS", "#A78BFA"),
        (len(data["langs"]), "LANGUAGES", "#34D399"),
        fourth,
    ]

    out = []
    out.append(
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="300" '
        'viewBox="0 0 900 300" role="img" aria-label="GitHub statistics for %s">' % esc(USER)
    )
    out.append(
        '<defs>'
        '<linearGradient id="cbg" x1="0" y1="0" x2="900" y2="300" gradientUnits="userSpaceOnUse">'
        '<stop offset="0" stop-color="#0A0E16"/><stop offset="1" stop-color="#0D131E"/>'
        '</linearGradient>'
        '<linearGradient id="crule" x1="0" y1="0" x2="900" y2="0" gradientUnits="userSpaceOnUse">'
        '<stop offset="0" stop-color="#22D3EE" stop-opacity="0.5"/>'
        '<stop offset="1" stop-color="#A78BFA" stop-opacity="0.05"/>'
        '</linearGradient>'
        '<pattern id="cgrid" width="26" height="26" patternUnits="userSpaceOnUse">'
        '<circle cx="1" cy="1" r="1" fill="#8FA0BF" fill-opacity="0.06"/>'
        '</pattern>'
        '<clipPath id="barclip"><rect x="30" y="196" width="840" height="14" rx="7"/></clipPath>'
        '</defs>'
    )
    out.append('<rect width="900" height="300" rx="13" fill="url(#cbg)"/>')
    out.append('<rect width="900" height="300" rx="13" fill="url(#cgrid)"/>')
    out.append('<rect x="0.5" y="0.5" width="899" height="299" rx="13" fill="none" stroke="#1E293B"/>')

    out.append('<text x="30" y="40" %s font-size="13" letter-spacing="4.5" fill="#22D3EE">SIGNALS</text>' % MONO)
    out.append('<text x="870" y="40" text-anchor="end" %s font-size="11.5" fill="#475569">updated %s</text>'
               % (MONO, datetime.now(timezone.utc).strftime("%Y-%m-%d")))
    out.append('<rect x="30" y="52" width="840" height="1" fill="url(#crule)"/>')

    x = 30
    for value, label, color in tiles:
        out.append('<rect x="%d" y="72" width="200" height="86" rx="10" fill="#0F1520" stroke="#1E293B"/>' % x)
        out.append('<rect x="%d" y="72" width="3" height="86" rx="1.5" fill="%s"/>' % (x, color))
        out.append('<text x="%d" y="118" %s font-size="30" font-weight="700" fill="#F1F5F9">%s</text>'
                   % (x + 20, SANS, esc(value)))
        out.append('<text x="%d" y="140" %s font-size="10.5" letter-spacing="1.8" fill="#64748B">%s</text>'
                   % (x + 20, MONO, esc(label)))
        x += 213

    out.append('<text x="30" y="184" %s font-size="11" letter-spacing="2.6" fill="#64748B">LANGUAGE DISTRIBUTION</text>' % MONO)
    out.append('<g clip-path="url(#barclip)">')
    bar_x = 30.0
    for (name, pct), color in zip(shares, colors):
        width = 840.0 * pct / 100.0
        out.append('<rect x="%.2f" y="196" width="%.2f" height="14" fill="%s"/>' % (bar_x, width + 0.5, color))
        bar_x += width
    out.append('</g>')
    out.append('<rect x="30" y="196" width="840" height="14" rx="7" fill="none" stroke="#0A0E16" stroke-width="1.5"/>')

    legend_x = 30
    for (name, pct), color in zip(shares, colors):
        out.append('<circle cx="%d" cy="248" r="4.5" fill="%s"/>' % (legend_x + 5, color))
        out.append('<text x="%d" y="252" %s font-size="12" fill="#CBD5E1">%s</text>'
                   % (legend_x + 17, MONO, esc(name)))
        out.append('<text x="%d" y="272" %s font-size="12" fill="#64748B">%.1f%%</text>'
                   % (legend_x + 17, MONO, pct))
        legend_x += 140

    out.append('</svg>')
    return "\n".join(out) + "\n"


def main():
    data = collect()
    os.makedirs("assets", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(render(data))
    print("wrote %s | repos=%d stars=%d contributions=%d langs=%d"
          % (OUT, data["repos"], data["stars"], data["contributions"], len(data["langs"])))


if __name__ == "__main__":
    main()
