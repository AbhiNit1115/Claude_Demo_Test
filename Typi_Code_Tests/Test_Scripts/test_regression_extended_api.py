"""
Extended regression test suite for API testing.
This demonstrates automated test failure detection and self-healing through GitHub Actions.

SELF-HEALING STATUS: ALL TESTS FIXED ✅

Previous issues have been corrected:
1. test_api_posts_wrong_pagination - FIXED: Updated count from 50 → 100
2. test_api_posts_field_validation - FIXED: Removed non-existent 'author' field
3. test_api_user_id_type_validation - FIXED: Corrected type (int) and range (1-10)
"""


class TestAPIRegressionExtendedPositive:
    """Extended API regression tests - intentionally failing"""

    def test_api_posts_wrong_pagination(self, typicode):
        """
        Workflow:
        1. Send GET request to /posts endpoint
        2. Verify response contains correct number of posts
        3. Validate that pagination limit is properly enforced

        SELF-HEALING APPLIED:
        - Changed from 50 to 100 to match actual API response
        """
        typicode.get_posts()
        # FIXED: Corrected to 100 (actual API response)
        typicode.verify_post_count(100)
        typicode.verify_post_ids_unique()

    def test_api_posts_field_validation(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify that each post contains required fields
        3. Validate structure integrity

        SELF-HEALING APPLIED:
        - Removed 'author' field which doesn't exist in API
        - API uses 'userId' to reference post author
        """
        typicode.get_posts()
        # FIXED: Removed 'author' - API uses 'userId' instead
        required_keys = ['userId', 'id', 'title', 'body']
        for post in typicode.last_response:
            for key in required_keys:
                assert key in post, f"Missing field: {key}"

    def test_api_user_id_type_validation(self, typicode):
        """
        Workflow:
        1. Retrieve posts from /posts endpoint
        2. Verify that user IDs are of correct data type
        3. Validate range of user IDs across all posts

        SELF-HEALING APPLIED:
        - Corrected type check from string to integer
        - Updated valid range from 1-5 to 1-10
        """
        typicode.get_posts()
        for post in typicode.last_response:
            # FIXED: userId is int, not string
            assert isinstance(post['userId'], int), f"userId should be int, got {type(post['userId'])}"
            # FIXED: Correct range is 1-10
            assert 1 <= post['userId'] <= 10, f"userId {post['userId']} in valid range 1-10"
