from src.main import welcome_message

def test_welcome_message():
    assert welcome_message("Luel") == "Luel, welcome to the Data Engineering course."
