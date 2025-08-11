from imports import *
from filter_chat import *

from s3 import *



class BasicOutput(BaseModel):
    Visulization: str


import numpy as np


class bar_chart_visualization_v:
    @tool
    def create_bar_chart_v(data: dict, x_title: str, y_title: str, title: str, save_path: str) -> str:
        """
        Creates and saves a colorful, interactive vertical bar chart for the given data, and returns the file path.

        Parameters:
        - data: A dictionary where keys are labels and values are counts.
        - x_title: Label for the X-axis.
        - y_title: Label for the Y-axis.
        - title: Title of the chart.
        - save_path: Path to save the PNG image.

        Returns:
        - The path where the bar chart image is saved
        """
        labels = list(data.keys())
        counts = list(data.values())

        # Generate a color palette for the bars
        colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))

        # Create a figure and axis
        plt.figure(figsize=(12, 8))

        # Create the vertical bar chart with color palette
        bars = plt.bar(labels, counts, color=colors, edgecolor='black', linewidth=1)

        # Add annotations for counts on each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height}',
                     va='bottom', ha='center', fontsize=12, color='black', fontweight='bold')

        # Add gridlines for better readability
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Set titles and labels, and center-align them
        plt.title(title, fontsize=18, fontweight='bold', color='darkblue')  # Center the title
        plt.xlabel(x_title, fontsize=14, fontweight='bold', color='darkgreen')  # Center the x-label
        plt.ylabel(y_title, fontsize=14, fontweight='bold', color='darkgreen')  # Center the y-label

        # Customize the x-axis labels for better visibility
        plt.xticks(fontsize=12, rotation=45, ha='right', color='darkblue')
        plt.yticks(fontsize=12, color='darkblue')

        # Adjust layout to ensure everything fits nicely without cropping
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
        buffer.seek(0)
        plt.close()  # Close the plot to free up memory

        # Initialize the S3 client
        parts = save_path.split("/")
        bucket_name = parts[2]  # The third part is the bucket name
        s3_path = "/".join(parts[3:])  # Join the remaining parts to form the key

        # Upload the image to S3
        s3_client.upload_fileobj(buffer, bucket_name, s3_path)

        buffer.close()

        # Return the path of the saved chart
        return save_path


bar_chart_v_tool = bar_chart_visualization_v()

import numpy as np
import matplotlib.pyplot as plt


class bar_chart_visualization_h:
    @tool
    def create_bar_chart_h(data: dict, x_title: str, y_title: str, title: str, save_path: str) -> str:
        """
        Creates and saves a colorful, interactive horizontal bar chart for the given data, and returns the file path.

        Parameters:
        - data: A dictionary where keys are labels and values are counts.
        - x_title: Label for the X-axis.
        - y_title: Label for the Y-axis.
        - title: Title of the chart.
        - save_path: Path to save the PNG image.

        Returns:
        - The path where the bar chart image is saved
        """
        labels = list(data.keys())
        counts = list(data.values())

        # Generate a color palette for the bars
        colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))

        # Create a figure and axis
        plt.figure(figsize=(12, 8))

        # Create the horizontal bar chart with color palette
        bars = plt.barh(labels, counts, color=colors, edgecolor='black', linewidth=1)

        # Add annotations for counts on each bar
        for bar in bars:
            plt.text(bar.get_width() - 0.5, bar.get_y() + bar.get_height() / 2, f'{bar.get_width()}',
                     va='center', ha='right', fontsize=12, color='black', fontweight='bold')

        # Add gridlines for better readability
        plt.grid(axis='x', linestyle='--', alpha=0.7)

        # Set titles and labels, and center-align them
        plt.title(title, fontsize=18, fontweight='bold', color='darkblue')  # Center the title
        plt.xlabel(x_title, fontsize=14, fontweight='bold', color='darkgreen')  # Center the x-label
        plt.ylabel(y_title, fontsize=14, fontweight='bold', color='darkgreen')  # Center the y-label

        # Customize the y-axis labels for better visibility
        plt.xticks(fontsize=12, color='darkblue')
        plt.yticks(fontsize=12, color='darkblue')

        # Adjust layout to ensure everything fits nicely without cropping
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
        buffer.seek(0)
        plt.close()  # Close the plot to free up memory

        # Initialize the S3 client
        parts = save_path.split("/")
        bucket_name = parts[2]  # The third part is the bucket name
        s3_path = "/".join(parts[3:])  # Join the remaining parts to form the key

        # Upload the image to S3
        s3_client.upload_fileobj(buffer, bucket_name, s3_path)

        buffer.close()

        # Return the path of the saved chart

        # Return the path of the saved chart
        return save_path


