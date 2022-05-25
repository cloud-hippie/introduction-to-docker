from celery import Celery

celery = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

@celery.task(name="create_task")
def test_celery(word: str) -> str:
    return f"test task return {word}"


