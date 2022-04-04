"""
blink/core/resource.py
Ian Kollipara
2022.03.31

API Resource Decorator
"""

# Imports
from dataclasses import dataclass
from re import compile as re_compile
from typing import Any, Callable, Dict, Generic, List, Optional, Type, TypedDict, TypeVar

from .protocols.resource import ResourceT

# Generic Type Variable

_T = TypeVar("_T")


class Dependency(TypedDict):
    """Dependency Type for use in Dependency Injection

    This dictionary type represents what a dependency could look like
    for Blink.
    """

    dependency: Callable
    dependency_params: Optional[Dict[str, Any] | List[Any]]


@dataclass(frozen=True)
class ResourceType(Generic[_T]):
    """ResourceType represents what the @Resource
    decorator returns.

    | Attributes | Type | Description               |
    |------------|------|---------------------------|
    | route      | str  | the api route             |
    | obj        | T    | The resource class object |
    """

    route: str
    obj: _T


class Resource:
    """Resource Decorator

    Each API falcon resource should be decorated with
    `@Resource` above it. This allows the user to set the
    path and path parameters for the route as well.

    Example:
    ```python
    @Resource("/test", [{"dependency": SomeClass}])
    class Test:
       def __init__(self, some_class: SomeClass) -> None:
           self.some_class = some_class
           ...
    ```
    """

    def __init__(
        self, route: str, dependencies: Optional[List[Dependency]] = None
    ) -> None:
        self.dependencies = dependencies or []
        self.route = route
        self.camel_to_snake_pattern = re_compile(r"(?<!^)(?=[A-Z])")

    def camel_case_to_snake(self, camel_case: str) -> str:
        """Transform a CamelCase string to snake_case.

        Given a valid string, return the lowered, snake_case
        version of that string.
        """

        return self.camel_to_snake_pattern.sub("_", camel_case).lower()

    def __call__(self, resource_cls: Type[ResourceT]) -> ResourceType[ResourceT]:

        # The main idea here is what happens when the
        # resource class is called, such as
        # Resource("/test")(Test)
        # Which is what happens with the decorator

        initialized_dependencies: Dict[str, Any] = {}
        for dep in self.dependencies:
                if isinstance(dep["dependency_params"], list):
                    initialized_dependencies |= {self.camel_case_to_snake(dep["dependency"].__name__): dep["dependency"](*dep["dependency_params"])}
                if isinstance(dep["dependency_params"], dict):
                    initialized_dependencies |= {self.camel_case_to_snake(dep["dependency"].__name__): dep["dependency"](**dep["dependency_params"])}
                else:
                    initialized_dependencies |= {self.camel_case_to_snake(dep["dependency"].__name__): dep["dependency"]()}

        obj = (
            resource_cls(**initialized_dependencies)  # type: ignore
            if len(initialized_dependencies)
            else resource_cls()
        )
        return ResourceType(self.route, obj)
