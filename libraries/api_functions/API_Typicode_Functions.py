from typing import List, Dict, Any

class Endpoints:
    POSTS = 'posts'

class TypiCodeAPI:
    def __init__(self, client):
        self.client = client
        self.last_response: List[Dict[str, Any]] = []

    def get_posts(self) -> List[Dict[str, Any]]:
        """
        Sends a GET request to /posts and stores the response.
        :return: List of post dictionaries.
        """
        response = self.client.get(Endpoints.POSTS)
        self.last_response = response
        return response

    def verify_posts_structure(self) -> None:
        """
        Verifies that each post in the response has the required keys.
        """
        required_keys = ['userId', 'id', 'title', 'body']
        for post in self.last_response:
            for key in required_keys:
                if key not in post:
                    raise AssertionError(f"Post missing key: {key}")

    def verify_post_count(self, expected_count: int = 100) -> None:
        """
        Verifies the number of posts in the response.
        """
        actual_count = len(self.last_response)
        if actual_count != expected_count:
            raise AssertionError(f"Expected {expected_count} posts, got {actual_count}")

    def verify_post_ids_unique(self) -> None:
        """
        Verifies that all post IDs are unique.
        """
        ids = []
        for post in self.last_response:
            ids.append(post['id'])
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                if ids[i] == ids[j]:
                    raise AssertionError(f"Duplicate post id found: {ids[i]}")

    def verify_user_id_range(self, min_id: int = 1, max_id: int = 10) -> None:
        """
        Verifies that all userId values are within the expected range.
        """
        for post in self.last_response:
            user_id = post['userId']
            if user_id < min_id or user_id > max_id:
                raise AssertionError(f"userId {user_id} out of expected range {min_id}-{max_id}")

    def negative_test_invalid_endpoint(self) -> None:
        """
        Negative test: GET an invalid endpoint and expect a ResponseError.
        """
        try:
            self.client.get('invalid_posts')
        except Exception as e:
            # Should raise ResponseError from client.py
            return
        raise AssertionError("Expected error for invalid endpoint, but none was raised.")