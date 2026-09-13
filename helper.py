from fastapi import HTTPException, status


def verify_item_exists(item_id: int):
    # Simulting a database check
    valid_ids = [1, 2, 3]

    if item_id not in valid_ids:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} was not found!",
        )
    return True
