from dal.data_loader import DataLoader
from bll.data_processor import DataProcessor
from bll.data_visualizer import DataVisualizer

class Command:
    def execute(self):
        file_path = 'lab_8/sources/dataset.csv'
        data_loader = DataLoader(file_path)
        data = data_loader.load_data()

        if data is not None:
            processor = DataProcessor(data)
            processed_data = processor.preprocess_data()
            print(processor.get_extreme_values())

            visualizer = DataVisualizer(processed_data)
            visualizer.basic_visualization('Temperature')
            visualizer.scatter_plot('Temperature', 'Humidity')

            visualizer.save_plot('output.png')