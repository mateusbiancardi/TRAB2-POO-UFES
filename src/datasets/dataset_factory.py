
from typing import Dict
from .dataset_interface import DatasetInterface
from .image_dataset import ImageDataset
from .news_dataset import NewsDataset


def create_dataset(path: str, train_path, type: str) -> DatasetInterface:
    if type == 'image':
        return ImageDataset(path)
    elif type == 'news':
        return NewsDataset(path, train_path)
    else:
        raise Exception("Dataset type not found.")
