import pytest
from app.index import check_feasibility, FeasibilityError


def test_feasibility_check_fails():
    # Define sample data
    groups = {
        'Group1': [['class1'], ['class2']],  # Two classes in Group1
        # Three classes in Group2
        'Group2': [['class3'], ['class4'], ['class5']]
    }
    labs = ['Lab1', 'Lab2']  # Only two labs available

    # Test that FeasibilityError is raised when classes exceed available labs
    with pytest.raises(FeasibilityError) as exc_info:
        check_feasibility(groups, labs)

    # Verify the error message
    assert str(exc_info.value) == (
        "Error: Unable to generate lab schedule for group 'Group2'. "
        "There are more classes scheduled than available labs (Lab1, Lab2). "
        "Consider adding more lab resources or adjusting the schedule."
    )


def test_feasibility_check_passes():
    # Define sample data where the number of classes is less than or equal to the number of labs
    groups = {
        'Group1': [['class1'], ['class2']],
        'Group2': [['class3'], ['class4']]
    }
    labs = ['Lab1', 'Lab2']

    # Perform feasibility check
    try:
        check_feasibility(groups, labs)
    except FeasibilityError as e:
        pytest.fail(f"Feasibility check failed unexpectedly: {e}")
