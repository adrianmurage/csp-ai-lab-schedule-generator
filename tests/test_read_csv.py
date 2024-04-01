import pytest
import os
from app.index import read_csv


@pytest.fixture
def sample_csv_file(tmp_path):
    # Create a sample CSV file with test data
    csv_data = [
        "7:00 AM,MW,APT2022,A,INTRODUCTION TO ASSEMBLY PROGRAMMING,\"Aloo, L\",22",
        "9:00 AM,MW,DST4010,A,DISTRIBUTED SYSTEMS,\"Ogore, F\",10",
        "7:00 AM,TR,APP4025,A,DESIGN & DEVELOPMENT OF CLOUD APPLICATIONS,\"Wokabi, F\",18"
    ]
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("\n".join(csv_data))
    yield csv_file  # Provide the path to the temporary file to the test


def test_read_csv(sample_csv_file):
    # Arrange & Act
    data = read_csv(sample_csv_file)

    # Assert
    assert len(data) == 3
    assert data[0] == ["7:00 AM", "MW", "APT2022", "A",
                       "INTRODUCTION TO ASSEMBLY PROGRAMMING", "Aloo, L", "22"]
    assert data[1] == ["9:00 AM", "MW", "DST4010",
                       "A", "DISTRIBUTED SYSTEMS", "Ogore, F", "10"]
    assert data[2] == ["7:00 AM", "TR", "APP4025", "A",
                       "DESIGN & DEVELOPMENT OF CLOUD APPLICATIONS", "Wokabi, F", "18"]
