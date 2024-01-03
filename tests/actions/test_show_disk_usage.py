from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_file_with_text(tmp_path, capsys):
    file_with_text = tmp_path / "file_with_text.txt"
    file_with_text.touch()
    file_with_text.write_text("something")
    str_file_with_text = str(file_with_text)
    context = {
        "all_files": [str_file_with_text]
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    expected_output = (
        f"'{_get_printable_file_path(str_file_with_text)}':".ljust(71) +
        "9 (100%)\n" +
        "Total size: 9\n")
    assert captured.out == expected_output

def test_file_empty(capsys):
    context = {
        "all_files": []
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    expected_output = ("Total size: 0\n")
    assert captured.out == expected_output

def test_multiple_files(tmp_path, capsys):
    file1 = tmp_path / "file1"
    file1.touch()
    file1.write_text("something" * 2)
    str_file1 = str(file1)

    file2 = tmp_path / "file2"
    file2.touch()
    file2.write_text("something")
    str_file2 = str(file2)

    context = {
        "all_files": [str_file1, str_file2]
    }
    show_disk_usage(context)
    captured = capsys.readouterr()
    expected_output = (
        f"'{_get_printable_file_path(str_file1)}':".ljust(71) + "18 (66%)\n"
        f"'{_get_printable_file_path(str_file2)}':".ljust(80) + "9 (33%)\n"
        "Total size: 27\n"
        )
    assert captured.out.strip() == expected_output.strip()