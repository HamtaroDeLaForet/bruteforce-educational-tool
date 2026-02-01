# 🔐 Bruteforce Audit Tool (Python) — Educational Cybersecurity Project

This project is an **educational tool** designed to demonstrate the impact of weak passwords by simulating **bruteforce attacks** on **local hashes**.  
It aims to raise awareness about password security and good cybersecurity practices in a controlled and responsible way.

---

## 🎯 Project Goals

- Understand brute force mechanics
- Visualize how weak passwords can be cracked
- Compare different brute force strategies
- Highlight password security best practices
- Promote **ethical cybersecurity awareness**

---

## 🧰 Features

✔ **Incremental Brute Force**  
→ Generates combinations over configurable charsets

✔ **Dictionary Attack**  
→ Tests candidate words from a wordlist

✔ **Standard Hashing Support**  
→ Supports `MD5`, `SHA1`, and `SHA256`

✔ **Complexity Estimation**  
→ Theoretical cracking time estimates based on parameters

✔ **Execution Statistics**  
→ Attempts count, execution time, found state, etc.

---

## 🏗 Internal Architecture

```
src/
├── core/
│   ├── brute_incremental.py   # Incremental brute force logic
│   ├── brute_dictionary.py    # Dictionary attack processing
│   └── hash_utils.py          # Hashing and comparison utilities
│
├── analysis/
│   └── time_estimator.py      # Time complexity estimation
│
├── cli/
│   └── main.py                # CLI entry point
│
└── config/
    └── settings.py            # Charset and default parameters
```

---

## 🖥 CLI Usage Examples

### 🔸 **1. Incremental Brute Force**
```bash
python main.py --mode incremental --hash <hash> --algo sha256 --charset digits --max-length 4
```

### 🔸 **2. Dictionary Attack**
```bash
python main.py --mode dictionary --hash <hash> --dict wordlists/common.txt
```

### 🔸 **3. Time Estimation**
```bash
python main.py --mode estimate --password "test123" --charset alphanumeric --speed 1000000
```

---

## 🧩 Supported Algorithms

- `MD5`
- `SHA1`
- `SHA256`

---

## 📈 Example Output (Simplified)

```
{
  "found": true,
  "password": "1234",
  "attempts": 10000,
  "time": 0.23
}
```

---

## 🔐 Ethical & Legal Considerations

This project is intended **solely for educational purposes** and is restricted to **local testing on user-provided data**.

> ❗ **No real system attack capabilities**  
> ❗ **No networking or remote exploitation**  
> ❗ **No password collection or harvesting**

Misuse of cybersecurity tools may be illegal in many countries.  
For example, in France, unauthorized system access is subject to **Article 323-1 of the Penal Code**.

By using this tool, you agree to **act responsibly and within legal boundaries**.

---

## 📦 Installation

```bash
git clone https://github.com/<your-repo>
cd bruteforce-audit
pip install -r requirements.txt
```

---

## 🔍 Why Recruiters Care About This Project

This project demonstrates that you:

✔ Understand **real-world offensive techniques** responsibly  
✔ Know how to implement **hashing and cryptographic logic**  
✔ Can design **modular and scalable software architectures**  
✔ Care about **ethical practices and legal boundaries**  
✔ Can communicate cyber concepts with **clarity and pedagogy**  
✔ Are comfortable with **CLI-based tooling**, common in pentesting environments  

This is highly relevant for roles such as:

- Security Engineer
- Pentester / Red Team
- SOC Analyst / Blue Team
- Cybersecurity Consultant
- Application Security Engineer

---

## 🚀 Future Improvements

Planned or possible enhancements:

- `bcrypt`, `argon2`, `PBKDF2` hashing
- Multi-threading / GPU acceleration
- Web interface (FastAPI + React)
- Benchmarking modes
- JSON/CSV reporting
- Wordlist mutation (leet speak, suffix, etc.)

These features provide a natural roadmap for further cybersecurity skill growth.

---

## Roadmap

### v1 (current)
- Incremental bruteforce
- Dictionary attack
- Time estimation
- Pytest coverage

### v2 (in progress)
- Argon2 / bcrypt support
- Realtime ETA & stats
- Early stop audit mode

### v3 (planned)
- Password strength scoring
- Multiprocessing engine


## 📄 License

Released under the **MIT License**, for **ethical use only**.

---

## ✍ Author

Developed by **HamtaroDesBois** — cybersecurity & software development enthusiast.  
For inquiries or collaboration: **www.linkedin.com/in/mateo-fauquembergue-84105a251**
