# Claude Code AI-Native SDLC Learning Hub

A static learning site that teaches the AI-native software development lifecycle
with Claude Code: setup, core features, the six lifecycle stages, and hands-on
greenfield and brownfield simulators with runnable Python starters.

## Contents

- `index.html` – course home and learning paths
- `setup.html` – install, first session, features, security and worktrees
- `lifecycle.html` – plays and the six stages (Plan → Maintain)
- `practice.html` – greenfield and brownfield simulators
- `reference.html` – learning loop, pilot, glossary and FAQ
- `labs/` – artifact templates, starters and worked solutions (Python 3.10+, no dependencies)
- `assets/` – shared dark theme stylesheets, adapted from the
  [AIDLC Onboarding Hub](https://github.com/kaweween/AIDLC-onboarding)

## Preview locally

```
python -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765/>. No build step is required.

## Run a lab

Copy one `labs/<case>/starter` folder to a new directory outside this checkout,
then run `python -B -m unittest -v`. To compare with the worked solution, copy
the matching `solution` files over a fresh starter copy and run the tests again.

## Publishing

Enable GitHub Pages with source `main` / root (requires an account or organization plan that supports Pages for this repository's visibility). The site uses relative links, so it works at any base path. After a push, check that
the stylesheet loads, both simulators open, step deep links work, and the
starter and solution links resolve.
