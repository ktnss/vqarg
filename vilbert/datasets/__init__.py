from .concept_cap_dataset import ConceptCapLoaderTrain, ConceptCapLoaderVal, ConceptCapLoaderRetrieval
from .vqa_dataset import VQAClassificationDataset
from .refer_expression_dataset import ReferExpressionDataset
from .retreival_dataset import RetreivalDataset, RetreivalDatasetVal
from .vcr_dataset import VCRDataset



# from .flickr_retreival_dataset import FlickrRetreivalDatasetTrain, FlickrRetreivalDatasetVal

__all__ = [
		   "VCRDataset", 
		   ]

DatasetMapTrain = {
				   'TASK1': VCRDataset,
				   'TASK2': VCRDataset,
				   }		

DatasetMapEval = {
				 'TASK1': VCRDataset,
				 'TASK2': VCRDataset,			   
				}
