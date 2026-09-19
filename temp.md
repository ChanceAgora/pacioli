# Pacioli: Technical Summary

## Overview

Pacioli is a small, dependency-free Python command-line application for recording study sessions and viewing aggregate study statistics. It stores data locally in `sessions.json`; there is no database, network layer, package configuration, or external service integration.

## Architecture and runtime flow

- `pacioli.py` is the entry point. `main()` initializes an empty JSON data file if necessary, prints the welcome message, repeatedly renders the menu, parses the user's numeric selection, and dispatches the selected operation.
- `menu.py` owns the CLI presentation and command registry. `mainMenuOptions` maps display labels to callable functions: show all statistics, summarize history, save a session, and quit.
- `use_data.py` implements the application/data operations:
  - `getSessionData()` prompts for a normalized topic and an integer duration.
  - `saveSession()` loads the JSON array, appends a session object, and writes it back.
  - `showAll()` prints the raw session history as formatted JSON.
  - `getSummary()` computes total minutes and minutes grouped by topic without mutating its input.
  - `summarize()` loads the history, computes the aggregate, and prints it.
- `utils.py` provides JSON file helpers: initialization of an empty file, loading, and overwriting/exporting data.
- `config.py` centralizes the relative data-file name (`sessions.json`).

The persisted schema is an array of objects shaped like `{ "topic": string, "minutes": integer }`. Summary output has the shape `{ "total_minutes": integer, "by_topic": { topic: integer } }`.

## Tests and current caveats

`test_use_data.py` uses direct assertions rather than a test runner. It checks empty-input behavior, aggregation across repeated topics, expected totals, and that `getSummary()` does not mutate the input list.

The test still imports `useData`, while the latest commit renamed the implementation to `use_data.py`; it therefore needs its import updated before it can run successfully. The application itself has also only light input validation: invalid menu text is handled, but session duration conversion and JSON/schema errors are not; the menu's upper-bound check appears off by one (`choice > len(...)` should reject `choice >= len(...)`).

## Development progression

The Git history shows a clear progression from an interactive prototype to a modestly modular CLI:

1. **Initial CLI (a4f67f2–17770f7):** added the menu, scalable option dispatch, input selection, and a clean quit action.
2. **Core study tracking (fbcb281–a3a5b33):** introduced configuration, session entry, analytics summaries, and improved prompting.
3. **Persistence hardening (80cecc7):** added initialization so an empty data file becomes valid JSON (`[]`). Subsequent fixes corrected the analytics structure and improved summary formatting.
4. **Modularization and import safety (9d950df–9b9e107):** added the conventional `if __name__ == "__main__"` guard and separated summary calculation from summary presentation, making the calculation independently testable.
5. **Input and history features (9fe2c89–68c85b1):** tightened menu selection behavior and added raw session-history display.
6. **Testing and naming cleanup (7cc8729–837be18):** added regression checks for the summary function, then renamed `useData.py` to `use_data.py` and updated application imports to follow snake_case. The test import was not updated in that final rename.

Overall, the project is intentionally simple: a synchronous read/modify/write workflow around a JSON list, with presentation, orchestration, persistence helpers, and aggregation separated into small modules. Its historical arc is the familiar one for small tools: first make the interaction work, then give the data a shape, then make side effects survivable, and finally extract pure logic so it can be tested—the software equivalent of learning bookkeeping before attempting Renaissance double-entry.
