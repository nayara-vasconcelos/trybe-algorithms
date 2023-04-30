import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    result = ""
    valid_message, invalid_message = "🦋🦄🐝🦆🐝🦄", 0
    valid_key, invalid_key = 0, "🦄🐝🦆🐝🦄🦋"
    lower_index_key = {"valid_key": 0, "expected_result": "🦄🐝🦆🐝🦄🦋"}
    out_of_range_key = {"valid_key": 6, "expected_result": "🦄🐝🦆🐝🦄🦋"}
    even_key = {"valid_key": 4, "expected_result": "🦄🐝_🦆🐝🦄🦋"}
    odd_key = {"valid_key": 3, "expected_result": "🐝🦄🦋_🦄🐝🦆"}

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(valid_message, invalid_key)
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(invalid_message, valid_key)

    result = encrypt_message(valid_message, lower_index_key["valid_key"])
    assert result == lower_index_key["expected_result"]

    result = encrypt_message(valid_message, out_of_range_key["valid_key"])
    assert result == out_of_range_key["expected_result"]

    result = encrypt_message(valid_message, even_key["valid_key"])
    assert result == even_key["expected_result"]

    result = encrypt_message(valid_message, odd_key["valid_key"])
    assert result == odd_key["expected_result"]
