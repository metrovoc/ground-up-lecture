# ground-up-lecture

An agent skill that turns any topic into a comprehensive, self-contained lecture, from the fundamentals to the deepest understanding, delivered as a single HTML file.

## Install

Clone this repository into your agent's skills directory, for example for Claude Code:

```sh
git clone https://github.com/metrovoc/ground-up-lecture ~/.claude/skills/ground-up-lecture
```

## Use

```
/ground-up-lecture <topic>
```

## Development

`dev/specimen.html` exercises every element the template styles. Serve it, rebuilt from `assets/template.html` on each reload:

```sh
python3 dev/preview.py
```
