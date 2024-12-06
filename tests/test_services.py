from cuizhanming_python_project1.services import declaim

class TestDeclaim:
    def test_declaim(self, capsys):
        title = "Super Cool"
        poem = (
            "Roses are red\n"
            "Violets are blue\n"
            "I think the Global South\n"
            "is super cool"
        )
        author = "Tonino"
        expected_output = (
            "---------------------------------------------------\n"
            "Super Cool\n"
            "\n"
            "Roses are red\n"
            "Violets are blue\n"
            "I think the Global South\n"
            "is super cool\n"
            "\n"
            "By Tonino\n"
            "---------------------------------------------------\n"
        )

        declaim(title, poem, author)

        captured = capsys.readouterr()

        assert captured.out == expected_output