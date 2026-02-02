# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased] – V2 (in progress)
### Added
- Planned support for bcrypt password hashes
- Planned support for argon2 password hashes
- Advanced bruteforce time estimation (min / avg / max)
- Optional audit report export (JSON / TXT)

### Changed
- Hash verification logic will be refactored to support slow password hashes
- CLI output will be improved for audit readability

---

## [1.0.0] – 2025-xx-xx
### Added
- Incremental bruteforce mode
- Dictionary attack mode
- Bruteforce time estimation
- Support for SHA-1 and SHA-256
- Configurable charset and max length
- Graceful Ctrl+C handling with statistics summary
- Unit tests with pytest
