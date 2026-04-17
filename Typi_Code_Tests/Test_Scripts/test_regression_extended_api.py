"""
Extended regression test suite for API testing.
This demonstrates automated test failure detection and self-healing through GitHub Actions.

SELF-HEALING STATUS: INTENTIONALLY FAILING - Ready for demonstration ⚠️

These tests are intentionally designed to fail with specific issues:
1. test_api_posts_wrong_pagination - Incorrect limit assumption
2. test_api_posts_field_validation - Invalid field name
3. test_api_user_id_type_validation - Wrong type check
"""


class TestAPIRegressionExtendedPositive:
    """Extended API regression tests - intentionally failing"""

    def test_api_posts_wrong_pagination(self, typicode):
        """
        Workflow:
        1. Send GET request to /posts endpoint
        2. Verify response contains correct number of posts
        3. Validate that pagination limit is properly enforced

        SELF-HEALING NEEDED:
        - Current: expects 50 posts (wrong assumption)
        - Should be: 100 posts (actual API returns 100)
        """
        typicode.get_posts()
        # BUG: Wrong count - API returns 100, not 50
        typicode.verify_post_count(50)
        typicode.verify_post_ids_unique()

    def test_api_posts_field_validation(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify that each post contains required fields
        3. Validate structure integrity

        SELF-HEALING NEEDED:
        - Current: checking for 'author' field (doesn't exist in API)
        - Should be: use 'userId' instead
        """
        typicode.get_posts()
        # BUG: 'author' field doesn't exist in API response
        required_keys = ['userId', 'id', 'title', 'body', 'author']
        for post in typicode.last_response:
            for key in required_keys:
                assert key in post, f"Missing field: {key}"

    def test_api_user_id_type_validation(self, typicode):
        """
        Workflow:
        1. Retrieve posts from /posts endpoint
        2. Verify that user IDs are of correct data type
        3. Validate range of user IDs across all posts

        SELF-HEALING NEEDED:
        - Current: checking if userId is string (wrong type)
        - Should be: userId should be integer
        """
        typicode.get_posts()
        for post in typicode.last_response:
            # BUG: userId is int, not string
            assert isinstance(post['userId'], str), f"userId should be string, got {type(post['userId'])}"
            # BUG: Range is wrong - valid range is 1-10
            assert 1 <= post['userId'] <= 5, f"userId {post['userId']} out of expected range 1-5"
