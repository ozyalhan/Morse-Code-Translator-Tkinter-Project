#From exploratory testing  to Automated Unit Testing :)
import translator as tsl
import unittest

class TestMorseTranslator(unittest.TestCase):
    
    def test_morse_translation_func_single_word(self):
        """
        Test that it can return right value of sos ->"... -- ..."
        """
        data = "sos"
        result_object = tsl.MorseTranslator(data)
        result_value =result_object.morse_translation_func()
        self.assertEqual(result_value,"... --- ...")

    def test_morse_translation_func_two_words(self):
        """
        Test that it can return right value of "sos sms"->"... --- ... / ... -- ..."
        """
        data = "sos sms"
        result_object = tsl.MorseTranslator(data)
        result_value =result_object.morse_translation_func()
        self.assertEqual(result_value,"... --- ... / ... -- ...")
 
    def test_morse_translation_func_two_words_end_with_space(self):
        """
        Test that it can return right value of "sos sms         "->"... --- ... / ... -- ..."
        Check that rstip working.
        """
        data = "sos sms         "
        result_object = tsl.MorseTranslator(data)
        result_value =result_object.morse_translation_func()
        self.assertEqual(result_value,"... --- ... / ... -- ...")   

    def test_morse_translation_func_two_words_start_with_space(self):
        """
        Test that it can return right value of "           sos sms"->"... --- ... / ... -- ..."
        Check that lstrip working.
        """
        data = "           sos sms"
        result_object = tsl.MorseTranslator(data)
        result_value =result_object.morse_translation_func()
        self.assertEqual(result_value,"... --- ... / ... -- ...")    

    def test_morse_translation_func_two_words_capitalized(self):
        """
        Test that it can return right value of "SOS SMS"->"... --- ... / ... -- ..."
        Check that lower() working.
        """
        data = "SOS SMS"
        result_object = tsl.MorseTranslator(data)
        result_value =result_object.morse_translation_func()
        self.assertEqual(result_value,"... --- ... / ... -- ...")               

    def test_morse_translation_func_words_numbers(self):
        """
        Test that it can return right value of "sos sms 12"->"... --- ... / ... -- ... / .---- ..---"
        Check that lower() working.
        """
        data = "sos sms 12"
        preticted_result = "... --- ... / ... -- ... / .---- ..---"
        result_object = tsl.MorseTranslator(data)
        result_value =result_object.morse_translation_func()
        self.assertEqual(result_value,preticted_result)    
       
if __name__ == "__main__":
    unittest.main()