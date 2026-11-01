from todo import add_task, mark_done, delete_task, save_tasks, load_tasks
import json
import pytest


def test_add_task():
    tasks = []

    add_task(tasks, "Learn Python")

    assert len(tasks) == 1
    assert tasks[0] == {"title": "Learn Python", "done": False}


def test_mark_done():
    tasks = [{"title": "Learn Python", "done": False}]

    result = mark_done(tasks, 1)

    assert result is True
    assert tasks[0]["done"] is True


def test_mark_done_invalid_zero():
    tasks = [{"title": "Learn Python", "done": False}]

    result = mark_done(tasks, 0)

    assert result is False
    assert tasks[0]["done"] is False


def test_mark_done_invalid_number():
    tasks = [{"title": "Learn Python", "done": False}]

    result = mark_done(tasks, 5)

    assert result is False
    assert tasks[0]["done"] is False


def test_delete_task():
    tasks = [
        {"title": "Learn Python", "done": False},
        {"title": "Learn Git", "done": False},
    ]

    result = delete_task(tasks, 1)

    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Learn Git"


def test_delete_task_invalid_number():
    tasks = [{"title": "Learn Python", "done": False}]

    result = delete_task(tasks, 5)

    assert result is False
    assert len(tasks) == 1


def test_add_multiple_tasks():
    tasks = []

    add_task(tasks, "Learn Python")
    add_task(tasks, "Learn Git")

    assert len(tasks) == 2
    assert tasks[0]["title"] == "Learn Python"
    assert tasks[1]["title"] == "Learn Git"


def test_mark_done_empty_list():
    tasks = []

    result = mark_done(tasks, 1)

    assert result is False
    assert tasks == []


def test_delete_task_zero():
    tasks = [{"title": "Learn Python", "done": False}]

    result = delete_task(tasks, 0)

    assert result is False
    assert len(tasks) == 1


def test_delete_task_empty_list():
    tasks = []

    result = delete_task(tasks, 1)

    assert result is False
    assert tasks == []


def test_save_tasks(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = [
        {"title": "Learn Python", "done": False},
        {"title": "Learn Git", "done": True},
    ]

    save_tasks(tasks)

    with open("to_do.json", "r") as file:
        saved_tasks = json.load(file)

    assert saved_tasks == tasks


def test_load_tasks(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    expected_tasks = [
        {"title": "Learn Python", "done": False},
        {"title": "Learn Git", "done": True},
    ]

    with open("to_do.json", "w") as file:
        json.dump(expected_tasks, file)

    loaded_tasks = load_tasks()

    assert loaded_tasks == expected_tasks


def test_load_tasks_missing_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    tasks = load_tasks()

    assert tasks == []


def test_load_tasks_corrupted_json(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with open("to_do.json", "w") as file:
        file.write('{"title": "Learn Python", "done": False')

    with pytest.raises(json.JSONDecodeError):
        load_tasks()
