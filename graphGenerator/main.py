#!/usr/bin/env python3
"""
Graph Generator - Generate various types of graphs from CSV data using YAML configuration.
Supports line charts, scatter plots, plots with markers, and bar charts.
"""

import os
import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import argparse


def load_config(config_path: str) -> dict:
    """
    Load and parse the YAML configuration file.

    Args:
        config_path (str): Path to the YAML config file

    Returns:
        dict: Parsed configuration dictionary
    """
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Config file '{config_path}' not found!")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        sys.exit(1)


def generate_graph(df: pd.DataFrame, graph_config: dict) -> None:
    """
    Generate a graph based on the provided configuration.

    Args:
        df (pd.DataFrame): Input data frame containing the plot data
        graph_config (dict): Configuration for the specific graph
    """
    # Clear any existing plots
    plt.clf()
    
    # Set figure size if specified
    if 'figure_size' in graph_config:
        plt.figure(figsize=tuple(graph_config['figure_size']))
    
    x = df[graph_config['x_column']]
    for y_column in graph_config['y_columns']:
        y = df[y_column]
        kind = graph_config['kind']

        if kind == 'line':
            plt.plot(x, y, label=y_column)
        elif kind == 'plot':  # Line with markers
            plt.plot(x, y, marker='o', label=y_column)
        elif kind == 'scatter':
            plt.scatter(x, y, label=y_column)
        elif kind == 'bar':
            plt.bar(x, y, label=y_column)
        else:
            print(f"[WARNING] Unsupported graph type: {kind}")
            return

    plt.title(graph_config['title'])
    plt.xlabel(graph_config.get('x_label', graph_config['x_column']))
    plt.ylabel(graph_config.get('y_label', ", ".join(graph_config['y_columns'])))
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Ensure output directory exists
    output_dir = os.path.dirname(graph_config['output_file'])
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    try:
        plt.savefig(graph_config['output_file'])
    except Exception as e:
        print(f"Error saving graph to {graph_config['output_file']}: {e}")
    finally:
        plt.close()  # Properly close the figure to free memory


def load_dataframe(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame with error handling.

    Args:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded DataFrame
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Data file '{file_path}' not found!")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: Data file '{file_path}' is empty!")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading data file '{file_path}': {e}")
        sys.exit(1)


def main():
    """Main function to run the graph generation process."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate graphs from CSV data')
    parser.add_argument('--input', '-i', type=str, help='Input CSV file path')
    parser.add_argument('--config', '-c', type=str, default='config.yaml', help='Config file path (default: config.yaml)')
    args = parser.parse_args()

    config = load_config(args.config)
    
    if args.input:
        # Handle custom input file
        df = load_dataframe(args.input)
        for graph in config['graphs']:
            if graph['x_column'] in df.columns:
                generate_graph(df, graph)
    else:
        # Handle default examples.csv graphs
        df_examples = load_dataframe('data/examples.csv')
        examples_graphs = [g for g in config['graphs'] if g['x_column'] in df_examples.columns]
        for graph in examples_graphs:
            generate_graph(df_examples, graph)
        
        # Handle fibonacci.csv graphs
        df_fibonacci = load_dataframe('data/fibonacci.csv')
        fibonacci_graphs = [g for g in config['graphs'] if g['x_column'] in df_fibonacci.columns]
        for graph in fibonacci_graphs:
            generate_graph(df_fibonacci, graph)


if __name__ == "__main__":
    main()
