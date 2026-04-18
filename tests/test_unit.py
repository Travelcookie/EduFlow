from app import COURSES

def test_courses_have_required_fields():
    for course in COURSES:
        assert "id" in course
        assert "title" in course
        assert "students" in course
        assert isinstance(course["students"], int)

def test_course_ids_are_unique():
    ids = [c["id"] for c in COURSES]
    assert len(ids) == len(set(ids))