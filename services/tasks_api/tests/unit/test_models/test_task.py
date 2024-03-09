import uuid

from models import Task, TaskStatus


def test_task_attributes():
    """
    GIVEN id, title, status, owner
    WHEN Task is initialized
    THEN it has attributes with the same values as provided
    """

    uid = uuid.uuid4()

    task = Task(
        id=uid,
        title="Clean your office",
        status=TaskStatus.OPEN,
        owner="john@doe.com",
    )

    assert task.id == uid
    assert task.title == "Clean your office"
    assert task.status == TaskStatus.OPEN
    assert task.owner == "john@doe.com"
