"""Authentication code challenge: hashing and JWT helpers.

This module defines functions whose behavior you should implement as part of
the challenge. The current bodies are stubs; update only docstrings here.

Expectations:
- Use bcrypt for hashing and verification.
- Use JWT (HS256) for token creation/validation.
- Do not mutate inputs; validate and normalize where appropriate.
- Handle edge cases (empty inputs, malformed tokens) clearly.
"""

from collections.abc import Mapping, Sequence
from datetime import datetime, timedelta
from typing import Any

import bcrypt
import jwt

from app.core.config import settings


def hash_password(plain_password: str) -> str:
    """Return a bcrypt hash for the given plaintext password.

    Behavior to implement:
    - Generate a new random salt per call (bcrypt.gensalt).
    - Hash the UTF-8 encoded plaintext using bcrypt.
    - Return the result as a UTF-8 string suitable for storage.

    Edge cases and guidance:
    - Reject or document behavior for empty passwords.
    - Do not store or log the plaintext.
    - The same plaintext will produce different hashes due to unique salts.

    Example:
    - hash_password("secret") -> "$2b$12$..."
    """
    salt = bcrypt.gensalt()
    password_encode = plain_password.encode("utf-8")
    hash_password = bcrypt.hashpw(password_encode, salt=salt)
    return str(hash_password)


def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """Check whether `plain_password` matches the given bcrypt `hashed_password`.

    Behavior to implement:
    - Encode `plain_password` and `hashed_password` as UTF-8.
    - Use `bcrypt.checkpw` to verify the password.
    - Return True if the check succeeds, False otherwise.

    Edge cases and guidance:
    - Treat any unexpected errors as a failed verification (return False).
    - Document expectations when `hashed_password` is malformed.
    - Avoid timing leaks by delegating to bcrypt's constant-time comparison.
    """
    password = plain_password.encode("utf-8")
    check_passord = bcrypt.checkpw(password, hashed_password)
    if check_passord:
        return True
    return False


def create_access_token(
    subject: str,
    *,
    roles: Sequence[str] | None = None,
    expires_delta: timedelta | None = None,
    extra_claims: Mapping[str, Any] | None = None,
) -> str:
    """Create and return a signed JWT access token as a string.

    Behavior to implement:
    - Build a payload with:
      - `sub`: the subject (typically user id)
      - `iat`: issued-at epoch seconds
      - `exp`: expiry epoch seconds; use `expires_delta` or default minutes from settings
      - `roles`: optional list of roles (case and format as-is or normalize)
      - Merge `extra_claims` if provided; do not overwrite standard claims unintentionally.
    - Sign the token using HS256 with the configured secret key.

    Edge cases and guidance:
    - Validate `roles` as a sequence of strings; normalize if needed.
    - Ensure `exp` is strictly in the future.
    - Avoid putting sensitive data in the payload.

    Example:
    - create_access_token("user-123", roles=["USER"]) -> "eyJhbGciOi..."
    """
    to_dict = {"subject": subject, "roles": roles, "expires_delta": expires_delta}

    expire = datetime.now(datetime.UTC) + timedelta(
        minutes=settings.security_access_token_expire_minutes
    )
    to_dict.update({"expires_delta": expire})
    encoded_jwt = jwt.encode(
        to_dict, settings.security_secret_key, algorithm=settings.security_jwt_algorithm
    )
    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT access token and return its payload.

    Behavior to implement:
    - Verify signature and `exp` using configured secret and algorithm.
    - Return the decoded payload as a dict.
    - Normalize `roles` to a list if present but not already a list.

    Edge cases and guidance:
    - Raise clear exceptions or document return behavior for invalid/expired tokens.
    - Avoid mutating input token; treat it as opaque data.
    - Consider clock skew allowances when validating `exp`.
    """
    try:
        decoded_token = jwt.decode(
            token,
            settings.security_secret_key,
            algorithms=[settings.security_jwt_algorithm],
        )
        return (
            decoded_token
            if decoded_token["expires_delta"] >= datetime.now(datetime.UTC)
            else None
        )
    except jwt.PyJWTError:
        return None
