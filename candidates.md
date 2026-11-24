# Haiku candidates — Seventeen Syllables of Debugging

Syllable counts verified by hand, word by word. No abbreviations
("a.m.", "3am") — a judge model could count those differently.
All candidates are 5-7-5 and ≤200 characters.

## Candidate 1 — CHAMPION
```
One line fixed at dawn
a dozen break by breakfast
the bug had children
```
- Line 1: One(1) line(1) fixed(1) at(1) dawn(1) = 5
- Line 2: a(1) doz-en(2) break(1) by(1) break-fast(2) = 7
- Line 3: the(1) bug(1) had(1) chil-dren(2) = 5
- Total: 17 syllables, 70 bytes (incl. 2 newlines), 70 chars.
- Why it wins: complete arc (fix at dawn → a dozen break by breakfast
  → the bug reproduces). The last line reframes the bug as alive and
  breeding — a real debugging truth (regression) with a funny, memorable
  turn. Concrete actions, time markers, no saturated imagery
  (no breakpoint, no log line, no 3am cursor). Reads aloud cleanly.

## Candidate 2
```
A log line at three
says the server died at noon
noon was yesterday
```
- 5/7/5: A(1) log(1) line(1) at(1) three(1) / says(1) the(1) serv-er(2)
  died(1) at(1) noon(1) / noon(1) was(1) yes-ter-day(3). 68 bytes.
- Strong twist (the log is stale; the hunt was for a ghost) but the
  log-line-at-3am image is the brief's own example and saturated
  in the field. Loses to #1 on freshness.

## Candidate 3
```
Cursor blinks at three
a thousand log lines whisper
it was my typo
```
- 5/7/5: Cur-sor(2) blinks(1) at(1) three(1) / a(1) thou-sand(2) log(1)
  lines(1) whis-per(2) / it(1) was(1) my(1) ty-po(2). 68 bytes.
- Vivid middle line, but "it was my typo" is the most common debugging
  punchline — many entries will end that way. Loses to #1 on originality.

## Candidate 4
```
Rubber duck listens
I explain the bug aloud
and the bug gives up
```
- 5/7/5: Rub-ber(2) duck(1) lis-tens(2) / I(1) ex-plain(2) the(1)
  bug(1) a-loud(2) / and(1) the(1) bug(1) gives(1) up(1). 66 bytes.
- Real technique (rubber-duck debugging), but the trope is well known
  and the turn is soft — "gives up" does not reframe as sharply as
  "had children". Loses to #1.

## Candidate 5
```
Breakpoint, red dot, waits
the run halts, holding its breath
the bug walked right past
```
- 5/7/5: Break-point(2) red(1) dot(1) waits(1) / the(1) run(1)
  halts(1) hold-ing(2) its(1) breath(1) / the(1) bug(1) walked(1)
  right(1) past(1). 81 bytes.
- Good turn (the breakpoint is in the wrong place) but the breakpoint
  image is saturated — two competitor entry titles already use
  "Breakpoint holds its breath". Loses to #1; also longest (81 bytes,
  worst tie-break).

## Candidate 6
```
Git blame points at me
the commit is mine, timestamped
I'd do it again
```
- 5/7/5: Git(1) blame(1) points(1) at(1) me(1) / the(1) com-mit(2)
  is(1) mine(1) time-stamped(2) / I'd(1) do(1) it(1) a-gain(2).
- Fun defiance, but git blame is debugging-adjacent rather than
  debugging itself, and the turn is attitude, not a reframe.
  Loses to #1.

## Pairwise verdict
#1 beats #2 (fresher turn), #3 (more original ending), #4 (sharper
reframe), #5 (unsaturated image, fewer bytes), #6 (truer to debugging).
Champion: candidate 1.