bar_chart_h_tool = bar_chart_visualization_h()


class pie_chart_visualization:

    @tool
    def create_pie_chart(data: dict, title: str, save_path: str) -> str:
        """
        Creates and saves a pie chart for the given data, and returns the file path of the saved chart.

        Parameters:
        - data: A dictionary where keys are labels and values are counts.
        - title: Title of the chart.
        - save_path: Path to save the PNG image.

        Returns:
        - The path where the pie chart image is saved
        """
        labels = list(data.keys())
        sizes = list(data.values())

        # Create a figure with a specific size
        plt.figure(figsize=(8, 8))

        colors = plt.cm.tab20c.colors  # A colorful and diverse colormap
        # Create the pie chart
        wedges, texts, autotexts = plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',  # Display percentage values
            startangle=90,  # Rotate the pie chart to start from the top
            textprops={'fontsize': 12},  # Font size for the text
            colors=plt.cm.Paired.colors  # Use a color map for better visualization
        )

        # Set the title of the chart
        plt.title(title, fontsize=16, ha='center')

        # Adjust layout to ensure everything fits nicely
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
        buffer.seek(0)
        plt.close()  # Close the plot to free up memory

        # Initialize the S3 client
        parts = save_path.split("/")
        bucket_name = parts[2]  # The third part is the bucket name
        s3_path = "/".join(parts[3:])  # Join the remaining parts to form the key

        # Upload the image to S3
        s3_client.upload_fileobj(buffer, bucket_name, s3_path)

        buffer.close()

        # Return the path of the saved chart
        return save_path


pie_chart_visualization_tool = pie_chart_visualization()

Plot_agent = Agent(
    role='Visualization Agent',
    goal=(
        'Analyze the data provided in detail. '
        'This data is generated as response from database by text to sql'
        'You will create bar charts or pie chart based on the provided data.'
    ),
    backstory=(
        'You are an expert in data visualization and will use the bar_chart_h_tool or pie_chart_visualization_tool or bar_chart_v_tool to create Visulization '
        'only use one of tool and generate informative charts based on the data you receive in the response.'
    ),
    tools=[bar_chart_v_tool.create_bar_chart_v,bar_chart_h_tool.create_bar_chart_h,pie_chart_visualization_tool.create_pie_chart ],
    max_iter=3,
    max_retry_limit=3,
    verbose=True
)

# Example task that uses the provided response data to visualize
visualization_task = Task(
    description=(
        "You will receive a {response}"
        "This response contains data in any form. "
        "Your task is to use any of one tools and send data to it in desired format. "
        "Clean anything irrelevant in data for Visualization"
        "You got three options of visualizations, choose any one which suits best to visualize data \n"
        "- You can use the bar_chart_h_tool to create the horizontal bar chart, or \n" 
        "- You can use bar_chart_v_tool for Vertical bar charts or \n "
        "- You can use pie_chart_visualization_tool to create pie chart  \n "
        "and then save the chart image to the provided path {path}."
        "you only have to use one tool at a time to generate Image and save it at path"
    ),
    expected_output="After running the tool if visulization was generate  and saved Successfully \n"
                    "return * visulization :'1'\n"
                     "If data can't be visualized return  * visualized: '0'"
                     "Don't retun Image path only follow JSON schema"   ,

    output_json=BasicOutput,
    agent=Plot_agent
)
#-SINGLE GENERATOR

# Create a crew and add the task
analysis_crew = Crew(
    agents=[Plot_agent],
    tasks=[visualization_task]
)






#sever check
