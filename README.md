# Encryption Study

A progressive implementation of encryption techniques starting from classical ciphers and working toward a full Enigma Machine. Each cipher builds on the concepts of the previous one, tracing the historical evolution of cryptography.

---

## Track Progress

| Level | Cipher | Category | Status |
|-------|--------|----------|--------|
| L1 | Caesar Cipher | Classical | ✅ Complete |
| L1 | Vigenère Cipher | Classical | ✅ Complete |
| L1 | Atbash Cipher | Classical | ✅ Complete |
| L2 | Rail Fence Cipher | Transposition | ✅ Complete |
| L2 | Playfair Cipher | Substitution | Pending |
| L2 | One-Time Pad | Substitution | Pending |
| L3 | Rotor Simulation | Mechanical | Pending |
| L3 | Plugboard Simulation | Mechanical | Pending |
| L3 | Reflector Simulation | Mechanical | Pending |
| L4 | Enigma Machine | Mechanical | Pending |

---

## Structure

```
encryption/
├── README.md
├── caesar/
│   └── caesar.py
├── vigenere/
│   └── vigenere.py
├── atbash/
│   └── atbash.py
├── ...
└── enigma/
    └── enigma.py
```

---

## Background

Built as part of a self-directed CS study curriculum. The goal is to understand encryption from first principles — starting with simple substitution, moving through classical and mechanical techniques, and culminating in a full working Enigma Machine implementation.

**Reading context:** *The Code Book* — Simon Singh · *Crypto* — Steven Levy · *The Codebreakers* — David Kahn

---

## Level 1 — Classical Ciphers

### Caesar Cipher

The simplest substitution cipher — each letter is shifted a fixed number of positions in the alphabet. Julius Caesar used a shift of 3.

**How it works:**
- Each letter shifts by a fixed amount
- Non-letter characters pass through unchanged
- Case is preserved
- Wraps around using modular arithmetic: `chr((ord(letter) - base + shift) % 26 + base)`

**Complexity:** O(n) time, O(n) space

**Weaknesses:**
- Only 25 possible shifts — brute force takes seconds
- Letter frequency analysis immediately reveals the shift
- Same letter always maps to the same output

---

### Vigenère Cipher

A polyalphabetic substitution cipher using a repeating keyword. Each letter of the keyword determines the shift for the corresponding message letter — essentially multiple Caesar Ciphers applied in sequence.

**How it works:**
- Keyword repeats to match message length using modular indexing: `key_index = i % len(key)`
- Each key letter's alphabet position (A=0, B=1 ... Z=25) determines the shift
- Case is preserved, non-letter characters pass through unchanged

**Example:** HELLO with key KEY → RIJVS

**Complexity:** O(n) time, O(n) space

**Weaknesses:**
- Vulnerable to Kasiski analysis — repeated ciphertext sequences reveal key length
- Once key length is known, reduces to multiple Caesar Ciphers
- Key reuse is the core vulnerability

**Improvement over Caesar:** The same plaintext letter maps to different ciphertext letters depending on position — breaks simple frequency analysis.

---

### Atbash Cipher

A fixed substitution cipher using the reversed alphabet — A becomes Z, B becomes Y, and so on. No key is required. It is its own inverse — encoding and decoding are the same operation.

**How it works:**
- Each letter maps to its mirror position in the alphabet
- Case is preserved, non-letter characters pass through unchanged
- Formula: `chr((2 * base) + 25 - ord(letter))`

**Example:** HELLO → SVOOL, SVOOL → HELLO

**Complexity:** O(n) time, O(n) space

**Weaknesses:**
- No key — the mapping is always fixed and public
- Trivially broken — just apply it again to decode
- Historically used in Hebrew texts (the name Atbash comes from the first, last, second, and second-to-last letters of the Hebrew alphabet)

**Improvement over Caesar/Vigenère:** None from a security standpoint — it is weaker than both. Its value is as a stepping stone to understanding fixed substitution before moving to keyed and mechanical systems.

---

## Level 2 — Transposition & Substitution

### Rail Fence Cipher

A transposition cipher that arranges the message in a zigzag pattern across a fixed number of rails, then reads off each rail in order to produce the ciphertext. Unlike substitution ciphers, the letters themselves don't change — only their positions.

**How it works:**
- Letters are distributed across n rails in a bouncing zigzag pattern (down to the last rail, then back up)
- Direction flips when hitting the top (rail 0) or bottom (rail n-1) rail
- Encoded message is formed by concatenating each rail left to right from top to bottom

**Example:** HELLOWORLD with 3 rails:

```
Rail 0: H . . . O . . . L .
Rail 1: . E . L . W . R . D
Rail 2: . . L . . . O . . .
```

Output: HOLELWRDLO

**Complexity:** O(n) time, O(n) space — two passes through the message

**Weaknesses:**
- Only n-1 possible rail counts for a message of length n — small key space
- Pattern is visible once the rail count is known
- No substitution — letter frequency is fully preserved

**Difference from Level 1:** Rail Fence is a transposition cipher — it rearranges letters rather than substituting them. Combined with a substitution cipher it becomes significantly harder to break.

---

## Study Context

Built as part of a self-directed CS study curriculum covering algorithms, data structures, and cryptography, working toward a full Enigma Machine implementation.