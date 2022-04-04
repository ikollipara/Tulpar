"""
tests/test_resource.py
Ian Kollipara
2022.04.04

Testing tuplar.resource
"""

# Imports
from falcon import Request, Response

from tulpar import resource
from tulpar.protocols.resource import HTML


def test_dependency():
    """Test if the Dependency Typed Dict works as intended.

    This test checks if the keys are the same for a random dictionary
    created with the class, and another initialized as a dictionary.
    """

    test = resource.Dependency(dependency=int, dependency_params={})
    successful = {"dependency": int, "dependency_params": {}}
    failure = {}

    assert test.keys() == successful.keys()
    assert not test.keys() == failure.keys()


def test_resource_type():
    """Test the ResourceType Generic Dataclass.

    Create a resource type for a specific class, then
    test that the instance is true and that all body
    parameters conform to type specification.
    """

    test = resource.ResourceType("/", int())

    assert isinstance(test, resource.ResourceType)
    assert isinstance(test.obj, int)
    assert test.route == "/"


def test_resource():
    """Test the @Resource Decorator

    Check if the dependency inject works, the decorator
    creates the class of that type, and that X implements
    one of ResourceT.
    """

    @resource.Resource("/", [{"dependency": int, "dependency_params": [0]}])
    class X:
        def __init__(self, int: int) -> None:
            self.x = int

        def on_get(self, req: Request, res: Response) -> HTML:
            return HTML("<p>Hello World</p>")

    assert type(X) == resource.ResourceType
    assert X.obj.x == 0
    assert X.route == "/"

    @resource.Resource(
        "/t", [resource.Dependency(dependency=dict, dependency_params={"name": "Ian"})]
    )
    class Y:
        def __init__(self, dict: dict) -> None:
            self.y = dict

        def on_get(self, req: Request, res: Response) -> HTML:
            return HTML("<p>Hello World</p>")

    assert type(Y) == resource.ResourceType
    assert Y.obj.y == {"name": "Ian"}
    assert Y.route == "/t"
