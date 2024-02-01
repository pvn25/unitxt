import unittest

from src.unitxt.artifact import (
    Artifact,
)
from src.unitxt.dataclass import UnexpectedArgumentError
from src.unitxt.logging_utils import get_logger

logger = get_logger()


class TestArtifact(unittest.TestCase):
    def test_set_artifact_identifier(self):
        artifact = Artifact()
        artifact_identifier = "artifact.id.dummy"
        artifact.set_artifact_identifier(value=artifact_identifier)
        self.assertEqual(artifact_identifier, artifact.artifact_identifier)

    def test_artifact_identifier_setter(self):
        artifact = Artifact()
        artifact_identifier = "artifact.id.dummy"
        artifact.artifact_identifier = artifact_identifier
        self.assertEqual(artifact_identifier, artifact.artifact_identifier)

    def test_artifact_identifier_cannot_be_used_as_keyword_arg(self):
        """Test that artifact_identifier cannot be set in construction.

        Since it is an internal field, and isn't serialized, it should never be set when
        constructing an Artifact from kwargs.
        """
        with self.assertRaises(UnexpectedArgumentError):
            Artifact(artifact_identifier="artifact.id.dummy")
