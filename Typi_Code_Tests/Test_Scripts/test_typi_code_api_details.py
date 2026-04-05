def test_typicode_get_posts(typicode):
    """
    Positive test: GET /posts and validate important parts of the API.
    """
    typicode.get_posts()
    typicode.verify_posts_structure()
    typicode.verify_post_count(100)
    typicode.verify_post_ids_unique()
    typicode.verify_user_id_range(1, 10)

def test_typicode_negative_endpoint(typicode):
    """
    Negative test: GET invalid endpoint and expect error.
    """
    typicode.negative_test_invalid_endpoint()