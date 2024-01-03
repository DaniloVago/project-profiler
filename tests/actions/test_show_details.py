from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_file_with_extension(tmp_path, capsys):
    file_with_extension = tmp_path / "Trybe_logo.png"
    file_with_extension.touch()
    context = {"base_path": str(file_with_extension)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = ("File name: Trybe_logo.png\n"
                        "File size in bytes: 0\n"
                        "File type: file\n"
                        "File extension: .png\n"
                        f"Last modified date: {date.today()}\n")
    assert captured.out == expected_output

def test_file_not_existing(capsys):
    context = {"base_path": "/home/trybe/????"}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = ("File '????' does not exist\n")
    assert captured.out == expected_output

def test_file_without_extension(tmp_path, capsys):
    file_without_extension = tmp_path / "Trybe_logo"
    file_without_extension.touch()
    context = {"base_path": str(file_without_extension)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = ("File name: Trybe_logo\n"
                        "File size in bytes: 0\n"
                        "File type: file\n"
                        "File extension: [no extension]\n"
                        f"Last modified date: {date.today()}\n")
    assert captured.out == expected_output