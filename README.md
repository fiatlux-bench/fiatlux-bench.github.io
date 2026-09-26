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

Two captions are load-bearing and must not be loosened: the `S02stance` and
`S10stance` frames show the robot **holding** an on-ladder stance after being placed
there by IK, with no leg joints in the action space. They are not climbs and not
achievability takes. The four climbing subtasks are dashed because those results are
outstanding, not zero.

## Updating

Edit and push to `main`; GitHub Pages serves the repo root.

To refresh the paper PDF after a rebuild:

```bash
cp ../fiatlux-report-2026-q3/.claude/worktrees/feat-57-arxiv-version/root.pdf \
   static/paper/fiatlux.pdf
```

## Credits

Page structure adapted from the [Nerfies](https://github.com/nerfies/nerfies.github.io)
project page template, used under CC BY-SA 4.0.
