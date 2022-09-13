"""
Redis
"""

# Imports
import redis

# Environment
from app.config.env import environment


class RedisConnection:
    """
    Redis Connection
    """

    def __init__(self) -> None:
        """
        Init
        """
        self.cache = redis.Redis(
            host=environment.redis_host,
            password=environment.redis_pass,
            port=environment.redis_port,
        )

    def build_key(self, key_items) -> str:
        """
        Build a cache key for redis

        Note:
            Format: redis_prefix + "-" + item_1 + ... + item_n

        Args:
            key_items (list of str): List of items used to construct the key

        Return:
            cache_key (str): Cache key
        """
        return environment.redis_prefix + "-" + "".join(key_items)

    def clear_cache(self, key_pattern=None) -> int:
        """
        Deletes all items in cache for a project. Key has a wildcard (*)
        appended to the end so that the key matches on a pattern.

        Note:
            Default key: <environment_prefix>-*
            Extended key: <environment_prefix>-<key_pattern>*

        Args:
            key_pattern (str): Optional,
        """
        count = 0
        key_match = environment.redis_prefix + "-"

        if key_pattern:
            key_match += key_pattern + "*"
        else:
            key_match += "*"

        for key in self.cache.scan_iter(key_match):
            self.cache.delete(key)
            count += 1

        return count


redis_connection = RedisConnection()
