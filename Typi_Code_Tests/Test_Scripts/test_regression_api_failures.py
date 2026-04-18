"""
Regression test suite with intentionally failing tests for self-healing demonstration.
These tests fail due to outdated/incorrect locators and assertions.
"""


class TestAPIRegressionFailures:
    """API tests that intentionally fail to demonstrate self-healing"""

    def test_api_posts_wrong_count(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify count is 100 (FIXED - corrected from 50)
        3. Verify post IDs are unique
        """
        typicode.get_posts()
        typicode.verify_post_count(100)  # FIXED - corrected to 100
        typicode.verify_post_ids_unique()

    # REMOVED: test_api_comments_invalid_endpoint
    # Root Cause: get_comments() method doesn't exist in TypiCodeAPI
    # Fix: Method would need to be implemented first - removing for now
    # To re-enable, implement get_comments() in libraries/api_functions/API_Typicode_Functions.py

    def test_api_posts_invalid_user_id_range(self, typicode):
        """
        Workflow:
        1. Fetch posts from /posts endpoint
        2. Verify user IDs are in range 1-10 (FIXED - corrected from 1-5)
        """
        typicode.get_posts()
        typicode.verify_user_id_range(1, 10)  # FIXED - corrected range to 1-10
