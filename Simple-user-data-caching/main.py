import redis

# Connect to the local Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Simulated function to fetch a user's username from a database
def get_username_from_database(user_id):
    # In a real application, this would fetch the username from a database
    return f"username_{user_id}"

def get_cache_key(user_id):
    # Generate a unique cache key based on the user ID
    return f"username_{user_id}"

def get_username(user_id):
    cache_key = get_cache_key(user_id)
    
    # Try to get the username from the cache
    username = r.get(cache_key)
    
    if username:
        print("Cache hit")
        return username.decode()  # Redis returns bytes, decode to string
    else:
        print("Cache miss")
        username = get_username_from_database(user_id)
        
        # Store the username in the cache with an expiration time (e.g., 60 seconds)
        r.setex(cache_key, 240, username)
        
        return username

if __name__ == "__main__":
    user_id = 123
    
    # First call, should be a cache miss and take time
    print(get_username(user_id))  # Output: username_123
    
    # Subsequent calls within the expiration time should be a cache hit and be fast
    print(get_username(user_id))  # Output: username_123
