import unittest
import unreal_engine as ue
from unreal_engine.structs import ColorMaterialInput


class TestStructs(unittest.TestCase):

    def test_new_struct(self):
        material_input = ColorMaterialInput()
        self.assertTrue('MaskR' in material_input.fields())

    def test_new_struct_with_kwargs(self):
        material_input = ColorMaterialInput(Mask=1, MaskR=1, MaskG=1, MaskB=0, MaskA=1)
        self.assertEqual(material_input.Mask, 1)
        self.assertEqual(material_input.MaskR, 1)
        self.assertEqual(material_input.MaskG, 1)
        self.assertEqual(material_input.MaskB, 0)
        self.assertEqual(material_input.MaskA, 1)


    def test_struct_set(self):
        material_input = ColorMaterialInput()
        material_input.MaskG = 1
        self.assertEqual(material_input.MaskG, 1)

    def test_struct_clone(self):
        material_input = ColorMaterialInput(Mask=1, MaskR=0, MaskG=1, MaskB=0, MaskA=1)
        material_input2 = material_input.clone()
        self.assertEqual(material_input2.Mask, 1)
        self.assertEqual(material_input2.MaskR, 0)
        self.assertEqual(material_input2.MaskG, 1)
        self.assertEqual(material_input2.MaskB, 0)
        self.assertEqual(material_input2.MaskA, 1)

   



