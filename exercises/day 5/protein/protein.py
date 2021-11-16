from collections import deque
import numpy as np
import plotly.graph_objects as go

class Protein(object):

    def __init__(self, name, sequence, dictionary):
        self.name = name
        self.sequence = sequence
        self.dictionary = dictionary
    
    def y_data_builder(self, metric = "hydropathy"):
        """Creates list with values of given column from list of dicts.

        Args:
            metric (str, optional): Is equal to the key of the metrics dictionary the class was initialized with. 
            Defaults to "hydropathy".

        Returns:
            y_data (list): Values of given metric.
        """
        y_data = []
        for aa in self.sequence:
            y_data.append(self.dictionary[metric][aa])
        return y_data

    def sliding_window(self, y_data, window_size):
        """Calculates mean of elements of window_size of sequence.

        Args:
            y_data (list): List of floats or integers which are the elements used to caculate mean.
            window_size (int, optional): defines of how many elements the mean is calculated.

        Returns:
            mean_list (list): List with all mean values.
        """
        sliding_window = deque([], maxlen = window_size)
        mean_list = []
        for y in y_data:
            sliding_window.append(y)
            mean = np.mean(list(sliding_window))
            mean_list.append(mean)
        return mean_list

    def plot(self, metric="hydropathy", window_size=1):
        """Create plotly fig object.

        The title of the fig contains protein name, 
        the x axis is the amino acid position (int) and
        y axis shows the metric at each given position. 
        A windows size can be specified to average the metrics using a sliding window 

        Args:
            metric (str, optional): Is equal to the key of the metrics dictionary the class was initialized with. 
                Defaults to "hydropathy".
            window_size (int, optional): Size of the sliding window. Defaults to 1.
        """

        y_data = self.y_data_builder(self, metric= "hydropathy")

        mean_list = self.sliding_window(self, y_data, window_size)

        data = [
            go.Bar(
                y = mean_list,
                x = [x for x in range(len(self.sequence))]
            )
        ]
        fig = go.Figure(data=data)
        fig.update_layout(template="plotly", title=self.name)
        return fig