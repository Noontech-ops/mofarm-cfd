def plot_field(data):
    """Visualize a scalar field from the provided data."""
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.imshow(data, cmap='viridis')
    plt.colorbar(label='Field Value')
    plt.title('Field Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


def plot_comparison(data1, data2, label1='Data 1', label2='Data 2'):
    """Compare two datasets with a line plot."""
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(data1, label=label1)
    plt.plot(data2, label=label2)
    plt.title('Comparison of Datasets')
    plt.xlabel('X-axis')
    plt.ylabel('Values')
    plt.legend()
    plt.show()


def plot_metrics_history(metrics):
    """Plot metrics over time or iterations"""
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    for key, value in metrics.items():
        plt.plot(value, label=key)
    plt.title('Metrics History')
    plt.xlabel('Iterations')
    plt.ylabel('Values')
    plt.legend()
    plt.show()


def plot_parametric_sweep(parameters, results):
    """Visualize results of a parametric sweep"""
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    for param, result in zip(parameters, results):
        plt.plot(param, result, label=f'Param: {param}')
    plt.title('Parametric Sweep Results')
    plt.xlabel('Parameter Value')
    plt.ylabel('Result')
    plt.legend()
    plt.show()