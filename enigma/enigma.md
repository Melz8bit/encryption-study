# Enigma Machine — GUI Project Plan

A full web-based interface for the Enigma Machine simulation, allowing users to configure plugboard connections, select rotors, and encrypt/decrypt messages through a visual interface.

---

## Architecture

```
Browser (HTML/JS UI)  ←→  Flask API  ←→  enigma.py
```

---

## Project Structure

```
enigma-machine/
├── backend/
│   ├── app.py          ← Flask app
│   ├── enigma.py
│   ├── rotor.py
│   ├── plugboard.py
│   └── reflector.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── enigma.js
└── README.md
```

---

## Phase 1 — Flask Backend

### Refactor Python files first

**rotor.py:**
- Add all 5 historical rotor wirings (I-V) instead of just Rotor I
- Update Rotor class to accept rotor selection as a parameter

**enigma.py:**
- Accept rotor selection (which rotor goes in each slot) as a parameter
- Accept plugboard pairs as a parameter instead of hardcoded import
- Accept rotor starting positions as before

**plugboard.py:**
- Accept a dictionary of pairs as a parameter instead of using hardcoded PLUGBOARD constant

### Flask API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/encrypt` | Accepts message, rotor selections, rotor positions, plugboard pairs → returns encrypted message |
| GET | `/rotors` | Returns available rotor names and wirings for the frontend to display |

### Historical rotor wirings (I-V)

| Rotor | Wiring |
|-------|--------|
| I | EKMFLGDQVZNTOWYHXUSPAIBRCJ |
| II | AJDKSIRUXBLHWTMCQGZNPYFVOE |
| III | BDFHJLCPRTXVZNYEIWGAKMUSQO |
| IV | ESOVPZJAYQUIRHXLNFTGKDCMWB |
| V | VZBRGITYUPSDNHLXAWMJQOFECK |

---

## Phase 2 — Frontend UI

### Plugboard panel
- 26 letter buttons displayed in keyboard layout
- Click first letter → highlights it
- Click second letter → draws a colored cable between them
- Click either connected letter → removes the connection
- Maximum 10 pairs enforced
- Connected pairs displayed as a list below the panel

### Rotor panel
- Three rotor slots: Left, Middle, Right
- Dropdown per slot to select rotor I-V
- Starting position selector per rotor (A-Z)

### Message panel
- Text input for message
- Encrypt button → calls Flask API
- Output display for ciphertext
- Same interface handles decode (Enigma is symmetric)

---

## Phase 3 — Polish

- Visual SVG cables connecting plugboard letter buttons
- Rotor positions displayed as letters (A-Z) not numbers
- Message auto-sanitization (uppercase, strip non-letters)
- Error handling for invalid configurations (duplicate rotor selection, etc.)
- Dark theme to match existing tools (Nerd Book, Coding Backlog)
- Military/vintage aesthetic to match the Enigma Machine theme

---

## Build Order

1. Refactor rotor.py — add rotors II-V
2. Refactor plugboard.py — accept pairs as parameter
3. Refactor enigma.py — accept rotor selection and plugboard as parameters
4. Build Flask app.py with `/encrypt` and `/rotors` endpoints
5. Build frontend HTML/CSS structure
6. Build plugboard interaction (JS)
7. Build rotor selector (JS)
8. Wire frontend to Flask API (JS fetch)
9. Add SVG cables to plugboard
10. Polish and error handling

---

## Notes

- The existing encryption-study Python files stay as is — the backend imports and wraps them
- Since Enigma is symmetric, no separate encode/decode mode needed in the UI
- Start positions default to A (position 0) if not set by user
- Plugboard defaults to no connections if none set