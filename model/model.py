class LayerInfo:
    def __init__(self, layer_id):
        self.layer_id = layer_id
        self.layer_type = ''
        self.activation_function = ''
        self.neurons_number = 0

    def set_layer_type(self, layer_type_index):
        layer_types = {1: "input_layer", 2: "hidden_layer", 3: 'output_layer'}
        self.layer_type = layer_types.get(layer_type_index)
        print(self.layer_type)

    def set_layer_ac_fn(self, layer_ac_fn):
        self.activation_function = layer_ac_fn
        print(self.activation_function)

    def set_neurons_num(self, neurons_num):
        self.neurons_number = neurons_num
        print(self.neurons_number)

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.layer_id, self.layer_type, self.activation_function,
                                           self.neurons_number)


class Layers:
    def __init__(self):
        self.layers = {}

    def add_layer(self, layer_id, layer_info):
        self.layers[layer_id] = layer_info
        # [todo] add log for method add_layer
        # print(self.layers)
        self.print_layers()

    def print_layers(self):
        layers_info_dict = {}
        for layer_id, layer_info in self.layers.items():
            layers_info_dict[layer_id] = str(layer_info)
        print(layers_info_dict)