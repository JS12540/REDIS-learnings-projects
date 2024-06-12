# REDIS-learnings-projects

# Important Redis Commands

Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. Here are some essential commands:

## Key-Value Operations

### SET
Set the string value of a key.

```bash
SET key value
```

### GET
Get the value of a key.

```bash
GET key
```

### DEL
Delete one or more keys.

```bash
DEL key [key ...]
```

### EXISTS
Check if a key exists.

```bash
EXISTS key
```

### List Operations

### LPUSH
Insert an element at the beginning of a list.

```bash
LPUSH key value [value ...]
```

### RPUSH
Insert an element at the end of a list.

```bash
RPUSH key value [value ...]
```

### LPOP
Remove and get the first element in a list.

```bash
LPOP key
```

### RPOP
Remove and get the last element in a list.

```bash
RPOP key
```

### Set Operations

### SADD
Add one or more members to a set.

```bash
SADD key member [member ...]
```

### SMEMBERS
Get all members of a set.

```bash
SMEMBERS key
```

### SISMEMBER
Check if a member exists in a set.

```bash
SISMEMBER key member
```

###Sorted Set Operations

### ZADD
Add one or more members to a sorted set.

```bash
ZADD key score member [score member ...]
```

### ZRANGE
Get a range of members from a sorted set by index.

```bash
ZRANGE key start stop [WITHSCORES]
```

### ZSCORE
Get the score associated with a member in a sorted set.

```bash
ZSCORE key member
```

### Hash Operations

### HSET
Set the value of a field in a hash.

```bash
HSET key field value
```

### HGET
Get the value of a field in a hash.

```bash
HGET key field
```

### HGETALL
Get all fields and values in a hash.

```bash
HGETALL key
```

These are just some of the fundamental Redis commands. For a complete list, refer to the official documentation.
