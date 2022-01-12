import io
from contextlib import redirect_stdout

import pytest

from app.main import create_dict


@pytest.mark.parametrize(
    "args,expected_std_output,expected_result",
    [
        (
            (7, 1, 3),
            "",
            {7: 0, 1: 1, 3: 2}
        ),
        (
            (3, (1, 2), 5),
            "",
            {3: 0, (1, 2): 1, 5: 2}
        ),
        (
            (3, [1, 2], 5),
            "Cannot add [1, 2] to the dict!\n",
            {3: 0, 5: 2}
        ),
        (
            (3, {1, 2}, 5),
            "Cannot add {1, 2} to the dict!\n",
            {3: 0, 5: 2}
        ),
        (
                (3, {1: 1, 2: 2}, 5),
                "Cannot add {1: 1, 2: 2} to the dict!\n",
                {3: 0, 5: 2}
        ),
        (
            ({},),
            "Cannot add {} to the dict!\n",
            {}
        ),
        (
            ([], {}, "asdf"),
            "Cannot add [] to the dict!\nCannot add {} to the dict!\n",
            {"asdf": 2}
        )
    ]
)
def test_create_dict(args: tuple, expected_std_output: str, expected_result: dict):
    f = io.StringIO()
    with redirect_stdout(f):
        create_dict_result = create_dict(*args)

    std_output = f.getvalue()

    assert create_dict_result == expected_result
    assert std_output == expected_std_output


def test_create_dict_with_function_argument():
    def func():
        pass

    f = io.StringIO()
    with redirect_stdout(f):
        create_dict_result = create_dict(func, 2)

    std_output = f.getvalue()

    assert create_dict_result == {func: 0, 2: 1}
    assert std_output == ""


# @pytest.mark.parametrize(
#     "args,expected_std_output,expected_result",
#     [
#         (
#             ((1, (2, [3, 4])), 2),
#             "Cannot add (1, (2, [3, 4])), 2) to the dict!\n",
#             {}
#         ),
#         (
#             (((1, 2), (3, 4), (5, (6, 7, 8, (9, "hello")))), "asdf"),
#             "",
#             {((1, 2), (3, 4), (5, (6, 7, 8, (9, "hello")))): 0, "asdf": 1}
#         ),
#         (
#             (((1, 2), (3, 4), (5, (6, 7, 8, (9, [1])))), "asdf"),
#             "Cannot add ((1, 2), (3, 4), (5, (6, 7, 8, (9, [1]])))) to the dict!",
#             {"asdf": 1}
#         )
#     ]
# )
# def test_create_dict_optional_task(args: tuple, expected_std_output: str, expected_result: dict):
#     f = io.StringIO()
#     with redirect_stdout(f):
#         create_dict_result = create_dict(*args)
#
#     std_output = f.getvalue()
#
#     assert create_dict_result == expected_result
#     assert std_output == expected_std_output
