# fiatlux-bench.github.io

Project page for **Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing
and Light-Bulb Replacement**.

Live at <https://fiatlux-bench.github.io>.

## Layout

```
index.html              the whole page
static/css/style.css    visual system (shared with bushuyeu.github.io)
static/images/          frames from the teleoperated takes
static/paper/           fiatlux.pdf (arXiv build, non-anonymous)
static/video/           fiatlux.mp4 (ICRA 2027 accompanying video, 2:58, 17 MB)
.nojekyll               serve files as-is, no Jekyll pass
```

## Where the content comes from

Prose and numbers are lifted from the arXiv build of the paper. The benchmark code
is the source of truth for every number; the page must not diverge from the paper.

| Page section | Source |
| --- | --- |
| Abstract, contributions | `sections/01-intro.tex`, `root.tex` |
| Subtask weights and takes | `sections/04-results.tex`, Table `tab:fiatlux_takes` |
| Baseline table | `sections/04-results.tex`, Table `tab:fiatlux_groot` |
| Scoring, observation modes | `sections/03-method.tex` |
| Acknowledgements | `sections/07-acknowledgements.tex` |
| Teaser video | `feat-60-video-submission` worktree, `video/current/final/` |

Two captions are load-bearing and must not be loosened: the `S02stance` and
`S10stance` frames show the robot **holding** an on-ladder stance after being placed
there by IK, with no leg joints in the action space. They are not climbs and not
achievability takes. The four climbing subtasks are dashed because those results are
outstanding, not zero.

## Updating

Edit and push to `main`; GitHub Pages serves the repo root.

**After editing `static/css/style.css`, run `python3 stamp.py` before committing.**
It rewrites the stylesheet link with a hash of the file's contents. GitHub Pages
sends `cache-control: max-age=600` on every file and the header cannot be changed,
so the HTML and the CSS expire independently. Without the stamp a visitor can hold
new markup against a ten-minute-old stylesheet, which has broken this page's layout
more than once.

To refresh the paper PDF after a rebuild:

```bash
cp ../fiatlux-report-2026-q3/.claude/worktrees/feat-57-arxiv-version/root.pdf \
   static/paper/fiatlux.pdf
```

To refresh the video, and regenerate its poster frame:

```bash
cp ../fiatlux-report-2026-q3/.claude/worktrees/feat-60-video-submission/\
video/current/final/fiatlux_icra2027_video.mp4 static/video/fiatlux.mp4
ffmpeg -ss 40 -i static/video/fiatlux.mp4 -frames:v 1 -q:v 3 \
   static/images/video_poster.jpg -y
```

The video is served from the repo, not YouTube. Keep it under 100 MB (git's
per-file ceiling); the whole published site must stay under 1 GB.

## Credits

Page structure adapted from the [Nerfies](https://github.com/nerfies/nerfies.github.io)
project page template, used under CC BY-SA 4.0.
