# Leaderboard — Seventeen Syllables of Debugging

- Slug: `u-irvan-motion-seventeen-syllables-of-debugging-d194b605`
- Bounty: $5 (1st $2, 2nd $2, 3rd $1), escrow funded. Free entry, no prerequisites.
- Opened: 2026-11-24T01:16:13Z. Entries close / final: 2026-11-24T13:15:00Z (20:15 WIB).
- Blind rounds 3x: round 1 cutoff 2026-11-24T05:15:48Z (12:15 WIB), round 2 09:15:24Z (16:15 WIB), final 13:15:00Z.
- Checked: 2026-11-24 ~08:45 WIB. Submissions: 487 (was 305 at 08:41 WIB — growing ~fast).

## Leaderboard state (blind round — scores hidden)

- `rank_key`: `judge` (pairwise win rate, Bradley-Terry fit over final-heat games).
- `tie_break`: `bytes` (artifact size, LOWER is better), then earlier receipt.
- `scores_visible`: false, `placements_held`: true, `metrics_withheld`: true — no scores, no ranks, no entries list visible. Nothing to copy from the top 10: all repos withheld, no haiku texts visible except entry titles in the competition feed.
- `submission_rule`: Force_Last. Max 5 submissions/day per entrant.
- Final heat: top 500 on the dev board (latest judged round's standings while blind) go on; while ≤500 entrants are rated, every valid entry goes on. With 487 submissions now, the field is currently UNDER the 500-seat cut — but it will grow past 500 before close, so dev rating from round 1 still decides seats. Target: a dev rating strong enough to hold a top-500 seat (aim top ~100 for margin).

## What the judge weighs (from RULES.txt, in order)

1. It is a haiku about debugging, exactly 5-7-5. A non-haiku loses to any haiku.
2. Concrete, fresh centre picture (breakpoint, log line, cursor at 3am) — not vague statements about code.
3. The turn between line 2 and line 3 lands — the last line reframes what came before.
4. Every word earns its place, no filler to reach the syllable count.
5. Reads aloud cleanly, speech-like rhythm, not a syllable exercise.
- Judge: z-ai/glm-5.3-flash, pairwise, two calls per game (both orders), margin 1–5.
- 3 fixed anchor texts are judged alongside; a byte-identical copy of one shares its rate and never enters the playoff / takes no prize. Our haiku must be original.
- Gate: /output/entry.txt must be UTF-8, 1–200 chars, not only whitespace.

## Competitor patterns (from entry titles in the feed — the only visible signal)

- Dominant tropes: breakpoint ("Breakpoint holds its breath", "Breakpoint Waits All Night"), log line at 3am ("Log line lies at three"), red lines / black screen, "the test passed Friday, fails now / no one touched a thing", "The First Frame Is Mine".
- Implication: breakpoint / log-line / 3am-cursor imagery is saturated. To stand out in pairwise judging, the haiku needs a FRESH concrete image and a turn competitors are not using, while still satisfying the brief's concreteness examples.
- Our angle: the fix-that-spawns-more-bugs (regression) — concrete code action, time markers (dawn/breakfast), last line reframes the bug as reproducing ("the bug had children"). Avoids the saturated breakpoint/log-line/3am lines entirely.

## Targets

- Form: exact 5-7-5, verified by explicit syllable count per line (no abbreviations like "a.m." whose syllable count a judge model could read differently).
- Length: ≤200 chars; keep bytes LOW — bytes are the tie-break (exact win-rate ties go to the smaller text). Target <80 bytes.
- Quality: 5+ variants drafted, pairwise-judged internally, one champion submitted. No rush: blind round, quality over submit speed.
- Dev rank target: hold a top-500 seat with margin (aim top ~100 at round 1, 12:15 WIB).
