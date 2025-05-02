{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "hTGUQcicx8QP",
        "_bXx18kmy3OZ",
        "Ue9uvXygzdom"
      ],
      "gpuType": "V28"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "TPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# ⚠️ ⚠️ ⚠️\n",
        "# **Open a new colab yourself and just copy paste the code(s) required, running in this same colab will show errors, due to cross dependencies.**"
      ],
      "metadata": {
        "id": "Dj7fyd9VBOD0"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 1**"
      ],
      "metadata": {
        "id": "hTGUQcicx8QP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install paho-mqtt\n",
        "\n",
        "import paho.mqtt.client as mqtt\n",
        "\n",
        "# Callback when connected to the broker\n",
        "def on_connect(client, userdata, flags, rc):\n",
        "    print(\"Connected with result code \" + str(rc))\n",
        "    client.subscribe(\"iot/test\")\n",
        "\n",
        "# Callback when a message is received\n",
        "def on_message(client, userdata, msg):\n",
        "    print(f\"Message received: {msg.payload.decode()}\")\n",
        "\n",
        "# Create MQTT client instance\n",
        "client = mqtt.Client()\n",
        "client.on_connect = on_connect\n",
        "client.on_message = on_message\n",
        "\n",
        "# Connect to public MQTT broker\n",
        "client.connect(\"broker.hivemq.com\", 1883, 60)\n",
        "\n",
        "# Start loop to process network traffic\n",
        "client.loop_start()\n",
        "\n",
        "# Publish a test message\n",
        "client.publish(\"iot/test\", \"Hello IoT\")\n",
        "\n",
        "# Stop the loop after short delay (optional in production)\n",
        "import time\n",
        "time.sleep(2)  # Allow time for message to be received\n",
        "client.loop_stop()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1BnQ4TiLyGJk",
        "outputId": "f1e4a03f-868e-4b78-d9ae-981af7793b9a"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting paho-mqtt\n",
            "  Downloading paho_mqtt-2.1.0-py3-none-any.whl.metadata (23 kB)\n",
            "Downloading paho_mqtt-2.1.0-py3-none-any.whl (67 kB)\n",
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/67.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.2/67.2 kB\u001b[0m \u001b[31m2.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: paho-mqtt\n",
            "Successfully installed paho-mqtt-2.1.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-4-477232011ba6>:15: DeprecationWarning: Callback API version 1 is deprecated, update to latest version\n",
            "  client = mqtt.Client()\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Connected with result code 0\n",
            "Message received: Pressure = 966.88 hPa\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<MQTTErrorCode.MQTT_ERR_SUCCESS: 0>"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 2**"
      ],
      "metadata": {
        "id": "_bXx18kmy3OZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "import time\n",
        "import json\n",
        "from datetime import datetime\n",
        "\n",
        "# Generate sensor data for temperature, humidity, pressure, and light\n",
        "def generate_sensor_data():\n",
        "    data = {\n",
        "        \"timestamp\": datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\"),\n",
        "        \"temperature\": round(random.uniform(20.0, 30.0), 2),     # °C\n",
        "        \"humidity\": round(random.uniform(40.0, 60.0), 2),        # %\n",
        "        \"pressure\": round(random.uniform(980.0, 1030.0), 2),     # hPa\n",
        "        \"light_intensity\": round(random.uniform(0.0, 1000.0), 2) # lux\n",
        "    }\n",
        "    return data\n",
        "\n",
        "# Collect sensor data for given duration and interval\n",
        "def collect_sensor_data(duration, interval, output_file):\n",
        "    collected_data = []\n",
        "    start_time = time.time()\n",
        "    print(\"Starting sensor data collection...\\n\")\n",
        "\n",
        "    while time.time() - start_time < duration:\n",
        "        data = generate_sensor_data()\n",
        "        collected_data.append(data)\n",
        "        print(\"Collected:\", data)\n",
        "        time.sleep(interval)\n",
        "\n",
        "    # Save to JSON file\n",
        "    with open(output_file, 'w') as f:\n",
        "        json.dump(collected_data, f, indent=4)\n",
        "\n",
        "    print(f\"\\nData saved to {output_file}\")\n",
        "\n",
        "# Main execution\n",
        "if __name__ == \"__main__\":\n",
        "    collect_sensor_data(duration=30, interval=5, output_file=\"enhanced_sensor_data.json\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kKviQoR2y6hN",
        "outputId": "740330b4-c2c2-4615-bab5-b0f72c44bff4"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Starting sensor data collection...\n",
            "\n",
            "Collected: {'timestamp': '2025-05-02 03:19:27', 'temperature': 23.06, 'humidity': 48.56, 'pressure': 1006.53, 'light_intensity': 989.49}\n",
            "Collected: {'timestamp': '2025-05-02 03:19:32', 'temperature': 22.85, 'humidity': 53.21, 'pressure': 1006.77, 'light_intensity': 877.45}\n",
            "Collected: {'timestamp': '2025-05-02 03:19:37', 'temperature': 23.72, 'humidity': 59.86, 'pressure': 990.15, 'light_intensity': 397.12}\n",
            "Collected: {'timestamp': '2025-05-02 03:19:42', 'temperature': 25.11, 'humidity': 56.31, 'pressure': 1024.25, 'light_intensity': 890.76}\n",
            "Collected: {'timestamp': '2025-05-02 03:19:47', 'temperature': 22.88, 'humidity': 55.29, 'pressure': 1010.84, 'light_intensity': 795.58}\n",
            "Collected: {'timestamp': '2025-05-02 03:19:52', 'temperature': 23.63, 'humidity': 43.93, 'pressure': 1001.81, 'light_intensity': 432.45}\n",
            "\n",
            "Data saved to enhanced_sensor_data.json\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 3**"
      ],
      "metadata": {
        "id": "Ue9uvXygzdom"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install dash\n",
        "\n",
        "from dash import Dash, dcc, html\n",
        "from dash.dependencies import Input, Output\n",
        "import plotly.graph_objs as go\n",
        "import random, time, threading\n",
        "\n",
        "# Simulated data store\n",
        "data = {'time': [], 'temperature': [], 'humidity': [], 'air_pressure': []}\n",
        "\n",
        "# Simulated Sensor Data Generator\n",
        "def generate_sensor_data():\n",
        "    while True:\n",
        "        data['temperature'].append(round(random.uniform(20.0, 30.0), 2))\n",
        "        data['humidity'].append(round(random.uniform(40.0, 60.0), 2))\n",
        "        data['air_pressure'].append(round(random.uniform(980.0, 1050.0), 2))\n",
        "        data['time'].append(time.strftime(\"%H:%M:%S\"))\n",
        "\n",
        "        if len(data['time']) > 100:\n",
        "            for key in data:\n",
        "                data[key] = data[key][-100:]\n",
        "\n",
        "        time.sleep(1)\n",
        "\n",
        "# Start sensor data thread\n",
        "threading.Thread(target=generate_sensor_data, daemon=True).start()\n",
        "\n",
        "# Dash App\n",
        "app = Dash(__name__)\n",
        "app.layout = html.Div([\n",
        "    html.H1(\"Real-Time IoT Sensor Dashboard\", style={'textAlign': 'center'}),\n",
        "\n",
        "    # Digital Displays\n",
        "    html.Div([\n",
        "        html.Div(id='temperature-digital', style={'fontSize': '30px', 'margin': '10px'}),\n",
        "        html.Div(id='humidity-digital', style={'fontSize': '30px', 'margin': '10px'}),\n",
        "        html.Div(id='air-pressure-digital', style={'fontSize': '30px', 'margin': '10px'})\n",
        "    ], style={'display': 'flex', 'justifyContent': 'space-around'}),\n",
        "\n",
        "    # Graphs\n",
        "    html.Div([\n",
        "        dcc.Graph(id='temperature-graph'),\n",
        "        dcc.Graph(id='humidity-graph'),\n",
        "        dcc.Graph(id='air-pressure-graph')\n",
        "    ]),\n",
        "\n",
        "    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)\n",
        "])\n",
        "\n",
        "@app.callback(\n",
        "    [Output('temperature-graph', 'figure'),\n",
        "     Output('humidity-graph', 'figure'),\n",
        "     Output('air-pressure-graph', 'figure'),\n",
        "     Output('temperature-digital', 'children'),\n",
        "     Output('humidity-digital', 'children'),\n",
        "     Output('air-pressure-digital', 'children')],\n",
        "    [Input('interval-component', 'n_intervals')]\n",
        ")\n",
        "def update_dashboard(n):\n",
        "    temp_fig = go.Figure([go.Scatter(x=data['time'], y=data['temperature'], mode='lines+markers')])\n",
        "    temp_fig.update_layout(title=\"Temperature Over Time\", xaxis_title=\"Time\", yaxis_title=\"°C\")\n",
        "\n",
        "    hum_fig = go.Figure([go.Scatter(x=data['time'], y=data['humidity'], mode='lines+markers')])\n",
        "    hum_fig.update_layout(title=\"Humidity Over Time\", xaxis_title=\"Time\", yaxis_title=\"%\")\n",
        "\n",
        "    press_fig = go.Figure([go.Scatter(x=data['time'], y=data['air_pressure'], mode='lines+markers')])\n",
        "    press_fig.update_layout(title=\"Air Pressure Over Time\", xaxis_title=\"Time\", yaxis_title=\"hPa\")\n",
        "\n",
        "    temp_val = f\"Temperature: {data['temperature'][-1]} °C\" if data['temperature'] else \"N/A\"\n",
        "    hum_val = f\"Humidity: {data['humidity'][-1]} %\" if data['humidity'] else \"N/A\"\n",
        "    press_val = f\"Air Pressure: {data['air_pressure'][-1]} hPa\" if data['air_pressure'] else \"N/A\"\n",
        "\n",
        "    return temp_fig, hum_fig, press_fig, temp_val, hum_val, press_val\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run(debug=True)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "_ncAKAuRzgWA",
        "outputId": "31c3c085-2284-495b-b122-f4590a1b177f"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting dash\n",
            "  Using cached dash-3.0.4-py3-none-any.whl.metadata (10 kB)\n",
            "Collecting Flask<3.1,>=1.0.4 (from dash)\n",
            "  Using cached flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)\n",
            "Requirement already satisfied: Werkzeug<3.1 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.6)\n",
            "Requirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.24.1)\n",
            "Requirement already satisfied: importlib-metadata in /usr/lib/python3/dist-packages (from dash) (4.6.4)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash) (4.13.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from dash) (2.32.3)\n",
            "Requirement already satisfied: retrying in /usr/local/lib/python3.11/dist-packages (from dash) (1.3.4)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.11/dist-packages (from dash) (1.6.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from dash) (75.2.0)\n",
            "Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (3.1.6)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
            "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (8.1.8)\n",
            "Collecting blinker>=1.6.2 (from Flask<3.1,>=1.0.4->dash)\n",
            "  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash) (9.1.2)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash) (25.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Werkzeug<3.1->dash) (3.0.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2.4.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2025.4.26)\n",
            "Requirement already satisfied: six>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from retrying->dash) (1.17.0)\n",
            "Using cached dash-3.0.4-py3-none-any.whl (7.9 MB)\n",
            "Using cached flask-3.0.3-py3-none-any.whl (101 kB)\n",
            "Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
            "Installing collected packages: blinker, Flask, dash\n",
            "  Attempting uninstall: blinker\n",
            "    Found existing installation: blinker 1.4\n",
            "\u001b[1;31merror\u001b[0m: \u001b[1muninstall-distutils-installed-package\u001b[0m\n",
            "\n",
            "\u001b[31m×\u001b[0m Cannot uninstall blinker 1.4\n",
            "\u001b[31m╰─>\u001b[0m It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'dash'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-7-33a22ad1b245>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msystem\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'pip install dash'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mdash\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDash\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdcc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhtml\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdash\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdependencies\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mInput\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOutput\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgraph_objs\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mgo\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'dash'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 4**"
      ],
      "metadata": {
        "id": "6e-Iy9zk0DHI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "import random\n",
        "import time\n",
        "import matplotlib.pyplot as plt\n",
        "from datetime import datetime\n",
        "\n",
        "# ThingSpeak API Key\n",
        "# Note: Replace these with your actual API keys and channel ID\n",
        "WRITE_API_KEY = \"2BP633L92JHJRV62\" # Placeholder key from document\n",
        "READ_API_KEY = \"52YPAO3SPC89EKAJ\"   # Placeholder key from document\n",
        "CHANNEL_ID = \"2832723\"           # Placeholder ID from document\n",
        "\n",
        "# URL for updating data\n",
        "WRITE_URL = f\"https://api.thingspeak.com/update\" # Corrected URL format based on usage\n",
        "\n",
        "def send_data_to_thingspeak(temperature, humidity):\n",
        "    \"\"\"Sends temperature and humidity data to ThingSpeak.\"\"\"\n",
        "    url = f'{WRITE_URL}?api_key={WRITE_API_KEY}&field1={temperature}&field2={humidity}'\n",
        "    response = requests.get(url)\n",
        "\n",
        "    if response.status_code == 200:\n",
        "        print(f\"Data sent successfully: Temp={temperature}°C, Humidity={humidity}%\")\n",
        "    else:\n",
        "        print(f\"Failed to send data. Status code: {response.status_code}\") # Added status code for debugging\n",
        "\n",
        "# Simulated Sensor Data Upload\n",
        "for _ in range(10): # Sending 10 data points\n",
        "    temp = round(random.uniform(20.0, 30.0), 2)\n",
        "    hum = round(random.uniform(40.0, 60.0), 2)\n",
        "\n",
        "    send_data_to_thingspeak(temp, hum)\n",
        "    time.sleep(15) # ThingSpeak allows updates every 15 seconds\n",
        "\n",
        "def retrieve_data_from_thingspeak():\n",
        "    \"\"\"Retrieves the latest data from ThingSpeak.\"\"\"\n",
        "    url = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=10'\n",
        "    response = requests.get(url).json()\n",
        "\n",
        "    feeds = response['feeds']\n",
        "\n",
        "    # Ensure feeds is not empty before processing\n",
        "    if not feeds:\n",
        "        print(\"No data retrieved from ThingSpeak.\")\n",
        "        return [], [], []\n",
        "\n",
        "    timestamps = [datetime.strptime(feed['created_at'], '%Y-%m-%dT%H:%M:%SZ') for feed in feeds]\n",
        "    temperatures = [float(feed['field1']) for feed in feeds]\n",
        "    humidities = [float(feed['field2']) for feed in feeds]\n",
        "\n",
        "    return timestamps, temperatures, humidities\n",
        "\n",
        "# Retrieve and Plot Data\n",
        "timestamps, temperatures, humidities = retrieve_data_from_thingspeak()\n",
        "\n",
        "if timestamps: # Proceed only if data was retrieved\n",
        "    plt.figure(figsize=(12, 6))\n",
        "\n",
        "    plt.plot(timestamps, temperatures, label='Temperature (°C)', marker='o')\n",
        "    plt.plot(timestamps, humidities, label='Humidity (%)', marker='s')\n",
        "\n",
        "    plt.xlabel('Time')\n",
        "    plt.ylabel('Value')\n",
        "    plt.title('IoT Sensor Data from ThingSpeak')\n",
        "    plt.legend()\n",
        "    plt.grid(True)\n",
        "    plt.xticks(rotation=45)\n",
        "    plt.tight_layout()\n",
        "    plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 785
        },
        "id": "Xhyl75Ql0JLh",
        "outputId": "2bda16d6-7ae7-4f2d-e0c3-b83f310327f0"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Data sent successfully: Temp=25.05°C, Humidity=44.44%\n",
            "Data sent successfully: Temp=20.48°C, Humidity=40.65%\n",
            "Data sent successfully: Temp=26.9°C, Humidity=48.98%\n",
            "Data sent successfully: Temp=29.6°C, Humidity=52.92%\n",
            "Data sent successfully: Temp=20.85°C, Humidity=54.46%\n",
            "Data sent successfully: Temp=29.62°C, Humidity=52.34%\n",
            "Data sent successfully: Temp=25.33°C, Humidity=43.76%\n",
            "Data sent successfully: Temp=23.6°C, Humidity=49.01%\n",
            "Data sent successfully: Temp=29.23°C, Humidity=46.35%\n",
            "Data sent successfully: Temp=23.35°C, Humidity=41.27%\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x600 with 1 Axes>"
            ],
            "image/png": "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gwZ8+OGHGVbQu379+gwfPpwlS5bw6aefcvbsWXx8fKhatSoffvhhcnIIIF++fGzatIn33nuPefPm8dVXXxEQEECFChX48MMP7/raDz74ICEhIfz6668cP34cT09PHnzwQZYsWULt2rWTj5s0aRIlSpRg6tSpzJ8/n/z58zNo0KAMmfIWGxvLs88+C4Cnpyd58+alWrVqvPvuu7Rp0war9cYg8oCAABYuXMirr77K4MGDyZUrF507d6ZRo0apVvx76aWX2LFjB1OmTOGzzz6jaNGitGzZkm7dunHq1CkmTJjAsmXLKF++PDNmzGDOnDmsWrXqvh/Pf1WoUIE//viDQYMGMWrUKJKSkqhVqxYzZsygVq1aGX69rO67774jf/78zJo1i/nz59O4cWN++OEHypQpk6IW08cff8ycOXNYvHgxEydOJC4ujiJFivDSSy8xePBg/P39U5y3QYMGBAcHM2zYMMLCwihfvjxTp05NUWctve+f+3mNdO7cmUuXLvHSSy/h6+vLRx99lCHPm4iIiL1YbBldtVJEREREJIvasWMHVatWZcaMGXTq1Omu72+xWOjTpw9ffvllJkQnIiKSs6imlIiIiIhkS1evXk3VNmbMGKxWa4ri9SIiImIOTd8TERERkWxp9OjRbN26lUceeQRnZ2eWLFnCkiVLeP7553PUSoQiIiJZlZJSIiIiIpItPfzww4SGhjJ8+HAuX75MkSJFGDp0KO+8847ZoYmIiAiqKSUiIiIiIiIiIiZQTSkREREREREREbE7JaVERERERERERMTusn1NqaSkJE6cOIGPjw8Wi8XscEREREREREREsjWbzcalS5coWLAgVmva46GyfVLqxIkTWl1FRERERERERMTOwsPDKVy4cJq3Z/uklI+PD2A8Eb6+vpl+vfj4eJYvX07Tpk1xcXHJ9OtJxlMfOj71oWNT/zk+9aFjU/85PvWh41MfOjb1n+NTH96/qKgogoKCknMyacn2SanrU/Z8fX3tlpTy9PTE19dXL14HpT50fOpDx6b+c3zqQ8em/nN86kPHpz50bOo/x6c+zDh3KqOkQuciIiIiIiIiImJ3SkqJiIiIiIiIiIjdKSklIiIiIiIiIiJ2l+1rSomIiIiIiIg4qsTEROLj480OI0eJj4/H2dmZmJgYEhMTzQ4nS3JxccHJyem+z6OklIiIiIiIiEgWY7PZOHXqFBEREWaHkuPYbDby589PeHj4HQt152T+/v7kz5//vp4jJaVEREREREREspjrCam8efPi6emp5IgdJSUlcfnyZby9vbFaVfXov2w2G9HR0Zw5cwaAAgUK3PO5lJQSERERERERyUISExOTE1IBAQFmh5PjJCUlERcXh7u7u5JSafDw8ADgzJkz5M2b956n8pn67A4dOhSLxZJiK1u2bPLtDRs2THV77969TYxYREREREREJHNdryHl6elpciQiabv++ryfmmemj5SqUKECK1asSN53dk4ZUq9evXjvvfeS9/WmFBERERERkZxAU/YkK8uI16fpSSlnZ2fy58+f5u2enp63vV1ERERERERERByP6ZMjDx48SMGCBSlRogSdOnUiLCwsxe3ff/89efLkoWLFigwaNIjo6GiTIhURERERERERyVr+97//8fzzz2fY+eLi4ihWrBhbtmzJsHOmxdSRUrVq1WLq1KmUKVOGkydPMmzYMOrVq8eePXvw8fGhY8eOFC1alIIFC7Jr1y7efPNN9u/fz7x589I8Z2xsLLGxscn7UVFRgDHH8X7mOabX9WvY41qSOdSHjk996NjUf45PfejY1H+OT33o+NSHji0j+i8+Ph6bzUZSUhJJSUn3fJ7EJBubj17gzKVY8vq4UaNYbpysmTMl8E6Frt99912GDBmSKdfOaDabLfm/t3v+S5QowSuvvMIrr7xir9BSOXXqFGPHjmXnzp3JsV65coWePXuyZs0aGjRowKRJk1KUQjp16hQjR45k8eLFHD9+nLx58/Lggw/yyiuv0KhRI5ydnXn11Vd58803CQ0NTfPaSUlJ2Gw24uPjU/V/el//Ftv1ZzsLiIiIoGjRonz66af06NEj1e0rV66kUaNGHDp0iJIlS97yHEOHDmXYsGGp2mfOnKl6VCIiIiIiIpLlXS9zExQUhKur6z2d47f95xm94h9OX4pLbsvn48objUvQqEzGr+h3+vTp5P+fP38+I0eOZPPmzcltXl5eeHt7Z/h1M5rNZiMxMTFVvetbqVy5Mi+++CIvvvjifV0zLi7unvv5448/ZsOGDfz0008p2sLCwnjhhRcYP348xYsX59VXXwUgLCyMZs2a4efnx6BBgyhfvjzx8fGsXLmSadOmsWnTJsDIz5QpU4ZVq1ZRrly5NOMODw/n1KlTJCQkpLgtOjqa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nD2MWlRFakNQbQiqAe5+pj0EERERkaxKSSkREZGs7Mr5lKOerhcdj4m49fFWZwgodaPeU95yEFgOchc3RgLJ/fHwh1JNjA2MovAnd94onh62Hq5egKN/GBsAFshXMeVoKr9CZj0CERERkSxDSSkREZGsICbyP6Oero2CunLm1sdbrMbKcteTTtcTULlLauqYPTm7QVBNY6uDMYrt3MGb6lKth4tH4PRuY9v8jXE/vyI3JalqG32oEWsiIiKSwygpJSIiYk9xV64lnf5TdDzqeNr38S96Y7rd9el3eUqDi7v94pb0sViMaZKBpaFaV6Pt0qkbhdPD1sOp3RAZBrvDYPePxjHufhBU68ZIqoIPqX9FREQk21NSSkREJDPExxir2/236HjEsbTv41vo2sinm2o+5SkDbt72i1synk9+qNDa2ABiL8PxLTeSVOGbjZFyB5cbG4CTKxSseiNJFVQLPHOb9QhEREQcwtGjRylevDjbt2+nSpUqtzxm1apVPPLII1y8eBF/f3+mTp1K//79iYiIyJSYnn32WcqVK8fbb799z+d45plnqFGjBq+++moGRpY1KCklIiJyPxLj4fyh1EXHL/wDtqRb38crb+qaT4FljHpFkv25eUOJhsYGkJhgTO27nqQK22AUsg/faGx/jjWOCyx7bTRVsJGsylUs562QKCIi6RMRDtHn077dM8BYyCODdevWjYiICH7++ecU7f9NBGWWoKAgTp48SZ48edJ9n6effpoWLVok7w8dOpSff/6ZVatW3Xc8O3fuZPHixYwfPz657eOPP2b06NEAvPnmmykSTRs3buSll15i48aNODvfSNcMHjyY+vXr07NnT/z8stfiKUpKiYhI9pZRH8qSEuHCkZtGPV1LQp0/CEkJt76PR66U9Z6uJ6C8Au7tsUj25ORsjIoqWBVqv2jUpbp45KYpfxvg3H4j2Xl2H2ybZtzPO/+NkVRFahvF1J300U5EJMeLCIcvqxmLcaTF2Q36bs2UxJSZnJycyJ8//13dx8PDAw8Pj0yJ54svvqB9+/Z4exuj3nft2sW7777LwoULsdlsPP744zRt2pRKlSqRkJBA7969mThxYoqEFEDFihUpWbIkM2bMoE+fPpkSq1n0yUVERLKve/lQlpRk1Pv5b9HxcwchIebW53D1uVbv6T9Fx73zaSSL3D2LxShin7sEVOlo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M507d87oWEREREREREREJIe466TUd999d9vbu3Tpcs/BiIiIiIiIiIhIznDXSalXXnklxX58fDzR0dG4urri6emppJSIiIiIiIiIiNzRXa++d/HixRTb5cuX2b9/P3Xr1lWhcxERERERERERSZe7TkrdSqlSpfjggw9SjaISERERERERERG5lQxJSoFR/PzEiRMZdToREREREREREcnG7rqm1IIFC1Ls22w2Tp48yZdffkmdOnUyLDAREREREREREcm+7jop1bp16xT7FouFwMBAHn30UT755JOMiktERERERERERLKxu05KJSUlZUYcIiIiIiIiIiKSg2RYTSkREREREREREZH0StdIqYEDB6b7hJ9++uk9ByMiIiIiIiIiIjlDupJS27dvT9fJLBbLfQUjIiIiIiIiIiI5Q7qSUr///ntmxyEiIiIiIiIiIjmIakqJiIiIiIiIiIjd3fXqewBbtmzhxx9/JCwsjLi4uBS3zZs3L0MCExERERERERGR7OuuR0rNnj2bhx9+mL179zJ//nzi4+P566+/WLlyJX5+fpkRo4iIiIiIiIiIZDN3nZQaOXIkn332Gb/++iuurq6MHTuWffv28dRTT1GkSJHMiFFERERERERERLKZu05KHT58mMceewwAV1dXrly5gsViYcCAAUycODHDAxQRERERERERkeznrpNSuXLl4tKlSwAUKlSIPXv2ABAREUF0dHTGRiciIiIiIiIiItlSupNS15NP9evXJzQ0FID27dvzyiuv0KtXLzp06ECjRo0yJ0oREREREREREclW0r36XuXKlalRowatW7emffv2ALzzzju4uLiwbt062rZty+DBgzMtUBERERERERERyT7SnZRavXo1U6ZMYdSoUYwYMYK2bdvSs2dP3nrrrcyMT0REREREREREsqF0T9+rV68e3377LSdPnuSLL77g6NGjNGjQgNKlS/Phhx9y6tSpzIxTRERERERERESykbsudO7l5UX37t1ZvXo1Bw4coH379owbN44iRYrwxBNPZEaMIiIiIiIiIiKSzdx1UupmDzzwAG+//TaDBw/Gx8eHRYsWZVRcIiIiIiIiIiKSjaW7ptR/rVmzhm+//Za5c+ditVp56qmn6NGjR0bGJiIiIiIiIiIi2dRdJaVOnDjB1KlTmTp1KocOHeLhhx/m888/56mnnsLLyyuzYhQRERERERERkWwm3Ump5s2bs2LFCvLkyUOXLl147rnnKFOmTGbGJiIiIiIiIiIi2VS6k1IuLi789NNPPP744zg5OWVmTCIiIiIiIiIiks2lOym1YMGCzIxDRERERERERERykPtafU9EREREREREROReKCklIiIiIiIiIiJ2p6SUiIiIiIiIiIjYnZJSIiIiIiIiIiJid0pKiYiIiIiIiIiI3ZmalBo/fjyVK1fG19cXX19fgoODWbJkSfLtDRs2xGKxpNh69+5tYsQiIiIiIiIiIpIRnM28eOHChfnggw8oVaoUNpuNadOm0apVK7Zv306FChUA6NWrF++9917yfTw9Pc0KV0REREREREREMoipSamWLVum2B8xYgTjx49nw4YNyUkpT09P8ufPb0Z4IiIiIiIiIiKSSUxNSt0sMTGROXPmcOXKFYKDg5Pbv//+e2bMmEH+/Plp2bIl//vf/247Wio2NpbY2Njk/aioKADi4+OJj4/PvAdwzfVr2ONakjnUh45PfejY1H+OT33o2NR/jk996PjUh45N/ef41If3L73PncVms9kyOZbb2r17N8HBwcTExODt7c3MmTNp0aIFABMnTqRo0aIULFiQXbt28eabb1KzZk3mzZuX5vmGDh3KsGHDUrXPnDlTU/9ERERERERERDJZdHQ0HTt2JDIyEl9f3zSPMz0pFRcXR1hYGJGRkfz0009MmjSJ1atXU758+VTHrly5kkaNGnHo0CFKlix5y/PdaqRUUFAQ586du+0TkVHi4+MJDQ2lSZMmuLi4ZPr1JOOpDx2f+tCxqf8cn/rQsan/HJ/60PGpDx2b+s/xqQ/vX1RUFHny5LljUsr06Xuurq488MADAFSrVo3NmzczduxYJkyYkOrYWrVqAdw2KeXm5oabm1uqdhcXF7u+mOx9Pcl46kPHpz50bOo/x6c+dGzqP8enPnR86kPHpv5zfOrDe5fe582ayXHctaSkpBQjnW62Y8cOAAoUKGDHiEREREREREREJKOZOlJq0KBBNG/enCJFinDp0iVmzpzJqlWrWLZsGYcPH06uLxUQEMCuXbsYMGAA9evXp3LlymaGLSIiIiIiIiIi98nUpNSZM2fo0qULJ0+exM/Pj8qVK7Ns2TKaNGlCeHg4K1asYMyYMVy5coWgoCDatm3L4MGDzQxZREREREREREQygKlJqcmT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DA0NYWNjg0mTJsHb2xsff/wxrl+/jqioKADADz/8gJYtW2Lu3Lnw9fVFy5YtsXz5chw8eBAJCQki/zRERERE98aeUkREREQ6JCgoSPtnhUIBa2trBAYGarfZ2dkBALKzswEAkZGROHjw4F37UyUlJaFp06ZPOWIiIiKix8OiFBEREZEO0dPTq/G1TCarsa16VT+NRgMAuHnzJgYMGICvvvrqju/l4ODwFCMlIiIiejIsShERERFJWKtWrfDHH3/A3d0dSiUv7YiIiEg62FOKiIiISMKmTp2KvLw8jBgxAqdPn0ZSUhL+/vtvjBs3Dmq1WuzwiIiIiO6JRSkiIiIiCXN0dMTx48ehVqvRu3dvBAYGYsaMGbCwsIBczks9IiIi0l0yQRAEsYMgIiIiIiIiIqKGhY/PiIiIiIiIiIiozrEoRUREREREREREdY5FKSIiIiIiIiIiqnMsShERERERERERUZ1jUYqIiIiIiIiIiOoci1JERERERERERFTnWJQiIiIiIiIiIqI6x6IUERERERERERHVORaliIiIiIiIiIiozrEoRUREREREREREdY5FKSIiIiIiIiIiqnMsShERERERERERUZ37f3uQp8MbaPnlAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 5**"
      ],
      "metadata": {
        "id": "T_MCY5Jw0wKF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install filterpy\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "from filterpy.kalman import KalmanFilter\n",
        "from filterpy.common import Q_discrete_white_noise\n",
        "\n",
        "# Simulated Sensor Data Generation\n",
        "def generate_sensor_data(n=100):\n",
        "    np.random.seed(42)\n",
        "    temperature = np.random.normal(25, 2, n)  # Mean 25C, Std Dev 2\n",
        "    humidity = np.random.normal(50, 5, n)  # Mean 50%, Std Dev 5\n",
        "    return pd.DataFrame({'Temperature': temperature, 'Humidity': humidity})\n",
        "\n",
        "# Moving Average Filter\n",
        "def moving_average_filter(data, window_size=5):\n",
        "    return data.rolling(window=window_size, center=True).mean()\n",
        "\n",
        "# Median Filter\n",
        "def median_filter(data, window_size=5):\n",
        "    return data.rolling(window=window_size, center=True).median()\n",
        "\n",
        "# Threshold-Based Filtering\n",
        "def threshold_filter(data, temp_range=(20, 30), hum_range=(40, 60)):\n",
        "    filtered_data = data[(data['Temperature'].between(*temp_range)) &\n",
        "                         (data['Humidity'].between(*hum_range))]\n",
        "    return filtered_data\n",
        "\n",
        "# Kalman Filter Implementation\n",
        "def setup_kalman_filter():\n",
        "    kf = KalmanFilter(dim_x=2, dim_z=1)  # State: [position, velocity], Measurement: position\n",
        "    dt = 1.0  # time step\n",
        "    kf.F = np.array([[1., dt], [0., 1.]])  # State transition matrix\n",
        "    kf.H = np.array([[1., 0.]])  # Measurement matrix\n",
        "    kf.R = np.array([[0.5]])  # Measurement noise variance\n",
        "    kf.Q = Q_discrete_white_noise(dim=2, dt=dt, var=0.13)  # Process noise\n",
        "    kf.x = np.array([[0.], [0.]])  # Initial state\n",
        "    kf.P = np.array([[1., 0.], [0., 1.]])  # Initial state covariance\n",
        "    return kf\n",
        "\n",
        "def kalman_filter(data):\n",
        "    kf = setup_kalman_filter()\n",
        "    filtered_data = np.zeros(len(data))\n",
        "    for i, measurement in enumerate(data):\n",
        "        kf.predict()\n",
        "        kf.update(measurement)\n",
        "        filtered_data[i] = kf.x[0]\n",
        "    return filtered_data\n",
        "\n",
        "# Generate and process data\n",
        "data = generate_sensor_data()\n",
        "smoothed_data = moving_average_filter(data)\n",
        "median_filtered_data = median_filter(data)\n",
        "kalman_filtered_temp = kalman_filter(data['Temperature'].values)\n",
        "\n",
        "# Visualization\n",
        "plt.figure(figsize=(12, 8))\n",
        "\n",
        "# Plot 1: Temperature\n",
        "plt.subplot(2, 1, 1)\n",
        "plt.plot(data['Temperature'], 'gray', alpha=0.5, label='Raw Temperature', linestyle='dotted')\n",
        "plt.plot(smoothed_data['Temperature'], 'b', label='Moving Average', alpha=0.7)\n",
        "plt.plot(median_filtered_data['Temperature'], 'g', label='Median Filter', alpha=0.7)\n",
        "plt.plot(kalman_filtered_temp, 'r', label='Kalman Filter', alpha=0.7)\n",
        "plt.ylabel('Temperature (°C)')\n",
        "plt.title('Comparison of Different Filtering Techniques')\n",
        "plt.legend()\n",
        "plt.grid(True, alpha=0.3)\n",
        "\n",
        "# Plot 2: Error Analysis\n",
        "plt.subplot(2, 1, 2)\n",
        "mae_ma = np.abs(data['Temperature'] - smoothed_data['Temperature']).mean()\n",
        "mae_median = np.abs(data['Temperature'] - median_filtered_data['Temperature']).mean()\n",
        "mae_kalman = np.abs(data['Temperature'] - kalman_filtered_temp).mean()\n",
        "errors = [mae_ma, mae_median, mae_kalman]\n",
        "plt.bar(['Moving Average', 'Median Filter', 'Kalman Filter'], errors, color=['blue', 'green', 'red'], alpha=0.6)\n",
        "plt.ylabel('Mean Absolute Error')\n",
        "plt.title('Error Analysis of Different Filters')\n",
        "plt.tight_layout()\n",
        "plt.show()\n",
        "\n",
        "# Print error metrics\n",
        "print(\"\\nError Analysis:\")\n",
        "print(f\"Moving Average MAE: {mae_ma:.3f}°C\")\n",
        "print(f\"Median Filter MAE: {mae_median:.3f}°C\")\n",
        "print(f\"Kalman Filter MAE: {mae_kalman:.3f}°C\")\n"
      ],
      "metadata": {
        "id": "S8micz1n0y4R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 6**"
      ],
      "metadata": {
        "id": "UeHeXI253X6v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import hashlib\n",
        "import random\n",
        "import time\n",
        "\n",
        "def hash_data(data):\n",
        "    \"\"\"Hashes input data using SHA-256 algorithm.\"\"\"\n",
        "    return hashlib.sha256(data.encode()).hexdigest()\n",
        "\n",
        "def verify_hash(original_data, hashed_data):\n",
        "    \"\"\"Verifies whether the hash of the given data matches the stored hash.\"\"\"\n",
        "    try:\n",
        "        return hash_data(original_data) == hashed_data\n",
        "    except Exception as e: # Added basic exception handling\n",
        "        print(f\"Error during verification: {e}\")\n",
        "        return False\n",
        "\n",
        "# Simulate generating and hashing data indefinitely until interrupted\n",
        "try:\n",
        "    while True:\n",
        "        # Generate random IoT sensor data\n",
        "        temperature = round(random.uniform(20.0, 30.0), 1)\n",
        "        humidity = random.randint(40, 80)\n",
        "        sensor_data = f\"Temperature: {temperature}°C, Humidity: {humidity}%\"\n",
        "\n",
        "        # Apply Hashing\n",
        "        hashed_data = hash_data(sensor_data)\n",
        "        verification = verify_hash(sensor_data, hashed_data)\n",
        "\n",
        "        # Print results\n",
        "        print(\"\\nOriginal Data:\", sensor_data)\n",
        "        print(\"Hashed Data:\", hashed_data)\n",
        "        print(\"Verification Successful:\", verification)\n",
        "\n",
        "        # Pause before generating new data\n",
        "        time.sleep(2)\n",
        "\n",
        "except KeyboardInterrupt:\n",
        "    print(\"\\nProcess stopped by user.\")"
      ],
      "metadata": {
        "id": "IuFucdXz3b4q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 7**\n",
        "\n",
        "> ⚠️ if this practical is being asked, run this practical in new colab, otherwise it will give error due to dependencies issue from other practicals in this same colab."
      ],
      "metadata": {
        "id": "w32Um89n4ukV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install flask pyngrok # install libraries required\n",
        "\n",
        "from flask import Flask, request, jsonify\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "device_state = {\"LED\": \"OFF\"} # Initial state of the virtual IoT device\n",
        "\n",
        "@app.route('/')\n",
        "def home():\n",
        "    \"\"\"Displays instructions on how to use the API.\"\"\"\n",
        "    return \"<h1>IoT Device Control</h1><p>Use /control?device=LED&state=ON to control the device.</p>\"\n",
        "\n",
        "@app.route('/control', methods=['GET'])\n",
        "def control_device():\n",
        "    \"\"\"Handles device control requests.\"\"\"\n",
        "    device = request.args.get('device')\n",
        "    state = request.args.get('state')\n",
        "\n",
        "    if device in device_state and state in [\"ON\", \"OFF\"]:\n",
        "        device_state[device] = state\n",
        "        return jsonify({\"message\": f\"{device} turned {state}\"})\n",
        "    else:\n",
        "        return jsonify({\"error\": \"Invalid device or state\"})\n",
        "\n",
        "@app.route('/status', methods=['GET'])\n",
        "def device_status():\n",
        "    \"\"\"Returns the current state of the device(s).\"\"\"\n",
        "    return jsonify(device_state)\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    # This runs the Flask development server.\n",
        "    # For production, use a more robust server like Gunicorn or uWSGI.\n",
        "    app.run(host='0.0.0.0', port=5000)"
      ],
      "metadata": {
        "id": "6j6fjfa54z0G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Practical 8**"
      ],
      "metadata": {
        "id": "7GgGLeIG6vAn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "\n",
        "# Set random seed for reproducibility\n",
        "np.random.seed(42)\n",
        "\n",
        "# Generate dataset with 1000 samples\n",
        "num_samples = 1000\n",
        "\n",
        "# Simulate sensor readings\n",
        "temperature = np.random.randint(30, 100, num_samples)  # Temperature in Celsius\n",
        "vibration = np.round(np.random.uniform(0.1, 3.0, num_samples), 2)  # Vibration level\n",
        "pressure = np.random.randint(50, 400, num_samples)  # Pressure in kPa\n",
        "humidity = np.random.randint(20, 80, num_samples)  # Humidity in %\n",
        "machine_age = np.random.randint(1, 20, num_samples)  # Machine age in years\n",
        "\n",
        "# Generate failure labels (1 = Failure, 0 = No Failure) based on conditions\n",
        "failure = np.where(\n",
        "    (temperature > 80) & (vibration > 2.0) & (pressure > 300) & (humidity > 60),\n",
        "    1,  # High failure risk\n",
        "    np.random.choice([0, 1], size=num_samples, p=[0.85, 0.15])  # 15% random failures\n",
        ")\n",
        "\n",
        "# Create DataFrame\n",
        "df = pd.DataFrame({\n",
        "    \"Temperature\": temperature,\n",
        "    \"Vibration\": vibration,\n",
        "    \"Pressure\": pressure,\n",
        "    \"Humidity\": humidity,\n",
        "    \"Machine_Age\": machine_age,\n",
        "    \"Failure\": failure\n",
        "})\n",
        "\n",
        "# Save dataset as CSV file\n",
        "csv_filename = \"iot_sensor_data.csv\"\n",
        "df.to_csv(csv_filename, index=False)\n",
        "print(f\"Dataset generated and saved as '{csv_filename}' successfully!\")\n",
        "\n",
        "# Display first 5 rows of the dataset\n",
        "print(\"\\nFirst 5 rows of the dataset:\")\n",
        "print(df.head())\n",
        "\n",
        "# Load dataset (if running separately)\n",
        "df = pd.read_csv(\"iot_sensor_data.csv\")\n",
        "\n",
        "# Split dataset into features and labels\n",
        "X = df.drop(columns=['Failure'])  # Features\n",
        "y = df['Failure']  # Target variable\n",
        "\n",
        "# Split into training (80%) and testing (20%) sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n"
      ],
      "metadata": {
        "id": "AjoFkPXp6xy7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Train a Random Forest model\n",
        "model_rf = RandomForestClassifier(n_estimators=100, random_state=42)\n",
        "model_rf.fit(X_train, y_train)\n",
        "\n",
        "# Predictions and Evaluation for Random Forest\n",
        "y_pred_rf = model_rf.predict(X_test)\n",
        "accuracy_rf = accuracy_score(y_test, y_pred_rf)\n",
        "print(\"\\nRandom Forest Model Accuracy:\", accuracy_rf)\n",
        "print(\"\\nRandom Forest Classification Report:\\n\", classification_report(y_test, y_pred_rf))\n",
        "\n",
        "# Confusion Matrix Visualization for Random Forest\n",
        "plt.figure(figsize=(5, 4))\n",
        "sns.heatmap(confusion_matrix(y_test, y_pred_rf), annot=True, fmt='d', cmap='Blues',\n",
        "            xticklabels=['No Failure', 'Failure'], yticklabels=['No Failure', 'Failure'])\n",
        "plt.xlabel(\"Predicted\")\n",
        "plt.ylabel(\"Actual\")\n",
        "plt.title(\"Random Forest Confusion Matrix\")\n",
        "plt.show()\n",
        "\n",
        "# Feature Importance Analysis for Random Forest\n",
        "feature_importance = pd.Series(model_rf.feature_importances_, index=X.columns).sort_values(ascending=False)\n",
        "plt.figure(figsize=(8, 5))\n",
        "sns.barplot(x=feature_importance, y=feature_importance.index)\n",
        "plt.xlabel(\"Feature Importance Score\")\n",
        "plt.ylabel(\"Features\")\n",
        "plt.title(\"Feature Importance in Random Forest Model\")\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "Sg2aEeL07f4n"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "from tensorflow.keras.models import Sequential\n",
        "from tensorflow.keras.layers import Dense\n",
        "\n",
        "# Set random seed for reproducibility\n",
        "np.random.seed(42)\n",
        "\n",
        "# Generate synthetic IoT sensor data\n",
        "num_samples = 1000\n",
        "iot_data = pd.DataFrame({\n",
        "    \"Temperature\": np.random.randint(30, 100, num_samples),\n",
        "    \"Vibration\": np.round(np.random.uniform(0.1, 3.0, num_samples), 2),\n",
        "    \"Pressure\": np.random.randint(50, 400, num_samples),\n",
        "    \"Humidity\": np.random.randint(20, 80, num_samples),\n",
        "    \"Machine_Age\": np.random.randint(1, 20, num_samples)\n",
        "})\n",
        "\n",
        "# Generate Failure labels (1 = Failure, 0 = No Failure)\n",
        "failure = np.where(\n",
        "    (iot_data['Temperature'] > 80) &\n",
        "    (iot_data['Vibration'] > 2.0) &\n",
        "    (iot_data['Pressure'] > 300) &\n",
        "    (iot_data['Humidity'] > 60),\n",
        "    1,\n",
        "    np.random.choice([0, 1], num_samples, p=[0.85, 0.15])\n",
        ")\n",
        "iot_data['Failure'] = failure\n",
        "\n",
        "# Split data into features and labels\n",
        "X = iot_data.drop(columns=['Failure'])\n",
        "y = iot_data['Failure']\n",
        "\n",
        "# Split into training (80%) and testing (20%) sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "\n",
        "# Train a Random Forest Classifier\n",
        "rf_model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
        "rf_model.fit(X_train, y_train)\n",
        "\n",
        "# Make predictions and evaluate accuracy\n",
        "rf_predictions = rf_model.predict(X_test)\n",
        "accuracy_rf = accuracy_score(y_test, rf_predictions)\n",
        "print(f\"Random Forest Model Accuracy: {accuracy_rf * 100:.2f}%\")\n",
        "\n",
        "# Generate and plot confusion matrix\n",
        "conf_matrix_rf = confusion_matrix(y_test, rf_predictions)\n",
        "sns.heatmap(conf_matrix_rf, annot=True, fmt='d', cmap='Blues',\n",
        "            xticklabels=['No Failure', 'Failure'], yticklabels=['No Failure', 'Failure'])\n",
        "plt.xlabel(\"Predicted\")\n",
        "plt.ylabel(\"Actual\")\n",
        "plt.title(\"Confusion Matrix - IoT Failure Prediction (Random Forest)\")\n",
        "plt.show()\n",
        "\n",
        "# Feature importance visualization\n",
        "feature_importance = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values(ascending=False)\n",
        "plt.figure(figsize=(8, 5))\n",
        "sns.barplot(x=feature_importance, y=feature_importance.index)\n",
        "plt.xlabel(\"Feature Importance Score\")\n",
        "plt.ylabel(\"Features\")\n",
        "plt.title(\"Feature Importance in IoT Failure Prediction (Random Forest)\")\n",
        "plt.show()\n",
        "\n",
        "# Neural Network Model\n",
        "nn_model = Sequential([\n",
        "    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  # Input layer\n",
        "    Dense(32, activation='relu'),  # Hidden layer\n",
        "    Dense(1, activation='sigmoid')  # Output layer for binary classification\n",
        "])\n",
        "\n",
        "nn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n",
        "\n",
        "# Train the neural network\n",
        "history = nn_model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=0)\n",
        "\n",
        "# Evaluate the neural network\n",
        "nn_loss, nn_accuracy = nn_model.evaluate(X_test, y_test, verbose=0)\n",
        "print(f\"Neural Network Model Accuracy: {nn_accuracy * 100:.2f}%\")\n",
        "\n",
        "# Predictions and confusion matrix for Neural Network\n",
        "nn_predictions = (nn_model.predict(X_test) > 0.5).astype(\"int32\")\n",
        "conf_matrix_nn = confusion_matrix(y_test, nn_predictions)\n",
        "sns.heatmap(conf_matrix_nn, annot=True, fmt='d', cmap='Blues',\n",
        "            xticklabels=['No Failure', 'Failure'], yticklabels=['No Failure', 'Failure'])\n",
        "plt.xlabel(\"Predicted\")\n",
        "plt.ylabel(\"Actual\")\n",
        "plt.title(\"Confusion Matrix - IoT Failure Prediction (Neural Network)\")\n",
        "plt.show()\n",
        "\n",
        "# Plot training history\n",
        "plt.plot(history.history['accuracy'], label='accuracy')\n",
        "plt.plot(history.history['val_accuracy'], label='val_accuracy')\n",
        "plt.xlabel('Epoch')\n",
        "plt.ylabel('Accuracy')\n",
        "plt.legend()\n",
        "plt.title('Model Accuracy Over Epochs')\n",
        "plt.show()\n",
        "\n",
        "# Compare Model Accuracies\n",
        "comparison_data = pd.DataFrame({\n",
        "    'Model': ['Random Forest', 'Neural Network'],\n",
        "    'Accuracy': [accuracy_rf * 100, nn_accuracy * 100]\n",
        "})\n",
        "print(comparison_data)\n",
        "\n",
        "sns.barplot(x='Model', y='Accuracy', data=comparison_data)\n",
        "plt.title('Model Accuracy Comparison')\n",
        "plt.ylabel('Accuracy (%)')\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "wvAaGir57koX"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}