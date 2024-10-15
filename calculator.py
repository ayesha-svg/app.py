{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOnr6+aGcjXaX2zRrKi6cK1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ayesha-svg/app.py/blob/main/calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JTkIpohz2zpH",
        "outputId": "22b93ff2-3f1c-4ab7-f109-1a1d642ef4d7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "import math\n",
        "\n",
        "st.title(\"Scientific Calculator\")\n",
        "\n",
        "# Function to perform calculations\n",
        "def calculate(operation, value1, value2):\n",
        "    if operation == 'Addition':\n",
        "        return value1 + value2\n",
        "    elif operation == 'Subtraction':\n",
        "        return value1 - value2\n",
        "    elif operation == 'Multiplication':\n",
        "        return value1 * value2\n",
        "    elif operation == 'Division':\n",
        "        return value1 / value2\n",
        "    elif operation == 'Square Root':\n",
        "        return math.sqrt(value1)\n",
        "    elif operation == 'Power':\n",
        "        return math.pow(value1, value2)\n",
        "\n",
        "# User inputs\n",
        "operation = st.selectbox(\"Select Operation\", ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Square Root', 'Power'])\n",
        "value1 = st.number_input(\"Enter first number\", value=0)\n",
        "value2 = st.number_input(\"Enter second number (for square root, enter first number only)\", value=0)\n",
        "\n",
        "if st.button(\"Calculate\"):\n",
        "    result = calculate(operation, value1, value2)\n",
        "    st.write(\"Result: \", result)\n"
      ]
    }
  ]
}