import unittest

from EmotionDetection.emotion_detection import emotion_detector

class test_emotion_detection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector('I am glad this happened.') 
        self.assertEqual(result['dominent_emotion'], 'joy') 
        result = emotion_detector('I am really mad about this.') 
        self.assertEqual(result['dominent_emotion'], 'anger') 
        result = emotion_detector('I feel disgusted just hearing about this.') 
        self.assertEqual(result['dominent_emotion'], 'disgust') 
        result = emotion_detector('I am sad about this.')
        self.assertEqual(result['dominent_emotion'], 'sadness')
        result = emotion_detector('I am really afraid this will happen.')
        self.assertEqual(result['dominent_emotion'], 'fear')
        
if __name__ == '__main__':
    unittest.main()
    