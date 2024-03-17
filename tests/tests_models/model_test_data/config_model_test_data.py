"""Simple data for Config Model tests."""


pass_data = [
    {
        "service": {
            "endpoint": "https://some.triplestore/repositories/endpoint",
            "user": "admin",
            "password": "password123"
        }
    },
    {
        "service": {
            "endpoint": "http://some.triplestore/repositories/endpoint",
            "user": "admin",
            "password": "password123"
        }
    }
]

fail_data = [
    {
        "ServicE": {
            "endpoint": "https://some.triplestore/repositories/endpoint",
            "user": "admin",
            "password": "password123"
        }
    },
    {
        "service": {
            "endpoint": "some.triplestore/repositories/endpoint",
            "user": "admin",
            "password": "password123"
        }
    },
    {
        "service": {
            "endpoint": "https://some.triplestore/repositories/endpoint",
            "user": 123,
            "password": "password123"
        }
    },

    {
        "service": {
            "endpoint": "https://some.triplestore/repositories/endpoint",
            "user": "admin",
            "password": 123
        }
    }

]
