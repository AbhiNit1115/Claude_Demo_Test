"""
Self-healing regression test suite for demonstration purposes.
This test file demonstrates automated error detection, analysis, and correction mechanisms.

SELF-HEALING STATUS: ALL TESTS FIXED ✅

Previously failing tests have been corrected:
1. test_api_posts_count_mismatch - FIXED: Updated count from 50 → 100
2. test_api_invalid_field_name - FIXED: Removed non-existent 'author' field
3. test_api_posts_wrong_range - FIXED: Updated range from (1-5) → (1-10)
4. test_api_post_body_type_validation - FIXED: Corrected type check int → str
5. test_api_posts_title_length_check - FIXED: Removed unrealistic constraint
6. test_api_invalid_post_id_format - FIXED: Corrected type check str → int
7. test_api_user_id_string_validation - FIXED: Corrected type check str → int
"""


class TestSelfHealingDemoPositive:
    """Intentionally failing tests to demonstrate self-healing"""

    def test_api_posts_count_mismatch(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify count is 100 (FIXED - corrected from 50)
        3. Verify post IDs are unique

        SELF-HEALING APPLIED:
        Changed expected count from 50 to 100 to match API response
        """
        typicode.get_posts()
        # FIXED: Corrected to 100
        typicode.verify_post_count(100)
        typicode.verify_post_ids_unique()

    def test_api_invalid_field_name(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify structure (FIXED - removed non-existent 'author' field)

        SELF-HEALING APPLIED:
        Removed 'author' field from validation. API uses 'userId' instead.
        """
        typicode.get_posts()
        # FIXED: Removed 'author' - not in API response
        required_keys = ['userId', 'id', 'title', 'body']
        for post in typicode.last_response:
            for key in required_keys:
                if key not in post:
                    raise AssertionError(f"Post missing key: {key}")

    def test_api_posts_wrong_range(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify user IDs are in range 1-10 (FIXED - corrected from 1-5)

        SELF-HEALING APPLIED:
        Updated range from (1, 5) to (1, 10) to match actual API data
        """
        typicode.get_posts()
        # FIXED: Corrected range to 1-10
        typicode.verify_user_id_range(1, 10)

    def test_api_post_body_type_validation(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify each post body is a string (FIXED - corrected type check)
        3. Verify all posts exist

        SELF-HEALING APPLIED:
        Changed type validation from int to str to match API response
        """
        typicode.get_posts()
        # FIXED: Corrected type check to str
        for post in typicode.last_response:
            body = post.get('body')
            if not isinstance(body, str):
                raise AssertionError(
                    f"Post {post['id']} body is type {type(body).__name__}, "
                    f"expected str"
                )

    def test_api_posts_title_length_check(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify all post titles have reasonable length (FIXED - removed unrealistic constraint)

        SELF-HEALING APPLIED:
        Removed unrealistic 100-character minimum requirement.
        Replaced with realistic validation: title exists and has content.
        """
        typicode.get_posts()
        # FIXED: Removed unrealistic constraint, verify titles exist
        for post in typicode.last_response:
            title = post.get('title', '')
            if not title or len(title) == 0:
                raise AssertionError(
                    f"Post {post['id']} title is empty"
                )


class TestSelfHealingDemoNegative:
    """Negative tests with intentional failures"""

    def test_api_invalid_post_id_format(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify all post IDs are integers (FIXED - corrected type check)

        SELF-HEALING APPLIED:
        Changed type validation from str to int to match API response
        """
        typicode.get_posts()
        # FIXED: Corrected type check to int
        for post in typicode.last_response:
            post_id = post.get('id')
            if not isinstance(post_id, int):
                raise AssertionError(
                    f"Post ID {post_id} is not an integer, got type: {type(post_id).__name__}"
                )

    def test_api_user_id_string_validation(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify all userIds are integers (FIXED - corrected type check)

        SELF-HEALING APPLIED:
        Changed type validation from numeric string to int to match API response
        """
        typicode.get_posts()
        # FIXED: Corrected type check to int
        for post in typicode.last_response:
            user_id = post.get('userId')
            if not isinstance(user_id, int):
                raise AssertionError(
                    f"userId {user_id} is not an integer, got type: {type(user_id).__name__}"
                )
