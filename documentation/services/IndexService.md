# IndexService

A list of all methods in the `IndexService` service. Click on the method name to view detailed information about that method.

| Methods                     | Description                                                                    |
| :-------------------------- | :----------------------------------------------------------------------------- |
| [hello_world](#hello_world) | Returns a greeting message with timestamp and optional language specification. |

## hello_world

Returns a greeting message with timestamp and optional language specification.

- HTTP Method: `GET`
- Endpoint: `/`

**Parameters**

| Name     | Type                              | Required | Description |
| :------- | :-------------------------------- | :------- | :---------- |
| language | [Language](../models/Language.md) | ❌       |             |

**Return Type**

`HelloResponse`

**Example Usage Code Snippet**

```python
from hello_world_sdk import HelloWorldSdk
from hello_world_sdk.models import Language

sdk = HelloWorldSdk(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)

result = sdk.index.hello_world(language="en")

print(result)
```
