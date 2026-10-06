---
name: ground-up-lecture
description: Turn any topic into a comprehensive, self-contained lecture, from the fundamentals to the deepest understanding, delivered as a single HTML file. Use only when explicitly asked to use ground-up-lecture.
---

Given a topic, deliver a comprehensive lecture on it, from the fundamentals to the deepest understanding.

- Make it fully self-contained: teach everything within the lecture itself, never deferring to external videos, books, or other resources.
- Keep it engaging and effortless to follow.
- No compromises on depth, breadth, or accessibility.
- Integrate interactive exercises, each substantial and well-placed.
- Exploit the browser boldly: imagine the most illuminating form each idea and exercise could take, then build it, however ambitious.

## The page

Start from [template.html](assets/template.html): copy it, fill in the title (in both `<title>` and the `<h1>`) and the subtitle, and write the lecture into `<main>` after the header. Deliver one standalone HTML file; it may load external resources.

The template already provides the following, so the lecture doesn't build its own:

- A contents panel built from the `h2`–`h4` headings, with ids generated when missing, so the lecture's outline lives in its headings. It highlights the section being read and docks beside the text on wide screens. Headings inside `figure`, `aside` or `details` stay out of it.
- A theme switch between system, light and dark, remembered across visits.
- Math: KaTeX renders `\( … \)`, `\[ … \]` and `$$ … $$`.
- A focus ring on whatever the reader reaches with the keyboard.
- Printing in light colors, with each `h2` starting a new page.
- Shorter CSS animations and transitions for readers who ask for reduced motion.

**Layout.** Design one layout, for a desktop window, and no alternatives for small screens; where something does not fit, scale it down as a whole. Small screens are not a priority, and shrinking keeps things correct, so put the effort into the desktop design. Text runs in a column capped at a comfortable reading width (`--measure`). Draw each figure at one fixed size that fits the column, with text at `var(--figure-text)` or larger.

**Theme.** Light and dark follow the system or the reader's toggle by swapping the template's color variables, so anything colored with them follows along. Give each new color a dark value as well, in both of the template's dark blocks. Drawing code that can't use CSS variables directly reads them with `getComputedStyle` and redraws on the `themechange` event the document fires.

## The look

Keep the template's look: a quiet, typographic page where headings carry the structure, color carries meaning, and surfaces stay flat. Design everything the lecture adds in the same language, so attention stays on the ideas and the page reads as one piece.

**Type.** Inter sets the text; JetBrains Mono sets code and numbers that update in place. Labels that aren't headings are small (12–14px), in sentence case, and set apart by weight or color, like the settings label in the template's own panel.

**Color.** The neutrals carry the page: `--bg`, `--surface`, `--surface-strong`, `--text`, `--text-muted`, `--border` and `--border-strong`. `--accent` marks what the reader can act on and terms being defined. `--success`, `--warning` and `--violet`, each with a pale `-bg` partner, mark kinds of content or feedback; give each a meaning once and keep it. `--series-1` to `--series-5` are for data in figures. Color that carries no meaning competes with the color that does, so leave it out.

**Surfaces.** Content and controls sit on the page, or on a flat tint (`--surface` or one of the `-bg` colors) with the page radius (`--radius`) and at most a hairline border. Shadows lift the template's floating panels above the page; content and controls stay on the page and have none.

**Motion.** Keep interface transitions brief, and let script-driven animation respect `prefers-reduced-motion` as the template's CSS does.

**Figures.** What a figure shows can use any visual means that carries information: a gradient that shades a surface, a color scale, motion. What surrounds it follows the page.

**Habits to avoid.** Machine-made web pages share a look that pulls attention from the content and makes a lecture look mass-produced: gradient fills, uppercase letter-spaced eyebrow labels, headings wrapped in banner cards, and cards with colored header strips, heavy borders or shadows. When the lecture needs something the template doesn't show, design it from the principles above rather than from these habits.
