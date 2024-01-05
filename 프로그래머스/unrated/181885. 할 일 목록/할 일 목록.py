def solution(todo_list, finished):
    return [ todo for todo, is_finished in zip(todo_list, finished) if is_finished is False ]