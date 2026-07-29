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
| L2 | Playfair Cipher | Substitution | ✅ Complete |
| L2 | One-Time Pad | Substitution | ✅ Complete |
| L3 | Rotor Simulation | Mechanical | ✅ Complete |
| L3 | Plugboard Simulation | Mechanical | ✅ Complete |
| L3 | Reflector Simulation | Mechanical | ✅ Complete |
| L4 | Enigma Machine | Mechanical | ✅ Complete |

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

### Playfair Cipher

A digraph substitution cipher that encrypts pairs of letters using a 5x5 grid built from a keyword. The most complex classical cipher — significantly harder to break than single-letter substitution.

**How it works:**

1. Build a 5x5 grid from the keyword (duplicates removed, I and J share a cell, remaining alphabet fills the rest)
2. Prepare the message — strip non-letters, split into pairs, insert X between repeated letters in a pair, pad odd-length messages with X
3. For each pair apply one of three rules:
   - **Same row** — each letter shifts one column right (wrapping), left to decode
   - **Same column** — each letter shifts one row down (wrapping), up to decode
   - **Rectangle** — each letter takes the column of the other, keeping its own row (same for encode and decode)

**Example:** HELLO with keyword KEYWORD → GYIZSC (X padding preserved on decode: HELXLO)

**Complexity:** O(n) time, O(1) space for the grid (always 5x5)

**Weaknesses:**
- Vulnerable to digraph frequency analysis — common pairs like TH, HE still appear with higher frequency
- Key space is larger than Caesar/Vigenère but still breakable with enough ciphertext
- I and J are treated as the same letter — information loss

**Improvement over previous ciphers:** Encrypts pairs instead of single letters, breaking simple frequency analysis. The rectangle rule creates non-linear relationships between plaintext and ciphertext.

---

### One-Time Pad

A theoretically unbreakable cipher that XORs each byte of the message against a corresponding byte from a truly random key. The key must be at least as long as the message and never reused.

**How it works:**
- Generate a cryptographically random key the same length as the message using `os.urandom()`
- XOR each message byte against the corresponding key byte
- Key and ciphertext are both represented as hex strings for portability
- Decryption is identical — XOR the ciphertext bytes with the same key bytes

**Why XOR works:**
- `message XOR key = ciphertext`
- `ciphertext XOR key = message`
- XOR is its own inverse — applying it twice with the same key recovers the original

**Example:**
```
message:    hello  →  68 65 6c 6c 6f  (hex bytes)
key:                  23 c1 44 7b 7c  (random hex)
ciphertext:           4b a4 28 17 13  (XOR result)
```

**Complexity:** O(n) time, O(n) space

**Why it's unbreakable (when used correctly):**
- The key is truly random — no pattern to exploit
- The key is the same length as the message — no repetition
- The key is never reused — no statistical analysis possible
- Without the key, every possible plaintext is equally likely

**Conditions that break it:**
- Key reuse — the Soviet Union's reuse of OTP keys allowed the US Venona project to break their communications
- Non-random key generation — predictable keys can be brute forced
- Key interception — security depends entirely on keeping the key secret

**Improvement over previous ciphers:** The only cipher with mathematical proof of perfect secrecy. Every previous cipher can be broken given enough ciphertext — OTP cannot, when used correctly.

---

## Level 3 — Mechanical Concepts

### Rotor Simulation

A simulation of the Enigma Machine's core component — a rotor that applies a position-dependent substitution cipher, stepping forward after every letter encrypted.

**How it works:**
- Each rotor has a fixed wiring — a scrambled alphabet mapping (Rotor I wiring used)
- The current position offsets the input before wiring lookup and offsets the output after
- After each letter the rotor steps forward one position (mod 26)
- The same starting position must be used for encode and decode

**Encoding a letter:**
1. Convert letter to index (A=0, Z=25)
2. Shift index forward by current position (mod 26)
3. Look up shifted index in wiring
4. Shift output back by current position (mod 26)
5. Step rotor forward

**Decoding a letter:**
1. Convert letter to index
2. Shift index forward by current position (mod 26)
3. Find shifted letter's position in wiring (reverse lookup)
4. Shift output back by current position (mod 26)
5. Step rotor forward

