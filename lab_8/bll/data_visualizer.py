import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, data):
        self._data = data

    def save_plot(self, file_name):
        plt.savefig(file_name)
        print(f'Візуалізацію збережено як {file_name}')

class DataVisualizer(Visualizer):
    def basic_visualization(self, column):
        plt.figure(figsize=(10, 6))
        plt.plot(self._data[column])
        plt.title(f'Basic Visualization of {column}')
        plt.xlabel('Index')
        plt.ylabel(column)
        self.save_plot(f'{column}_basic.png')
        plt.show()

    def scatter_plot(self, column_x, column_y):
        plt.figure(figsize=(10, 6))
        plt.scatter(self._data[column_x], self._data[column_y])
        plt.title(f'Scatter Plot of {column_x} vs {column_y}')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        self.save_plot(f'{column_x}_{column_y}_scatter.png')
        plt.show()
