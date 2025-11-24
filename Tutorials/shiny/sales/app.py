from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import calendar

import plotly.express as px
from shiny import reactive
from shiny.express import render, input, ui
from shinywidgets import render_plotly

ui.tags.style(
    """
        .header-container {
            display: flex;
            align-items: center;
            height: 60px;
            background-color: #5DADE2;
        }

        .logo-container {
            margin-right: 5px;
            height: 100% !important;
            padding: 10px;
        }
        .logo-container img {
            height: 40px;
        }

        .title-container h2 {
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin: 0;
        }
    """
)

ui.page_opts(window_title="Sales Dashboard", fillable=False)

# ui.input_checkbox('bar_color', 'Make bars red?', False)

# @reactive.calc
# def color():
#     return "red" if input.bar_color() else "blue"

# ui.input_numeric('n', 'Number of Items', 5, min=0, max=20)

@reactive.calc
def dat():
    infile = Path(__file__).parent / "data/sales.csv"
    df = pd.read_csv(infile)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.month_name()
    df['value'] = df['quantity_ordered'] * df['price_each']
    df['hour'] = df["order_date"].dt.hour
    return df

# @render_plotly
# def plot1():
#     df = dat()
#     top_sales = df.groupby('product')['quantity_ordered'].sum().nlargest(input.n()).reset_index()
#     return px.bar(top_sales, x='product', y='quantity_ordered')
# @render.data_frame
# def data():
#     return dat()

with ui.div(class_="header-container"):
    with ui.div(class_="logo-container"):
        @render.image
        def image():
            img = {"src": Path(__file__).parent / "assets/shiny-logo.png", "width": "100px"}
            return img
    
    with ui.div(class_="title-container"):
        ui.h2("Sales Dashboard")

with ui.layout_column_wrap(width=1/2): # layout_column for hard fixed positioning
    with ui.card():
        ui.card_header("Sellers")
        with ui.navset_underline(id="tab", footer=ui.input_numeric('n', 'Number of Items', 5, min=0, max=20)):
            with ui.nav_panel("Top Sellers ($)"):
                @render_plotly
                def top_sellers():
                    df = dat()
                    top_sales = df.groupby('product')['value'].sum().nlargest(input.n()).reset_index()
                    return px.bar(top_sales, x='product', y='value')
            with ui.nav_panel("Bottom Sellers ($)"):
                @render_plotly
                def bottom_sellers():
                    df = dat()
                    bottom_sales = df.groupby('product')['value'].sum().nsmallest(input.n()).reset_index()
                    return px.bar(bottom_sales, x='product', y='value')
    with ui.card():
        ui.card_header("Sales over Time")
        with ui.layout_sidebar(class_="custom-sidebar"):
            with ui.sidebar(bg="#f8f8f8"):
                ui.input_selectize(
                "city",
                "Select a City:",
                ['Dallas (TX)', 'Boston (MA)', 'Los Angeles (CA)', 'San Francisco (CA)', 'Seattle (WA)', 'Atlanta (GA)', 'New York City (NY)'],
                multiple=True,
                selected='Los Angeles (CA)'
                )

            @render_plotly
            def sales_over_time_bar():
                df = dat()
                sales = df.groupby(['city', 'month'])['quantity_ordered'].sum().reset_index()
                sales_by_city = sales[sales['city'].isin(input.city())]
                # if multiple=False, then you'd just check == input.city() instead of isin()
                month_orders = calendar.month_name[1:]
                fig = px.bar(sales, x='month', y='quantity_ordered', title=f"Sales over Time -- {input.city()}", category_orders={'month' : month_orders})
                # fig.update_traces(marker_color=color())
                return fig

    with ui.card():
        ui.card_header("Sales by Time of Day Heatmap")
        @render.plot
        def plot_sales_by_time():
            df = dat()
            sales_by_hour = df['hour'].value_counts().reindex(np.arange(0, 24), fill_value=0)
            heatmap_data = sales_by_hour.values.reshape(24, 1)
            sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="coolwarm", cbar=False, xticklabels=[], yticklabels=[f'{i}:00' for i in range(24)])
            plt.title("Number of Orders by Hour of Day")
            plt.xlabel("Hour of Day")
            plt.ylabel("Order Count")

# with ui.card():
#     ui.card_header("Sample Data")
#     @render.data_frame # Adds data table
#     def sample_sales_data():
#         return dat().head(100)

# Consider render.data_grid and render.data_frame for filters option (how to customize filter headers)