**Wiring used (Rotor I):**
```
Input:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Output: EKMFLGDQVZNTOWYHXUSPAIBRCJ
```

**Complexity:** O(n) time, O(1) space

**What makes it powerful:** The substitution changes with every letter — the same letter typed twice produces different outputs. This is what separates the Enigma from all previous static ciphers.

---

### Plugboard Simulation

A simulation of the Enigma Machine's plugboard (Steckerbrett) — a panel of letter pairs that swaps letters before they enter the rotors and again after they exit. The plugboard is its own inverse — applying it twice returns the original letter.

**How it works:**
- A dictionary maps each connected letter to its pair
- Unconnected letters pass through unchanged
- The swap is symmetric — if A→B then B→A
- Encode and decode are identical operations

**Typical Enigma configuration:**
- 10 pairs connected, 6 letters left unconnected
- Applied before the rotors and after the rotors

**Complexity:** O(n) time, O(1) space — dictionary lookup is O(1)

**Why a function not a class:** The plugboard has no state — it's a pure transformation. A function is the right abstraction.

**What it adds to Enigma:** The plugboard dramatically increases the key space. With 10 pairs chosen from 26 letters there are over 150 trillion possible plugboard configurations — multiplied against the rotor starting positions this makes brute force effectively impossible.

---

### Reflector Simulation

A simulation of the Enigma Machine's reflector (Umkehrwalze) — a fixed, stationary component that bounces the signal back through the rotors a second time, doubling the encryption. The reflector is its own inverse and never steps.

**How it works:**
- A fixed wiring maps each letter to a unique partner (Reflector B used)
- The mapping is always symmetric — if A→Y then Y→A
- No letter maps to itself — this was the fatal flaw that aided codebreakers
- No encode/decode distinction — applying it twice returns the original letter
- Never steps — it has no position state

**Wiring (Reflector B / UKW-B):**
```
Input:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Output: YRUHQSLDPXNGOKMIEBFZCWVJAT
```

**Complexity:** O(n) time, O(1) space

**The fatal flaw:** Because no letter can map to itself, Alan Turing's bombe machine could eliminate impossible rotor configurations by testing whether any letter encrypted to itself. This dramatically reduced the search space and made cracking feasible.

**Why a function not a class:** The reflector has no state — it never steps and its wiring never changes. A pure function is the right abstraction.

---

## Level 4 — Enigma Machine

### Enigma Machine

A full working simulation of the German Enigma Machine — combining the plugboard, three rotors, and reflector into a complete encryption system. Symmetric by design: the same operation with the same settings encodes and decodes.

**Signal path (per keypress):**
1. Plugboard — swap letter if connected
2. Rotor 1 steps, then encodes letter forward
3. Rotor 2 steps (if rotor 1 completed full rotation), then encodes forward
4. Rotor 3 steps (if rotor 2 completed full rotation), then encodes forward
5. Reflector — bounces signal back
6. Rotor 3 decodes backward
7. Rotor 2 decodes backward
8. Rotor 1 decodes backward
9. Plugboard — swap letter again
10. Output letter

**Symmetry:** No encode/decode mode — the same operation with the same rotor starting positions encodes and decodes. HELLO → MMGAS → HELLO.

**Rotor stepping (odometer mechanic):**
- Rotor 1 steps every keypress
- Rotor 2 steps when rotor 1 completes a full rotation (every 26 keypresses)
- Rotor 3 steps when rotor 2 completes a full rotation (every 676 keypresses)

**Components used:**
- Plugboard — 10 hardcoded letter pairs
- Rotor I wiring — EKMFLGDQVZNTOWYHXUSPAIBRCJ
- Reflector B wiring — YRUHQSLDPXNGOKMIEBFZCWVJAT

**Complexity:** O(n) time — constant work per letter regardless of message length

**Historical note:** The actual Enigma used 3-5 rotors chosen from a set of 8, variable plugboard settings, and ring settings on each rotor — creating over 10^23 possible configurations. Our implementation uses fixed settings for clarity but the core mechanics are identical.

---

## Study Context

Built as part of a self-directed CS study curriculum covering algorithms, data structures, and cryptography, working toward a full Enigma Machine implementation.