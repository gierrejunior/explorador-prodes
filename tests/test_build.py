import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build', ROOT / 'scripts' / 'build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildTests(unittest.TestCase):
    def test_publication_is_reproducible(self):
        original = (ROOT / 'index.html').read_text()
        data, note = build.payload(original)
        self.assertEqual(build.render(build.TEMPLATE.read_text(), data, note), original)

    def test_requires_unambiguous_placeholders(self):
        with self.assertRaises(ValueError):
            build.render('__DADOS__ __DADOS__ __NOTA_USO__', '{}', 'nota')

    def test_does_not_interpret_data_as_template_code(self):
        data = '{"mestre":[],"texto":"<script>$HOME __NOTA_USO__</script>"}'
        self.assertEqual(build.render('__DADOS__\n__NOTA_USO__', data, 'nota'), data+'\nnota')


if __name__ == '__main__':
    unittest.main()
