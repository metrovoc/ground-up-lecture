# ground-up-lecture

An agent skill that turns any topic into a comprehensive, self-contained lecture, from the fundamentals to the deepest understanding, delivered as a single HTML file.

## Install

The skill lives in `skills/ground-up-lecture`. Copy that directory into your agent's skills directory, for example for Claude Code:

```sh
git clone https://github.com/metrovoc/ground-up-lecture
cp -r ground-up-lecture/skills/ground-up-lecture ~/.claude/skills/
```

## Use

```
/ground-up-lecture <topic>
```

## Development

`dev/specimen.html` exercises every element the template styles. Serve it, rebuilt from `skills/ground-up-lecture/assets/template.html` on each reload:

```sh
python3 dev/preview.py
```
