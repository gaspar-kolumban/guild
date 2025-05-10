import pathlib
import tempfile
import unittest
import yaml


simple_example = """
- type: c_library
  name: PrintHelloWorldLib
  interfaces:
    - helloworld.h
  sources:
    - helloworld.c

- type: c_library
  name: MainLib
  dependencies:
    - PrintHelloWorldLib
  sources:
    - main.c

- type: c_executable
  name: Main
  dependencies:
    - MainLib
    - PrintHelloWorldLib
"""


class TestYamlFormat(unittest.TestCase):
    def test_parse_simple_yaml(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            yaml_file = pathlib.Path(tmp_dir) / "build.yaml"

            with open(yaml_file, "w") as fd:
                fd.write(simple_example)

            with open(yaml_file, "r") as fd:
                data = yaml.safe_load(fd)

            self.assertIsInstance(data, list)
            self.assertEqual(len(data), 3)

            element = data[0]
            self.assertEqual(element["name"], "PrintHelloWorldLib")
            self.assertEqual(element["type"], "c_library")
            self.assertIsInstance(element["interfaces"], list)
            self.assertEqual(len(element["interfaces"]), 1)
            self.assertIn("helloworld.h", element["interfaces"])
            self.assertIsInstance(element["sources"], list)
            self.assertEqual(len(element["sources"]), 1)
            self.assertIn("helloworld.c", element["sources"])

            element = data[1]
            self.assertEqual(element["name"], "MainLib")
            self.assertEqual(element["type"], "c_library")
            self.assertIsInstance(element["dependencies"], list)
            self.assertEqual(len(element["dependencies"]), 1)
            self.assertIn("PrintHelloWorldLib", element["dependencies"])
            self.assertIsInstance(element["sources"], list)
            self.assertEqual(len(element["sources"]), 1)
            self.assertIn("main.c", element["sources"])

            element = data[2]
            self.assertEqual(element["name"], "Main")
            self.assertEqual(element["type"], "c_executable")
            self.assertIsInstance(element["dependencies"], list)
            self.assertEqual(len(element["dependencies"]), 2)
            self.assertIn("MainLib", element["dependencies"])
            self.assertIn("PrintHelloWorldLib", element["dependencies"])
