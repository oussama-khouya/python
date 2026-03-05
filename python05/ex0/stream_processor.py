from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

#an abstract class that have abstarct methodes
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    def format_output(self, result: str) -> str:
        pass
    
#a sub class called NumericProcessor that process 
#numeric data

class NumericProcessor(DataProcessor):
    #override abstract
    #validate if a list and x is int
    def validate(self, data: Any) -> bool:
        if not isinstance(data,list):
            return False
        for x in data:
            if not isinstance(x,int):
                return False
        return True
    #process the list len and sum
    def process(self, data: Any) -> str:
        try:
            total = len(data)
            summ = sum(data)    
            av = summ / total
            return f"Processed {total} numeric values, sum={summ}, avg={av}"
        except ZeroDivisionError:
            return "Error: you list is empty"
        
    
    def format_output(self, result: str) -> str:
        return f"Output: {result}\n"

class  TextProcessor(DataProcessor):
    """process text"""
    def validate(self, data: Any) -> bool:
        """not an empty str"""
        return isinstance(data, str) and len(data) > 0
        
    def process(self, data : Any) -> str:
        try:
            words = len(data.split(" "))
            characters = len(data)
            return f" Processed text: {characters} characters, {words} words"
        except (AttributeError, IndexError) as e:
            return f"Error type: {e}"
    
    
    def format_output(self, result: str) -> str:
        return f"Output: {result}\n"
    
class  LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        """ valid str and not empty """
        return isinstance(data,str) and len(data) > 0
    
    def process(self, data : Any) -> str:
        try:
            ls = data.split(":")
            alert = ls[0]
            message = ls[1]
            return f"[ALERT] {alert} level detected: {message}"
        except (AttributeError, IndexError) as e:
            return f"Error type: {e}"


    def format_output(self, result: str) -> str:
        return f"Output: {result}\n"
    
if __name__ == "__main__":
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
        #numirique processor
        print("Initializing Numeric Processor...")
        np = NumericProcessor()
        data = [1, 2, 3, 4, 5]
        print(f"Processing data: {data}")
        #validating the data
        if np.validate(data):
            print("Validation: Numeric data verified")
        #processing the data
        result = np.process(data)
        #printing the data
        print(np.format_output(result))

        #text processor
        print("Initializing Text Processor...")
        tp = TextProcessor()
        data1 = "Hello Nexus World"
        print(f'Processing data: "{data1}"')
        #validating
        if tp.validate(data1):
            print("Validation: Text data verified")
        #processing
        result1 = tp.process(data1)
        #print the data
        print(tp.format_output(result1))

        #log processing
        print("Initializing Log Processor...")
        lp = LogProcessor()
        data2 = "ERROR: Connection timeout"
        print("Processing data: {data2}")
        #validation
        if lp.validate(data2):
            print("Validation: Log entry verified")
        #processing
        result2 = lp.process(data2)
        #print data
        print(tp.format_output(result2))

        #demonstating polymorphism
        print("=== Polymorphic Processing Demo ===\n")
        
        collection = [(NumericProcessor(), [1,2,3]),
                      (TextProcessor(), "oussama khou"),
                        (LogProcessor(), "INFO : System ready")
                    ]
        i = 1
        for processor , data in collection:
            if processor.validate(data):
                result4 = processor.process(data)
                print(f"Result {i}: {result4}")
            i+=1
        print("\nFoundation systems online. Nexus ready for advanced streams.")




        


        




        
    



    








    
        







