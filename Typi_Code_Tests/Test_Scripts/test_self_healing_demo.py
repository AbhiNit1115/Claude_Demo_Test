"""
Self-healing regression test suite for demonstration purposes.
These tests are intentionally designed to fail, showcasing automated error detection,
analysis, and correction mechanisms.

Expected Failures:
1. test_api_posts_count_mismatch - Expects 50 posts but API returns 100
2. test_api_invalid_field_name - Looks for 'author' field that doesn't exist
3. test_api_posts_wrong_range - Expects user IDs in range 1-5 (actual: 1-10)
4. test_api_post_body_type - Expects post body to be an integer (actual: string)
"""


class TestSelfHealingDemoPositive:
    """Intentionally failing tests to demonstrate self-healing"""

    def test_api_posts_count_mismatch(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify count is 50 (INTENTIONAL ERROR - actual is 100)
        3. Verify post IDs are unique

        Expected Failure:
        AssertionError: Expected 50 posts, got 100

        Root Cause: Incorrect hardcoded count value
        """
        typicode.get_posts()
        # INCORRECT: Actually returns 100 posts
        typicode.verify_post_count(50)
        typicode.verify_post_ids_unique()

    def test_api_invalid_field_name(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify structure (will fail on missing 'author' field)

        Expected Failure:
        AssertionError: Post missing key: author

        Root Cause: Incorrect field name - should be 'userId' not 'author'
        """
        typicode.get_posts()
        # This method will verify posts have required keys
        required_keys = ['userId', 'id', 'title', 'body', 'author']  # INCORRECT: no 'author'
        for post in typicode.last_response:
            for key in required_keys:
                if key not in post:
                    raise AssertionError(f"Post missing key: {key}")

    def test_api_posts_wrong_range(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify user IDs are in range 1-5 (INTENTIONAL ERROR - actual: 1-10)

        Expected Failure:
        AssertionError: userId X out of expected range 1-5

        Root Cause: Hardcoded incorrect range value
        """
        typicode.get_posts()
        # INCORRECT: Actual range is 1-10, not 1-5
        typicode.verify_user_id_range(1, 5)

    def test_api_post_body_type_validation(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify each post body is a string (correct)
        3. Verify all posts exist (correct)

        Expected Failure:
        This test contains logic error in type checking

        Root Cause: Incorrect type validation that assumes integer body
        """
        typicode.get_posts()
        # Intentional type error - body is string, not int
        for post in typicode.last_response:
            body = post.get('body')
            # INCORRECT: Body is a string, not an integer
            if not isinstance(body, int):
                raise AssertionError(
                    f"Post {post['id']} body is type {type(body).__name__}, "
                    f"expected int but got: {body[:20]}..."
                )

    def test_api_posts_title_length_check(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify all post titles are longer than 100 characters

        Expected Failure:
        AssertionError: Post X title too short (length: Y)

        Root Cause: Unrealistic title length requirement
        """
        typicode.get_posts()
        # INCORRECT: Most titles are much shorter than 100 chars
        for post in typicode.last_response:
            title = post.get('title', '')
            if len(title) < 100:
                raise AssertionError(
                    f"Post {post['id']} title too short (length: {len(title)}), "
                    f"expected >= 100: '{title}'"
                )


class TestSelfHealingDemoNegative:
    """Negative tests with intentional failures"""

    def test_api_invalid_post_id_format(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify all post IDs are strings (INTENTIONAL ERROR - they are integers)

        Expected Failure:
        AssertionError: Post ID X is not a string

        Root Cause: Type checking error
        """
        typicode.get_posts()
        # INCORRECT: IDs are integers, not strings
        for post in typicode.last_response:
            post_id = post.get('id')
            if not isinstance(post_id, str):
                raise AssertionError(
                    f"Post ID {post_id} is not a string, got type: {type(post_id).__name__}"
                )

    def test_api_user_id_string_validation(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify all userIds are numeric strings (INTENTIONAL ERROR - they are integers)

        Expected Failure:
        AssertionError: userId X is not a numeric string

        Root Cause: Type validation error
        """
        typicode.get_posts()
        # INCORRECT: userIds are integers, not strings
        for post in typicode.last_response:
            user_id = post.get('userId')
            if not isinstance(user_id, str) or not user_id.isdigit():
                raise AssertionError(
                    f"userId {user_id} is not a numeric string, got type: {type(user_id).__name__}"
                )
