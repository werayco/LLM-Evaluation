import uuid
import hashlib
from typing import Tuple

def hashgenerator(user_name: str) -> Tuple[str, str]:
    salt = uuid.uuid4().hex

    hash_object = hashlib.sha256((user_name + salt).encode())
    hashed_name = hash_object.hexdigest()
    return salt, hashed_name