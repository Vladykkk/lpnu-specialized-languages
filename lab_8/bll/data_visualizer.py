import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def basic_visualization(self, column):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data[column])
        plt.title(f'Basic Visualization of {column}')
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.savefig('output_basic.png')
        plt.show()

    def scatter_plot(self, column_x, column_y):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data[column_x], self.data[column_y])
        plt.title(f'Scatter Plot of {column_x} vs {column_y}')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.savefig('output_scatter.png')
        plt.show()

    def save_plot(self, file_name):
        plt.savefig(file_name)
        print(f'Візуалізацію збережено як {file_name}')
