"""Pull GSC data focused on SYSTEMology book + chapter-related queries.

Reuses OAuth token from ../seo-audit/seo_token.json.

Outputs:
  04-gsc-rankings.md — markdown report with key tables
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as OAuthCredentials
from googleapiclient.discovery import build

HERE = Path(__file__).parent
TOKEN_FILE = HERE.parent.parent / "seo-audit" / "seo_token.json"
OAUTH_SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]
GSC_SITE = "sc-domain:systemology.com"

# Keywords we care about for the book launch
BOOK_KEYWORDS = [
    "systemology",
    "book",
    "pdf",
    "free",
    "download",
    "ccf",
    "critical client flow",
    "systems champion",
    "systemise",
    "systemize",
    "systemisation",
    "documenting",
    "sop",
    "extract",
    "minimum viable systems",
    "mvs",
    "e-myth",
    "process documentation",
    "business systems",
    "work on the business",
    "david jenyns",
]

# Stage names for chapter-mapping
STAGE_KEYWORDS = ["define", "assign", "extract", "organise", "organize",
                  "integrate", "scale", "optimise", "optimize"]


def get_creds():
    if not TOKEN_FILE.exists():
        print(f"ERROR: token file missing: {TOKEN_FILE}")
        sys.exit(1)
    creds = OAuthCredentials.from_authorized_user_file(str(TOKEN_FILE), OAUTH_SCOPES)
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(TOKEN_FILE, "w") as f:
                f.write(creds.to_json())
        else:
            print("ERROR: token invalid and not refreshable. Re-run seo-audit OAuth.")
            sys.exit(1)
    return creds


def query_gsc(service, dimensions, days=90, row_limit=10000, dim_filter=None):
    end = datetime.now().strftime("%Y-%m-%d")
    start = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": row_limit,
    }
    if dim_filter:
        body["dimensionFilterGroups"] = [{"filters": [dim_filter]}]
    rows = []
    start_row = 0
    while True:
        body["startRow"] = start_row
        resp = service.searchanalytics().query(siteUrl=GSC_SITE, body=body).execute()
        chunk = resp.get("rows", [])
        if not chunk:
            break
        rows.extend(chunk)
        if len(chunk) < row_limit:
            break
        start_row += row_limit
    return rows


def matches_book_intent(query):
    q = query.lower()
    return any(kw in q for kw in BOOK_KEYWORDS) or "systemolog" in q


def matches_stage(query):
    q = query.lower()
    if "systemolog" not in q and "system" not in q:
        return None
    for stage in STAGE_KEYWORDS:
        if stage in q:
            return stage
    return None


def main():
    creds = get_creds()
    service = build("searchconsole", "v1", credentials=creds)

    print("Pulling GSC data for systemology.com (last 90 days)...")

    # 1. Top queries overall
    print("  - top queries...")
    queries = query_gsc(service, ["query"], days=90, row_limit=5000)

    # 2. Query + page (so we know which page absorbs each query — cannibalisation map)
    print("  - query + page combos...")
    qpage = query_gsc(service, ["query", "page"], days=90, row_limit=10000)

    # 3. Pages with traffic
    print("  - top pages...")
    pages = query_gsc(service, ["page"], days=90, row_limit=2000)

    print(f"  Pulled: {len(queries)} queries, {len(qpage)} q+page combos, {len(pages)} pages")

    # Filter for book-relevant
    book_queries = [r for r in queries if matches_book_intent(r["keys"][0])]
    book_qpage = [r for r in qpage if matches_book_intent(r["keys"][0])]

    # Sort by impressions desc
    book_queries.sort(key=lambda r: r.get("impressions", 0), reverse=True)
    book_qpage.sort(key=lambda r: r.get("impressions", 0), reverse=True)

    # Stage-keyword map
    stage_map = {}
    for r in book_qpage:
        s = matches_stage(r["keys"][0])
        if s:
            stage_map.setdefault(s, []).append(r)

    # Build report
    out = []
    out.append("# GSC Rankings — SYSTEMology Book Launch (last 90 days)")
    out.append(f"\nPulled: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    out.append(f"\nSite: `{GSC_SITE}`")
    out.append(f"\nTotals: {len(queries)} queries, {len(book_queries)} book-relevant.\n")

    # Top book-relevant queries
    out.append("\n## Top 50 book-relevant queries (by impressions)\n")
    out.append("| Query | Clicks | Impressions | Position | CTR |")
    out.append("|---|---:|---:|---:|---:|")
    for r in book_queries[:50]:
        q = r["keys"][0]
        out.append(
            f"| {q} | {int(r.get('clicks', 0))} | {int(r.get('impressions', 0))} "
            f"| {round(r.get('position', 0), 1)} | {round(r.get('ctr', 0) * 100, 1)}% |"
        )

    # Top pages absorbing book intent
    out.append("\n## Pages currently absorbing book-related search intent\n")
    out.append("Top query→page assignments where the query is book-relevant. "
               "**These are cannibalisation candidates** — if /book/ launches, decide "
               "whether to redirect, canonicalise, or co-exist.\n")
    out.append("| Query | Page | Pos | Clicks | Impressions |")
    out.append("|---|---|---:|---:|---:|")
    for r in book_qpage[:60]:
        q = r["keys"][0]
        page = r["keys"][1].replace("https://www.systemology.com", "")
        out.append(
            f"| {q} | {page} | {round(r.get('position', 0), 1)} "
            f"| {int(r.get('clicks', 0))} | {int(r.get('impressions', 0))} |"
        )

    # Stage-by-stage targets
    out.append("\n## Per-stage chapter targets — current rankings\n")
    out.append("If a stage already ranks well via a blog post or page, that page "
               "should canonicalise to the chapter on launch.\n")
    for stage in STAGE_KEYWORDS:
        rows = stage_map.get(stage, [])
        if not rows:
            continue
        rows.sort(key=lambda r: r.get("impressions", 0), reverse=True)
        out.append(f"\n### {stage.title()} ({len(rows)} queries)\n")
        out.append("| Query | Page | Pos | Imp |")
        out.append("|---|---|---:|---:|")
        for r in rows[:10]:
            q = r["keys"][0]
            page = r["keys"][1].replace("https://www.systemology.com", "")
            out.append(
                f"| {q} | {page} | {round(r.get('position', 0), 1)} "
                f"| {int(r.get('impressions', 0))} |"
            )

    # Top systemology.com pages period
    pages.sort(key=lambda r: r.get("impressions", 0), reverse=True)
    out.append("\n## Top 30 systemology.com pages by impressions (all queries)\n")
    out.append("Watch for pages that ranks high but might be at risk if /book/ "
               "competes for the same intent.\n")
    out.append("| Page | Clicks | Impressions | Position |")
    out.append("|---|---:|---:|---:|")
    for r in pages[:30]:
        p = r["keys"][0].replace("https://www.systemology.com", "")
        out.append(
            f"| {p} | {int(r.get('clicks', 0))} | {int(r.get('impressions', 0))} "
            f"| {round(r.get('position', 0), 1)} |"
        )

    # Write
    output_path = HERE / "04-gsc-rankings.md"
    output_path.write_text("\n".join(out))
    print(f"\nWritten: {output_path}")

    # Also save raw JSON for follow-up
    raw = {
        "pulled_at": datetime.now().isoformat(),
        "queries": [{"q": r["keys"][0], **{k: r.get(k) for k in ["clicks", "impressions", "ctr", "position"]}} for r in queries],
        "book_queries": [{"q": r["keys"][0], **{k: r.get(k) for k in ["clicks", "impressions", "ctr", "position"]}} for r in book_queries],
        "book_qpage": [{"q": r["keys"][0], "page": r["keys"][1], **{k: r.get(k) for k in ["clicks", "impressions", "ctr", "position"]}} for r in book_qpage],
        "pages": [{"page": r["keys"][0], **{k: r.get(k) for k in ["clicks", "impressions", "ctr", "position"]}} for r in pages],
    }
    raw_path = HERE / "04-gsc-rankings.json"
    raw_path.write_text(json.dumps(raw, indent=2))
    print(f"Raw JSON: {raw_path}")


if __name__ == "__main__":
    main()
