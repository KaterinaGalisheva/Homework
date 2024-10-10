
import traceback
import class_R_logs as cl
import unittest
import logging
'''for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)'''

logging.basicConfig(level=logging.INFO, 
                    filemode='w', 
                    encoding='utf-8', 
                    filename='runner_tests.log', 
                    format='%(asctime)s | %(levelname)s | %(messege)s')




class RunnerTest(unittest.TestCase):


    def test_run(self):
        try:
            r_2 = cl.Runner(542, 8)
            for _ in range(10):
                r_2.run()
            self.assertEqual(r_2.distance, 100)
            logging.info('"Test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner') 
            logging.warning(traceback.format_exc())
            

    def test_walk(self):
        try:
            r_1 = cl.Runner('any', -3)
            for _ in range(10):
                r_1.walk()
            self.assertEqual(r_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')
            logging.warning(traceback.format_exc())





if __name__ == '__main__':
    unittest.main()
    
    
