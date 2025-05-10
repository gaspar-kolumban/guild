import pathlib
import tempfile
import unittest
import yaml


simple_build = """
name: HelloWorld
type: c_library
interfaces:
  - helloworld.h
sources:
  - main.c
  - helloworld.c
"""


class TestYamlFormat(unittest.TestCase):
    def test_parse_simple_yaml(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            yaml_file = pathlib.Path(tmp_dir) / "build.yaml"

            with open(yaml_file, "w") as f:
                f.write(simple_build)

            with open(yaml_file, "r") as file:
                data = yaml.safe_load(file)

            self.assertEqual(data["name"], "HelloWorld")
            self.assertEqual(data["type"], "c_library")
            self.assertIn("helloworld.h", data["interfaces"])
            self.assertIn("helloworld.c", data["sources"])
            self.assertIn("main.c", data["sources"])
