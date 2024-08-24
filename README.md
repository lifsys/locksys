# Locksys

Locksys is a Python library developed by Lifsys, Inc. for securely retrieving API keys from 1Password vaults using the 1Password Connect SDK.

## Installation

Install Locksys using pip:

```bash
pip install locksys
```

Ensure you have Python 3.7 or later installed.

## Usage

Here's a comprehensive example of how to use Locksys:

```python
from locksys import Locksys

# Initialize Locksys with a vault name (default is "API")
lock = Locksys("MyVault")

try:
    # Retrieve an API key
    api_key = lock.item("MyItem").key("API_KEY").results()
    print(f"Retrieved API key: {api_key}")

    # Retrieve multiple keys from the same item
    database_url = lock.item("DatabaseCredentials").key("DATABASE_URL").results()
    database_password = lock.item("DatabaseCredentials").key("DATABASE_PASSWORD").results()
    print(f"Database URL: {database_url}")
    print(f"Database Password: {database_password}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Features

- Secure retrieval of API keys and other sensitive information from 1Password vaults
- Caching of 1Password client for improved performance
- Simple and intuitive API with method chaining
- Error handling for missing items or keys
- Support for retrieving multiple keys from the same item
- Logging for debugging and troubleshooting

## Requirements

- Python 3.7+
- 1Password Connect SDK

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to Locksys! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please ensure your code adheres to our coding standards and includes appropriate tests.

## Support

If you encounter any problems or have any questions:

1. Check the [documentation](https://github.com/lifsys/locksys/wiki)
2. Open an issue on the [GitHub repository](https://github.com/lifsys/locksys/issues)
3. For commercial support, contact Lifsys, Inc. at support@lifsys.com

## Acknowledgements

- 1Password for their excellent Connect SDK
- All contributors who have helped shape Locksys
