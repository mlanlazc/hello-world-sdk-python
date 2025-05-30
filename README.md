# HelloWorldSdk Python SDK 1.6.0

Welcome to the HelloWorldSdk SDK documentation. This guide will help you get started with integrating and using the HelloWorldSdk SDK in your project.

[![This SDK was generated by liblab](https://public-liblab-readme-assets.s3.us-east-1.amazonaws.com/built-by-liblab-icon.svg)](https://liblab.com/?utm_source=readme)

## Versions

- API version: `1.6.0`
- SDK version: `1.6.0`

## About the API

A simple FastAPI example with OpenAPI specification

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [Access Token Authentication](#access-token-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Async Usage](#async-usage)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install hello_world_sdk
```

## Authentication

### Access Token Authentication

The HelloWorldSdk API uses an Access Token for authentication.

This token must be provided to authenticate your requests to the API.

#### Setting the Access Token

When you initialize the SDK, you can set the access token as follows:

```py
HelloWorldSdk(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)
```

If you need to set or update the access token after initializing the SDK, you can use:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Setting a Custom Timeout

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from hello_world_sdk import HelloWorldSdk

sdk = HelloWorldSdk(timeout=10000)
```

# Sample Usage

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from hello_world_sdk import HelloWorldSdk
from hello_world_sdk.models import Language

sdk = HelloWorldSdk(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.index.hello_world(language="en")

print(result)

```

# Async Usage

The SDK includes an Async Client for making asynchronous API requests. This is useful for applications that need non-blocking operations, like web servers or apps with a graphical user interface.

```py
import asyncio
from hello_world_sdk import HelloWorldSdkAsync
from hello_world_sdk.models import Language

sdk = HelloWorldSdkAsync(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)


async def main():
  result = await sdk.index.hello_world(language="en")
  print(result)

asyncio.run(main())
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                               |
| :----------------------------------------------------------------- |
| [IndexService](documentation/services/IndexService.md)             |
| [OpenapiJsonService](documentation/services/OpenapiJsonService.md) |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                               | Description |
| :----------------------------------------------------------------- | :---------- |
| [HelloResponse](documentation/models/HelloResponse.md)             |             |
| [Language](documentation/models/Language.md)                       |             |
| [HttpValidationError](documentation/models/HttpValidationError.md) |             |
| [ValidationError](documentation/models/ValidationError.md)         |             |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.
